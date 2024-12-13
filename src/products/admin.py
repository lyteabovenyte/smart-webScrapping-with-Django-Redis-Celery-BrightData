from django.contrib import admin

from .models import Product, ProductScrapeEvent

admin.site.register(Product)
admin.site.register(ProductScrapeEvent)
