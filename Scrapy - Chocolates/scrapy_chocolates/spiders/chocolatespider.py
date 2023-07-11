import scrapy


class ChocolatespiderSpider(scrapy.Spider):
    name = "chocolatespider"
    allowed_domains = ["chocolate.co.uk"]
    start_urls = ["https://www.chocolate.co.uk/collections/all"]

    def parse(self, response):
        products = response.css('product-item')
        
        for product in products:
            yield{
                'Name' : product.css('a.product-item-meta__title::text').get(),
                'Price' : product.xpath("//span[@class='price']/text()[2]").get(),
                'URL' : product.css('div.product-item-meta a').attrib['href']
                }
                
        next_page = response.css('[rel="next"] ::attr(href)').get()

        if next_page:
            next_page_url = 'https://www.chocolate.co.uk' + next_page
            yield response.follow(next_page_url, callback=self.parse)
