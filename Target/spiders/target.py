import scrapy
from scrapy import Spider
from scrapy.http import Request, FormRequest
from selenium import webdriver
from scrapy.selector import Selector

class TargetSpider(scrapy.Spider):
    name = 'target'
    allowed_domains = ['target.com']
    start_urls = ['https://target.com/c/shop-all-categories/-/N-5xsxf/']

    def start_requests(self):
        self.driver = webdriver.Chrome('/Users/benweiss/Downloads/chromedriver2')
        self.driver.get('https://www.target.com/c/shop-all-categories/-/N-5xsxf')

        sel = Selector(text=self.driver.page_source)
        categories = sel.xpath('//a[@class="Link-sc-1khjl8b-0 ItemLink-sc-1eyz3ng-0 dJwaza iFCzmw"]/@href').extract()
        for category in categories:
            if 'https' in category:
                pass
            elif 'Indoor Christmas Decorations' in category:
                pass
            elif '/c/women/-/N-5xtd3' in category:
                pass
            elif '/c/men/-/N-18y1l' in category:
                pass
            elif '/c/young-adult/-/N-qh1tf' in category:
                pass
            elif '/c/kids/-/N-xcoz4' in category:
                pass
            elif '/c/baby/-/N-5xtly' in category:
                pass
            elif '/c/shoes/-/N-55b0t' in category:
                pass
            else:
                url = 'https://target.com' + category
                yield Request(url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        title = response.xpath('//div/a[@class="Link-sc-1khjl8b-0 styles__StyledTitleLink-mkgs8k-5 dJwaza jqiYMz h-display-block h-text-bold h-text-bs flex-grow-one"]/text()').extract()
        yield { 'title': title}
