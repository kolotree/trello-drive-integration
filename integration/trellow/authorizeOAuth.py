from integration.trellow.TrelloClientWrapper import TrelloClientWrapper

class AuthorizeOAuth():
    def __init__(self, clientKey, clientSecret, token, token_secret, board=None, list=None):
        self.client = TrelloClientWrapper(api_key=clientKey, api_secret=clientSecret, token=token, token_secret=token_secret, board=board, list=list)

    def getClient(self):
        return self.client