# -*- coding: utf-8 -*-

class Torrent(object):

    def __init__(self):
        self.title = ''
        self.torrent_url = ''
        self.seeds = 0
        self.size = ''

    def __eq__(self, other):
        return self.title == other.title

    def __repr__(self):
        return unicode(self.title).encode('utf8')

    def __str__(self):
        return unicode(self.title).encode('utf8')
