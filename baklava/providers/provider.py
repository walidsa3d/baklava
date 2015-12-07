import browseragents as ba


class BaseProvider(object):

    """A base class for search providers"""

    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {'Referer': self.base_url, 'User-Agent': ba.random()}

    def search(self, query):
        pass

    def get_top(self):
        pass
