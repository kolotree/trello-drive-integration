from integration.trellow.clientFactory import ClientFactory
from integration.configuration.configuration import Configuration

class TrelloCardWriter:
    def __init__(self):
        self.trelloClientWrapper = ClientFactory().getClient()

    def add_invoices_for(self, company, invoice_groups):
        print ('Company: %s, %s' % (company.name, str(invoice_groups)))
        card_name = '{0} ({1})'.format(company.name, str(invoice_groups))
        card_description = '{0} - ID: {1}'.format(company.name, company.id)
        card = self.trelloClientWrapper.add_or_update_card(card_name, card_description)
        # self.assign_member_to_card(card[1])
        return card[0]

    def assign_member_to_card(self, card):
        if (card == None):
            return
        member_id = self.get_member_by_card_name(card.name)
        if (member_id != None):
            card.assign(member_id)

    def get_member_by_card_name(self, card_name):
        return Configuration().get_assigned_user_for_company(card_name)
