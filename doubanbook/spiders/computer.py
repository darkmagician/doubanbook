# -*- coding: utf-8 -*-
import scrapy
from doubanbook.items import DoubanbookItem

class ComputerSpider(scrapy.Spider):
    name = "computer"
    allowed_domains = ["book.douban.com"]
    start_urls = ['https://book.douban.com/tag/%E8%AE%A1%E7%AE%97%E6%9C%BA']

    def parse(self, response):
       
        links = response.xpath('//*[@id="subject_list"]/ul/li/div[2]/h2/a')
        for link in links:
            item = DoubanbookItem()
            item['href'] = link.xpath('@href').extract_first();
            item['title'] = link.xpath('@title').extract_first();
            yield item
        
        next = response.xpath('//*[@class="next"]/a/@href').extract_first()
        if next is not None:
            yield scrapy.Request(response.urljoin(next))
            