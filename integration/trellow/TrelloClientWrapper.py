from trello.trelloclient import TrelloClient
from integration.configuration.configuration import Configuration
from integration.myLogging.myLogger import MyLogger

class TrelloClientWrapper(TrelloClient):

    def __init__(self, api_key, api_secret=None, token=None, token_secret=None, board=None, list=None):
        super(TrelloClientWrapper, self).__init__(api_key, api_secret, token, token_secret)

        configuration = Configuration()
        self.myLogger = MyLogger(configuration.get_logging_file_path(), configuration.get_logging_log_level())

        if board == None :
            self.board = None
        else:
            self.board = self.get_board(board_id=board)

        if self.board == None or list == None:
            self.list = None
        else:
            self.list = self.board.get_list(list)

    def add_card(self, name, description):
        if self.board == None or self.list == None:
            self.myLogger.log_info('Card cannot be added because board and/or list ID is not defined')
            return None

        return self.list.add_card(name=name, desc=description)

    def add_card_conditionaly(self, name, description):
        if self.board == None or self.list == None:
            self.myLogger.log_info('Card cannot be added because board and/or list ID is not defined')
            return None

        current_card = self.get_card_by_name(name)

        if len(current_card) > 0:
            self.myLogger.log_info('Card "' + name + '" already exists')
            return None

        return self.add_card(name, description)

    def get_card_by_name(self, card_name):
        cards = [card for card in self.board.all_cards() if card.name == card_name]
        if len(cards) == 0:
            return []
        return cards

    def delete_card(self, card_name):
        cards = self.get_card_by_name(card_name)
        for card in cards:
            card.delete()

    def get_current_board(self):
        return self.board

    def get_current_list(self):
        return self.list

    def set_current_list(self, list):
        self.list = list