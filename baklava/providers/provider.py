import browseragents as ba
from abc import ABCMeta, abstractmethod


class BaseProvider(object):

    """A base class for search providers"""
    __metaclass__ = ABCMeta

    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {'Referer': self.base_url, 'User-Agent': ba.random()}

    @abstractmethod
    def search(self, query):
        pass

    @abstractmethod
    def get_top(self):
        pass
