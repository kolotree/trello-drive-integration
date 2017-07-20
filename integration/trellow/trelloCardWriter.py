from integration.trellow.clientFactory import ClientFactory


class TrelloCardWriter:
    def __init__(self):
        self.trelloClientWrapper = ClientFactory().getClient()

    def add_invoices_for(self, company, input_invoices_count, output_invoices_count):
        print ('Company: %s, UF: %s, IF: %s' % (company.name, str(input_invoices_count), str(output_invoices_count)))
        card_name = '{0} (UF:{1} | IF:{2})'.format(company.name, input_invoices_count, output_invoices_count)
        card_description = '{0} - ID: {1}'.format(company.name, company.id)
        card = self.trelloClientWrapper.add_or_update_card(card_name, card_description)
        return False if card == [] or card == None else True
