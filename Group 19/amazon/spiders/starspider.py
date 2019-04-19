# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from amazon.items import AmazonItem


class AmazonSpider(scrapy.Spider):
    name = 'star'
    allowed_domains = ['amazon.in']
    start_urls = ['https://www.amazon.in/']

    def start_requests(self):
        url = "https://www.amazon.in/OPPO-Purple-16GB-Storage-Offers/dp/B07FJY24WL/ref=pd_rhf_gw_s_pd_crcd_0_4?_encoding=UTF8&pd_rd_i=B07FJY24WL&pd_rd_r=4ad5cb67-2674-4729-8785-a887f497101b&pd_rd_w=yiRMZ&pd_rd_wg=DBjxG&pf_rd_p=6376ac07-6b52-4317-b621-3080a4a917e5&pf_rd_r=R22F0PY861MD2RHRGXNV&psc=1&refRID=R22F0PY861MD2RHRGXNV"
        yield scrapy.Request(url=url, callback=self.parse)
      
    def parse(self, response):
        see_all_page = response.selector.xpath("//a[@class='a-link-emphasis a-text-bold']/@href").extract_first()
        see_all_page_link=response.urljoin(see_all_page)
        yield scrapy.Request(url=see_all_page_link, callback=self.parse)
        for review in response.selector.xpath("//div[@class='a-section a-spacing-none review-views celwidget']/div[@data-hook='review']"):
            #loader=ItemLoader(item=AmazonItem(), selector=review, response=response)
            #loader.add_xpath('review_title',".//a[@data-hook='review-title']/text()",)
            #loader.add_xpath('review_text',".//span[@data-hook='review-body']/text()")
            #yield loader.load_item()
                #records.append(record)
            yield{
                #'review_title' : review.xpath(".//a[@data-hook='review-title']/span[@class='cr-original-review-content']/text()").extract_first(),
                'review_star' : review.xpath(".//i[@data-hook='review-star-rating']/span[@class='a-icon-alt']/text()").extract_first()
            }
        next_page=response.selector.xpath("//div[@data-hook='pagination-bar']/ul/li[@class='a-last']/a/@href").extract_first()

        if next_page is not None:
            next_page_link=response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)


