import httplib2
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
from oauth2client import tools
from googleapiclient.discovery import build


class ServiceProvider:
    def __init__(self, client_id, client_secret):
        self.scope = 'https://www.googleapis.com/auth/drive'
        self.client_id = client_id
        self.client_secret = client_secret

    def getDriveServiceInstance(self):
        flow = OAuth2WebServerFlow(self.client_id, self.client_secret, self.scope)

        storage = Storage('credentials.dat')
        credentials = storage.get()
        if credentials is None or credentials.invalid:
            credentials = tools.run_flow(flow, storage, tools.argparser.parse_args())

        http = httplib2.Http()
        http = credentials.authorize(http)

        service = build('drive', 'v3', http=http)
        return service
