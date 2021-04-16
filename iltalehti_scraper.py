import scrapy


class IltalehtiScraperSpider(scrapy.Spider):
    name = 'iltalehti_scraper'
    allowed_domains = ['iltalehti.fi']
    start_urls = ['https://iltalehti.fi/']

    def parse(self, response):
        title_texts = response.css('.front-title.a-title-font::text')
        for title in title_texts:
            yield {'title': title.extract()}
'''         
        
import scrapy


class IltalehtiScraperSpider(scrapy.Spider):
    name = 'iltalehti_scraper'
    allowed_domains = ['iltalehti.fi']
    start_urls = ['https://iltalehti.fi/']

    def parse(self, response):
        title_texts = response.css('front-title.a-title-font')
        for i in range(len(title_texts)):
            title_texts[i] = "".join(title_texts[i].css('::text').extract()).strip()
            
        for i in range(len(review_texts)):
            news = {
                'title': title_texts[i]
            }
            yield news
'''