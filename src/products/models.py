from django.db import models

from .tasks import scrape_product_url_task

class Product(models.Model):
    asin = models.CharField(max_length=120, unique=True, db_index=True)
    url = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=220, unique=True, db_index=True)
    current_price = models.FloatField(blank=True, null=True, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    metadata = models.JSONField(blank=True, null=True)
    trigger_scrape = models.BooleanField(default=False)
    _trigger_scrape = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.url and self.pk:
            if self.trigger_scrape is not self._trigger_scrape:
                # add the product to the celery to be done async
                scrape_product_url_task.delay(self.url)
        super().save(*args, **kwargs)
     


class ProductScrapeEventManager(models.Manager):
    def create_scrape_event(self, data, url=None):
        asin = data.get('asin')
        if asin is None:
            return None
        product, _ = Product.objects.update_or_create(
            asin=asin,
            defaults={
                "url": url,
                "title": data.get("title") or "",
                "current_price": data.get("price") or 0.00,
                "metadata": data,
            }
        )
        event = self.create(
            product=product,
            url=url,
            asin=asin,
            data=data,
        )
        return event

class ProductScrapeEvent(models.Model): 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='scrape_events')
    asin = models.CharField(max_length=120, null=True, blank=True)
    url = models.URLField(blank=True, null=True)
    data = models.JSONField(blank=True, null=True)
    
    objects = ProductScrapeEventManager()