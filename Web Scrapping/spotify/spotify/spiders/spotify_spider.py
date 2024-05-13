import scrapy
import json

class SpotifySpider(scrapy.Spider):
    name = 'spotify'

    def start_requests(self):
        urls = [
            'https://spotifycharts.com/regional'
        ]

        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)

    def parse(self, response):
        tracks = response.css('td.chart-table-track strong::text').getall()
        authors = response.css('td.chart-table-track span::text').getall()
        streams = response.css('td.chart-table-streams::text').getall()


        data = {'tracks' : tracks,
                'authors' : authors,
                'streams' : [int(stream.replace(',', '')) for stream in streams]}
        json.dump(data, open('data.json', 'w'))
