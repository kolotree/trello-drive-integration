from requests_oauthlib import OAuth1Session
from integration.configuration.configuration import Configuration


def save_tokens(config, token, token_secret):
    config.save_property('token', token)
    config.save_property('token_secret', token_secret)

config = Configuration()
client_key = config.get_client_key()
client_secret = config.get_client_secret()

oauth = OAuth1Session(client_key,client_secret)

fetch_response = oauth.fetch_request_token(config.get_request_url())

resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')

authorization_url = oauth.authorization_url(config.get_authorize_url())
print('Please go here and authorize,', authorization_url+'&expiration=never')

verifier = input('Paste the verification token: ')

print('verifier: ' + verifier)

# Get Access Token

oauth = OAuth1Session(client_key,
                      client_secret=client_secret,
                      resource_owner_key=resource_owner_key,
                      resource_owner_secret=resource_owner_secret,
                      verifier=verifier)

oauth_tokens = oauth.fetch_access_token(config.get_access_url())

oauth_token = oauth_tokens.get('oauth_token')
oauth_token_secret = oauth_tokens.get('oauth_token_secret')


print('oauth_token: ' + oauth_token)
print('oauth_token_secret: ' + oauth_token_secret)
save_tokens(config, oauth_token, oauth_token_secret)