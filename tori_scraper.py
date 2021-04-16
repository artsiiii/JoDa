'''import scrapy

class ToriScraper(scrapy.Spider):
    name = 'tori_scraper'
    allowed_domains =['tori.fi']
    start_urls = ['https://www.tori.fi/koko_suomi/kodinkoneet/tiskikoneet?ca=18&st=s&st=k&st=u&st=h&st=g&w=3&cg=3010&c=3011']
        
    def parse(self, response):       
        for item in response.css('.li-title:'):
            yield {'title': item.extract()}
            break'''
        
import scrapy

class ToriScraper(scrapy.Spider):
    name = 'toriscraper'
    allowed_domains =['tori.fi']
    start_urls = ['https://www.tori.fi/koko_suomi/kodinkoneet/tiskikoneet?ca=18&st=s&st=k&st=u&st=h&st=g&w=3&cg=3010&c=3011']
        
    def parse(self, response):       
        titles = response.css('.li-title')        
        for i in range(len(titles)):
            titles[i] = "".join(titles[i].css('::text').extract()).strip()
            
        price = response.css('.list_price ineuros')
        for i in range(len(price)):
            price[i] = "".join(titles[i].css('::text').extract()).strip()
        
        for i in range(len(titles)):
            product = {
                'title': titles[i],
                'price': price[i]
            }
            yield product
           
    
       
        
        
    

              
            
           