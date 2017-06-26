from requests_oauthlib import OAuth1Session
from trello import TrelloClient
from integration.TrelloClientWrapper import TrelloClientWrapper

requestURL = "https://trello.com/1/OAuthGetRequestToken"
accessURL = "https://trello.com/1/OAuthGetAccessToken"
authorizeURL = "https://trello.com/1/OAuthAuthorizeToken"
appName = "Trello OAuth Example";

class AuthorizeOAuth():
    def __init__(self, clientKey, clientSecret, token, token_secret, board=None, list=None):
        self.client = TrelloClientWrapper(api_key=clientKey, api_secret=clientSecret, token=token, token_secret=token_secret, board=board, list=list)

    def getClient(self):
        return self.client