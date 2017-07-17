from integration.trellow.clientFactory import ClientFactory


class TrelloCardWriter:
    def __init__(self):
        self.trelloClientWrapper = ClientFactory().getClient()

    def add_invoice_for(self, company, invoice):
        card_name = company.name + ': ' + invoice.name + '(' + invoice.id + ')'
        card_description = ''
        if self.trelloClientWrapper.add_card_conditionaly(card_name, card_description) is None:
            return False
        else:
            return True
