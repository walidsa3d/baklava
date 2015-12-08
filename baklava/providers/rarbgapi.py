# -*- coding: utf-8 -*-
import requests

from models import Torrent
from provider import BaseProvider


class RarbgAPI(BaseProvider):

    def __init__(self, base_url):
        super(RarbgAPI, self).__init__(base_url)

    def _get_token(self):
        token_payload = {
            'get_token': 'get_token',
            'app_id': 'baklava',
        }
        response = requests.get(self.base_url, params=token_payload).json()
        self.token = response['token']

    def search(self, query):
        self._get_token()
        search_payload = {
            'sort': 'seeders',
            'category': 'movies',
            'mode': 'search',
            'app_id': 'baklava',
            'format': 'json_extended',
            'search_string': query,
            'token': self.token,

        }
        results = requests.get(self.base_url, params=search_payload).json()
        torrents = []
        for result in results['torrent_results']:
            t = Torrent()
            t.title = result['title']
            t.seeds = result['seeders']
            t.size = result['size']
            t.torrent_url = result['download']
            torrents.append(t)
        return torrents
