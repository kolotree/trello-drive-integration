from integration.configuration.configuration import Configuration
from integration.trellow import authorizeOAuth


class ClientFactory():
    def __init__(self):
        pass

    def getClient(self):
        """
        Method will always return new client, on that way new congfiguration from .ini file will always be in app
        :return: Trello Client Wrapper
        """
        authDict = Configuration().read_auth_data_from_config()
        client_key = authDict['client_key']
        client_secret = authDict['client_secret']
        token = authDict['token']
        token_secret = authDict['token_secret']

        authorize_OAuth_ob = authorizeOAuth.AuthorizeOAuth(client_key,
                                                           client_secret,
                                                           token,
                                                           token_secret,
                                                           Configuration().read_board_id_config())

        trello_client_wrapper = authorize_OAuth_ob.getClient()
        self.set_list(trello_client_wrapper)
        return trello_client_wrapper

    def set_list(self, trello_client_wrapper):
        list_name = Configuration().read_list_name_config()
        lists = trello_client_wrapper.get_current_board().all_lists()
        current_list = next(item for item in lists if item.name == list_name)
        if current_list == None:
            print('List %s could not be found!' % list_name)
        else:
            trello_client_wrapper.set_current_list(current_list)

