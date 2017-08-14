from integration.trellow.clientFactory import ClientFactory


class TrelloCardWriter:
    def __init__(self):
        self.trelloClientWrapper = ClientFactory().getClient()

    def add_invoices_for(self, company, invoice_groups):
        print ('Company: %s, %s' % (company.name, str(invoice_groups)))
        card_name = '{0} ({1})'.format(company.name, str(invoice_groups))
        card_description = '{0} - ID: {1}'.format(company.name, company.id)
        card = self.trelloClientWrapper.add_or_update_card(card_name, card_description)
        return False if card == [] or card == None else True
