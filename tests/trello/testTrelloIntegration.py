import unittest

from integration.trellow.clientFactory import ClientFactory


class TestTrelloIntegration(unittest.TestCase):

    @classmethod
    def CARD_NAME(self):
        return 'Test Company (UF:5, IF:3)'

    @classmethod
    def UPDATED_CARD_NAME(self):
        return 'Test Company (UF:15, IF:0)'

    @classmethod
    def COMPANY_NAME(self):
        return 'Company_42 - ID: 0BCQx123SAKF2K332K'

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

    def test_find_card_by_description(self):
        card = self.trelloClientWrapper.add_card(self.CARD_NAME(), self.COMPANY_NAME())
        results = self.trelloClientWrapper.get_card_by_description(self.COMPANY_NAME())
        self.assertIsNotNone(results[0])

    def test_add_and_update_card(self):
        card = self.trelloClientWrapper.add_or_update_card(self.CARD_NAME(), self.COMPANY_NAME())
        self.assertIsNotNone(card)
        card = self.trelloClientWrapper.add_or_update_card(self.UPDATED_CARD_NAME(), self.COMPANY_NAME())
        self.assertIsNotNone(card)
        self.assertEqual(card.name, self.UPDATED_CARD_NAME())

    def test_add_card_if_company_is_archived(self):
        card = self.trelloClientWrapper.add_card(self.CARD_NAME(), self.COMPANY_NAME())
        card.set_closed(True)
        card = self.trelloClientWrapper.add_card(self.CARD_NAME(), self.COMPANY_NAME())
        self.assertIsNotNone(card)


    def test_card_search(self):
        self.test_add_card()
        card = self.trelloClientWrapper.get_card_by_name(self.CARD_NAME())
        self.assertIsNotNone(card)

    def tearDown(self):
        self.trelloClientWrapper.delete_card(self.CARD_NAME())
        self.trelloClientWrapper.delete_card(self.UPDATED_CARD_NAME())


if __name__ == '__main__':
    unittest.main()