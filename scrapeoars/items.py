# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapeoarsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    course_no = scrapy.Field()
    title = scrapy.Field()
    instructor = scrapy.Field()
    instructor_mail = scrapy.Field()
    pre_req = scrapy.Field()
    credits = scrapy.Field()
    dept = scrapy.Field()
    schedule = scrapy.Field()
    instructor_notes = scrapy.Field()
    current_status = scrapy.Field()

