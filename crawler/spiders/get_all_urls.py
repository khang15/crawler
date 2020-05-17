from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = '123nhadat'
    allowed_domain = ['123nhadat.com']

    start_urls = ['http://123nhadat.vn']

    rules = (Rule(LinkExtractor(), callback='parse_url', follow=True))

    def parse_url(self, response):
        url = response.url
        yield url

