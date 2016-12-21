# -*- coding: UTF-8 -*-
import scrapy

class LagouJobSpider(scrapy.Spider):
    name = "lagou_job"
    start_urls = ['https://www.lagou.com/zhaopin/qianduankaifa/1/']
    def parse(self, response):
        for job in response.css('ul.item_con_list>li.con_list_item'):
            yield {
                'position_id': job.css('.con_list_item::attr(data-positionid)').extract_first(),
                'salary': job.css('.con_list_item::attr(data-salary)').extract_first(),
                'company': job.css('.con_list_item::attr(data-company)').extract_first(),
                'position_name': job.css('.con_list_item::attr(data-positionname)').extract_first(),
                'position_link': 'https:' + job.css('.list_item_top a.position_link::attr(href)').extract_first(),
                'company_desc': job.css('.list_item_top .company .industry::text').extract_first().strip(),
                'company_pros': job.css('.list_item_bot .li_b_r::text').extract_first(),
            }

        next_page = response.css('.pager_container a')[-1].css('a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

