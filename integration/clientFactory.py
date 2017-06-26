from integration import authorizeOAuth
import configparser
import os

class ClientFactory():

    def __init__(self):
        pass

    def getClient(self):
        """
        Method will always return new client, on that way new congfiguration from .ini file will always be in app
        :return: Trello Client Wrapper
        """
        authDict = self.readAuthDataFromConfig()
        client_key = authDict['client_key']
        client_secret = authDict['client_secret']
        token = authDict['token']
        token_secret = authDict['token_secret']

        board_id = 'gOzNH8uG'
        list_id = None
        listName = 'Column 1'

        authorizeOAuthOb = authorizeOAuth.AuthorizeOAuth(clientKey=client_key, clientSecret=client_secret, token=token, token_secret=token_secret, board=board_id, list=list_id)
        trelloClientWrapper = authorizeOAuthOb.getClient()

        self.setList(trelloClientWrapper, listName)

        return trelloClientWrapper

    def setList(self, trelloClientWrapper, listName):
        lists = trelloClientWrapper.get_current_board().all_lists()
        currentList = next(item for item in lists if item.name == listName)
        if currentList == None:
            print('List %s could not be found!' % listName)
        else:
            trelloClientWrapper.set_current_list(currentList)

    def readAuthDataFromConfig(self):
        config = self.get_configuration()
        authDict = {key : value for key, value in config['OAUTH'].items()}
        return authDict

    def get_configuration(self):
        config = configparser.ConfigParser()
        config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
        config.read(config_file)