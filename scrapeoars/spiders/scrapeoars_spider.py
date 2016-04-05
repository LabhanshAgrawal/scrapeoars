import scrapy

class scrapeoarsSpider(scrapy.Spider):
    name = "scrapeoars"
    allowed_domains = ["http://172.26.142.75:4040/"]
    start_urls = [
        "http://172.26.142.75:4040/Common/CourseListing.asp"
    ]

    def parse(self, response):
        for sel in response.xpath('//html/body/center/table/tr[*]/td[1]/font/a/text()').extract():
            print sel
