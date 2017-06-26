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
        authDict = self.read_auth_data_from_config()
        client_key = authDict['client_key']
        client_secret = authDict['client_secret']
        token = authDict['token']
        token_secret = authDict['token_secret']

        board_id = self.read_board_id_config()
        list_id = None
        list_name = 'Column 1'

        authorize_OAuth_ob = authorizeOAuth.AuthorizeOAuth(clientKey=client_key, clientSecret=client_secret, token=token, token_secret=token_secret, board=board_id, list=list_id)
        trello_client_wrapper = authorize_OAuth_ob.getClient()

        self.set_list(trello_client_wrapper, list_name)

        return trello_client_wrapper

    def set_list(self, trello_client_wrapper, list_name):
        lists = trello_client_wrapper.get_current_board().all_lists()
        current_list = next(item for item in lists if item.name == list_name)
        if current_list == None:
            print('List %s could not be found!' % list_name)
        else:
            trello_client_wrapper.set_current_list(current_list)

    def read_auth_data_from_config(self):
        config = self.get_configuration()
        auth_dict = {key : value for key, value in config['OAUTH'].items()}
        return auth_dict

    def read_board_id_config(self):
        return self.get_configuration()['BOARD']['board_id']

    def get_configuration(self):
        config = configparser.ConfigParser()
        config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
        config.read(config_file)
        return config