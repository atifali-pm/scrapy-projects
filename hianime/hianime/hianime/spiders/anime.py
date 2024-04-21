import scrapy

from hianime.items import AnimeItem


class AnimeSpider(scrapy.Spider):
    name = "anime"
    allowed_domains = ["www.hianime.to"]
    start_urls = ["https://hianime.to/az-list"]

    def parse(self, response):
        animes = response.css('div.film_list-wrap div.flw-item')

        for anime in animes:
            anime_url = anime.css('a').attrib['href']
            if "/watch" in anime_url:
                anime_url = 'https://www.hianime.to' + anime_url.replace('/watch', '')
           

            yield response.follow(anime_url, callback=self.parse_anime_page)


        
        links = response.css("li.page-item a")
        for link in links:
            if "Next" in link.get():
                print("********************************")
                print(link.attrib['href'])
                print("********************************")
                next_page_url = 'https://www.hianime.to' + link.attrib['href']
                yield response.follow(next_page_url, callback=self.parse)


    def parse_anime_page(self, response):

        details = response.css('div.anisc-info-wrap div.anisc-info div.item-title')

        anime_item = AnimeItem()

        anime_item['image'] = response.css('div#ani_detail div.anis-content img').attrib['src']
        anime_item['title'] = response.css('div.anisc-detail h2 ::text').get()

        detail_array = []
        for detail in details:

            if "Overview:" in detail.css('span.item-head ::text').get():
                anime_item['overview'] = detail.css('div.text ::text').get()

            if "Japanese:" in detail.css('span.item-head ::text').get():
                anime_item['japanese'] = detail.css('span.name ::text').get()

            if "Aired:" in detail.css('span.item-head ::text').get():
                anime_item['aired'] = detail.css('span.name ::text').get()

            if "Premiered:" in detail.css('span.item-head ::text').get():
                anime_item['premiered'] = detail.css('span.name ::text').get()

            if "Duration:" in detail.css('span.item-head ::text').get():
                anime_item['duration'] = detail.css('span.name ::text').get()

            if "Status:" in detail.css('span.item-head ::text').get():
                anime_item['status'] = detail.css('span.name ::text').get()

            if "MAL Score:" in detail.css('span.item-head ::text').get():
                anime_item['mal_score'] = detail.css('span.name ::text').get()

            if "Genres:" in detail.css('span.item-head ::text').get():
                anime_item['genres'] = detail.css('span.name ::text').get()

            if "Studios:" in detail.css('span.item-head ::text').get():
                anime_item['studios'] = detail.css('a ::text').get()

            if "Producers:" in detail.css('span.item-head ::text').get():
                anime_item['producers'] = detail.css('a ::text').get()

        yield anime_item        
