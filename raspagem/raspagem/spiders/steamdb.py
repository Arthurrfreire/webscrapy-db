import scrapy

class SteamSalesSpider(scrapy.Spider):
    name = "steamdb"
    start_urls = ['https://steamdb.info/sales/']

    def parse(self, response):
        for row in response.css('table.table-sales tbody tr'):
            game = row.css('td:nth-child(1) a::text').get()
            discount = row.css('td:nth-child(2) .discount span::text').get()
            price = row.css('td:nth-child(3) div::text').get()
            rating = row.css('td:nth-child(4) span::text').get()
            release_date = row.css('td:nth-child(5)::text').get()

            # Verifique se os dados foram extraídos corretamente
            if game and discount and price and rating and release_date:
                yield {
                    'game': game,
                    'discount': discount,
                    'price': price,
                    'rating': rating,
                    'release_date': release_date,
                }

