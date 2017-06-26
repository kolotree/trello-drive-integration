from trello import TrelloApi
from urllib import request

class AuthorizeRoute():
    def __init__(self, apikey):
        self.trello = TrelloApi(apikey)
        url = self.trello.get_token_url('trello')
        print(url)
        response = request.urlopen(url).read()

    def getTrello(self):
        return self.trello