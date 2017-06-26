from requests_oauthlib import OAuth1Session

requestURL = "https://trello.com/1/OAuthGetRequestToken"
accessURL = "https://trello.com/1/OAuthGetAccessToken"
#authorizeURL = "https://trello.com/1/OAuthAuthorizeToken"
authorizeURL = "https://trello.com/1/authorize?scope=read,write"
appName = "Trello OAuth Example"

client_key='ba807f65e19546e12ae15d7032620651'
client_secret='ce4d3aef857b1442977c06b18672724f72d47ab017ae264dff42e154b8e01888'

oauth = OAuth1Session(client_key,client_secret)

fetch_response = oauth.fetch_request_token(requestURL)

resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')

authorization_url = oauth.authorization_url(authorizeURL)
print('Please go here and authorize,', authorization_url)

verifier = input('Paste the verification token: ')

print('verifier: ' + verifier)

# Get Access Token

oauth = OAuth1Session(client_key,
                      client_secret=client_secret,
                      resource_owner_key=resource_owner_key,
                      resource_owner_secret=resource_owner_secret,
                      verifier=verifier)

oauth_tokens = oauth.fetch_access_token(accessURL)

oauth_token = oauth_tokens.get('oauth_token')
oauth_token_secret = oauth_tokens.get('oauth_token_secret')


print('oauth_token: ' + oauth_token)
print('oauth_token_secret: ' + oauth_token_secret)