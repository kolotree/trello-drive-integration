from integration import authorizeOAuth

class ClientFactory():

    def __init__(self):
        pass

    def getClient(self):
        client_key = 'ba807f65e19546e12ae15d7032620651'
        client_secret = 'ce4d3aef857b1442977c06b18672724f72d47ab017ae264dff42e154b8e01888'
        token = 'a8d52bcbfafa6e015311c4a4f55316bb97d35f6745f967a71817dba24396a0cc'
        token_secret = '8d62e2cfc08e92df29b7be0589a5fb69'
        board = 'gOzNH8uG'
        list = None
        listName = 'Column 1'

        authorizeOAuthOb = authorizeOAuth.AuthorizeOAuth(clientKey=client_key, clientSecret=client_secret, token=token, token_secret=token_secret, board=board, list=list)
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