import unittest

from integration.trellow.clientFactory import ClientFactory


class TestTrelloIntegration(unittest.TestCase):

    @classmethod
    def CARD_NAME(self):
        return 'UnitTestCard - [0xffaabb1123]'

    def setUp(self):
        self.trelloClientWrapper = ClientFactory().getClient()

    def test_accessing_boards(self):
        board = self.trelloClientWrapper.get_current_board()
        self.assertIsNotNone(board)

    def test_add_card(self):
        card = self.trelloClientWrapper.add_card(self.CARD_NAME(), 'This is the test card created from Unit test')
        self.assertIsNotNone(card)

    def test_add_existing_card(self):
        self.test_add_card()
        card = self.trelloClientWrapper.add_card_conditionaly(self.CARD_NAME(), 'some other description')
        self.assertIsNone(card)

    def test_add_new_card(self):
        card = self.trelloClientWrapper.add_card_conditionaly(self.CARD_NAME(), 'some other description')
        self.assertIsNotNone(card)

    def test_card_search(self):
        self.test_add_card()
        card = self.trelloClientWrapper.get_card_by_name(self.CARD_NAME())
        self.assertIsNotNone(card)

    def tearDown(self):
        self.trelloClientWrapper.delete_card(self.CARD_NAME())


if __name__ == '__main__':
    unittest.main()