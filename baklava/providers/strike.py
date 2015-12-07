import requests

from models import Torrent
from provider import BaseProvider


class Strike(BaseProvider):

    def __init__(self, base_url):
        super(Strike, self).__init__(base_url)

    def search(self, query):
        search_url = "https://getstrike.net/api/v2/torrents/search/"
        payload = {'phrase': query, 'category': 'Movies'}
        response = requests.get(
            search_url, params=payload, headers=self.headers).json()
        torrents = self._parse_page(response)
        return torrents

    def get_top(self):
        torrents = []
        return torrents

    def _parse_page(self, page_text):
        torrents = []
        for result in page_text['torrents']:
            t = Torrent()
            t.title = result['torrent_title']
            t.seeds = result['seeds']
            t.size = result['size']
            t.torrent_url = result['magnet_uri']
            torrents.append(t)
        return torrents[:50]
