from datetime import timedelta
from datetime import datetime
from trello.trelloclient import TrelloClient
from integration.configuration.configuration import Configuration
from integration.myLogging.loggerFactory import LoggerFactory

class TrelloClientWrapper(TrelloClient):

    def __init__(self, api_key, api_secret=None, token=None, token_secret=None, board=None, list=None):
        super(TrelloClientWrapper, self).__init__(api_key, api_secret, token, token_secret)

        self.configuration = Configuration()
        self.myLogger = LoggerFactory().getLoggerInstance()

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

        return self.list.add_card(name=name, desc=description, due=self.calculate_due_date())

    # deprecated
    def add_card_conditionaly(self, name, description):
        if self.board == None or self.list == None:
            self.myLogger.log_info('Card cannot be added because board and/or list ID is not defined')
            return None

        current_card = self.get_card_by_name(name)

        if len(current_card) > 0:
            self.myLogger.log_info('Card "' + name + '" already exists')
            return None

        return self.add_card(name, description)

    def add_or_update_card(self, name, description):
        results = self.get_opened_cards_by_description(description)
        if len(results) > 1:
            self.myLogger.log_info('Found more than 1 card with description: ' + description)
            return [False, None]

        if results == []:
            card = self.add_card(name, description)
            return [True, card]
        else:
            results[0].set_name(name)
            return [False, results[0]]

    def get_card_by_name(self, card_name):
        cards = [card for card in self.board.all_cards() if card.name == card_name]
        if len(cards) == 0:
            return []
        return cards

    def get_opened_cards_by_description(self, description):
        all_cards = self.search(description, partial_match=False, models=['cards'],board_ids=[self.board.id])
        results = [card for card in all_cards if card.closed == False]
        return results

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
		
    def calculate_due_date(self):
        return str(datetime.utcnow() + timedelta(days=self.configuration.get_due_days_from_now()))