### building **SMART** Web Scraping platform using **Django** and **Selenium** to avoid bot captcha and run it on certain intervals using **Celery**

features:
- integrating **Celery** & **Redis** --> Queuing Celery tasks into Redis.
- using [brigh data](https://brightdata.com) proxies to solve captcha and integrate it with *selenium*
- taking screenshots of the url. 👻
- using jupyter notebook and `bs4.BeautifulSoup` to interact with our parsed data and find the wanted portion of the returned html --> located at `/src/nbs`
- 