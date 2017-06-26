from integration.clientFactory import ClientFactory

def addCard(listId, cardName, description=None):
    pass
    #trello.cards.new(idList=listId, name=cardName, desc=description)

#token = 'e6f56db8c666c9474a6fcc4980fa900ce751a56ec3deb26860b53a58ea30bb23'
trelloClient = ClientFactory().getClient()

board = trelloClient.get_board('gOzNH8uG')

lists = board.all_lists()

list = lists[0]

print(list.list_cards('all'))

list.add_card('123', 'asd')

###### authorizeRoute with old trello lib TrelloApi

#trello = authorizeRoute.AuthorizeRoute('ba807f65e19546e12ae15d7032620651').getTrello()

#trello.set_token(token)

#board = trello.boards.get('gOzNH8uG')

#lists = trello.boards.get_list('gOzNH8uG')

#addCard('594ce8f803425fb590fb3ff7', 'Test', 'some description')

#print(lists)


