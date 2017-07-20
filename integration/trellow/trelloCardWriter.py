from integration.trellow.clientFactory import ClientFactory


class TrelloCardWriter:
    def __init__(self):
        self.trelloClientWrapper = ClientFactory().getClient()

    def add_invoices_for(self, company, input_invoices_count, output_invoices_count):
        print ('Company: %s, UF: %s, IF: %s' % (company.name, str(input_invoices_count), str(output_invoices_count)))
        return True
