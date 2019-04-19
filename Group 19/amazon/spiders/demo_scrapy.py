import scrapy

class DemoSpider(scrapy.Spider):
    name = 'demo_amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/']

    def start_requests(self):
        url = "https://www.amazon.com/Apple-iPhone-6S-Plus-Unlocked/dp/B01EVPCFH0/ref=br_asw_pdt-11?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=&pf_rd_r=5QWFBYQ7CF676CMMNKK0&pf_rd_t=36701&pf_rd_p=74c2af8b-5acb-4bf8-b252-8b1584c94b14&pf_rd_i=desktop"
        yield scrapy.Request(url=url, callback=self.parse)
      
    def parse(self, response):
        star = response.xpath(".//div[@id='averageCustomerReviews_feature_div']//span[@class='a-icon-alt']/text()").extract_first()
        print(star)