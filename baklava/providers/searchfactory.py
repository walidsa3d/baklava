# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from constants import (
    TPB_URL, KICKASS_URL, NYAA_URL, YTS_URL, CPABSIEN_URL, STRIKE_URL, RARBG_API_URL)
from cpasbien import Cpasbien
from kickass import Kickass
from nyaa import Nyaa
from operator import attrgetter
from strike import Strike
from tpb import TPB
from yts import YTS
from rarbgapi import RarbgAPI

providers = {
    "kickass": (Kickass, KICKASS_URL),
    "rarbg": (RarbgAPI, RARBG_API_URL),
    "yts": (YTS, YTS_URL),
    "thepiratebay": (TPB, TPB_URL),
    "cpasbien": (Cpasbien, CPABSIEN_URL),
    "strike": (Strike, STRIKE_URL),
    "nyaa": (Nyaa, NYAA_URL),
}


class SearchFactory(object):

    def __init__(self, provider):
        self.provider = provider

    def search(self, query, max=20):
        provider_class, site_url = providers.get(
            self.provider, ('tpb', TPB_URL))
        results = provider_class(site_url).search(query)
        self.results = results[:max]
        return self

    def sortBy(self, *args):
        '''sort results by given criteria'''
        criteria = ['seeds', 'size']
        for k in args:
            if k in criteria:
                self.results = sorted(
                    self.results, key=attrgetter(k), reverse=True)
        return self

    def filterBy(self, **kwargs):
        ''' filter results by given criteria'''
        criteria = ['seeds', 'size']
        for k, v in kwargs.iteritems():
            if k in criteria:
                self.results = filter(
                    lambda x: getattr(x, k) >= v, self.results)
        return self

    def get(self):
        return self.results

    def get_top(self, provider):
        provider_class, site_url = providers.get(provider, ('tpb', TPB_URL))
        results = provider_class(site_url).get_top()
        return results
