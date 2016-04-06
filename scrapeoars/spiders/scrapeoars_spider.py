import scrapy
import re

from scrapeoars.items import ScrapeoarsItem

class scrapeoarsSpider(scrapy.Spider):
    name = "scrapeoars"
    allowed_domains = ["172.26.142.75"]
    start_urls = [
        "http://172.26.142.75:4040/Common/CourseListing.asp"
    ]

    def parse(self, response):
        for CourseName in response.xpath('//html/body/center/table/tr[*]/td[1]/font/a/text()').extract():
            url = "http://172.26.142.75:4040/Utils/CourseInfoPopup2.asp?Course=" + CourseName
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = ScrapeoarsItem()
        item['course_no'] = response.xpath('//html/body/table/tr[1]/td[2]/text()').extract()
        item['title'] = response.xpath('//html/body/table/tr[2]/td[2]/text()').extract()
        item['instructor'] = response.xpath('//html/body/table/tr[3]/td[2]/text()').extract()
        item['instructor_mail'] = response.xpath('//html/body/table/tr[4]/td[2]/text()').extract()
        item['pre_req'] = response.xpath('//html/body/table/tr[5]/td[2]/text()').extract()
        item['credits'] = response.xpath('//html/body/table/tr[6]/td[2]/text()').extract()
        item['dept'] = response.xpath('//html/body/table/tr[7]/td[2]/text()').extract()
        text = ''.join(response.xpath('//html/body/table/tr[8]/td[2]/text()').extract())
        item['schedule'] = str(re.sub(r"\s+", " ", text))
        item['instructor_notes'] = response.xpath('//html/body/table/tr[9]/td[2]/text()').extract()
        item['current_status'] = response.xpath('//html/body/table/tr[10]/td[2]/text()').extract()
        yield item