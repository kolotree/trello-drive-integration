from .clientFactory import ClientFactory


class TrelloCardWriter:
    def __init__(self):
        self.trelloClientWrapper = ClientFactory().getClient()

    def add_invoice_for(self, company, invoice):
        card_name = company.name + ': ' + invoice.name
        card_description = 'My description'
        if self.trelloClientWrapper.add_card_conditionaly(card_name, card_description) == None:
            return False
        else:
            return True
