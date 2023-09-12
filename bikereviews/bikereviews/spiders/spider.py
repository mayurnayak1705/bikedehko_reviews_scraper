import scrapy


class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["www.bikedekho.com"]
    start_urls = ["https://www.bikedekho.com/yezdi-motorcycles-bikes"]

    def parse(self, response):
        bike_links=response.css('section.gsc_row.gsc_container_hold.heading.BrandPagelist.marginTop20   h3 a::attr(href)').getall()
        new_list = ['https://www.bikedekho.com' + item for item in bike_links]

        print(new_list)