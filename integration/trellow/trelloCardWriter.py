from integration.myLogging.loggerFactory import LoggerFactory
from integration.trellow.clientFactory import ClientFactory
from integration.configuration.configuration import Configuration
from trello.exceptions import ResourceUnavailable


class TrelloCardWriter:
    def __init__(self):
        self.trelloClientWrapper = ClientFactory().getClient()
        self.myLogger = LoggerFactory().getLoggerInstance()

    def add_invoices_for(self, company, invoice_groups):
        print ('Company: %s, %s' % (company.name, str(invoice_groups)))
        card_name = '{0} ({1})'.format(company.name, str(invoice_groups))
        card_description = '{0} - ID: {1}'.format(company.name, company.id)
        card = self.trelloClientWrapper.add_or_update_card(card_name, card_description)
        self.assign_member_to_card(card[1])
        return card[0]

    def assign_member_to_card(self, card):
        if (card == None):
            return
        member_name = self.get_member_by_card_name(card.name)
        member = None if member_name == None else self.trelloClientWrapper.get_member(member_name)
        if (member != None and member.id != None):
            try:
                self.myLogger.log_info('Adding Member "{0}" to Card "{1}"'.format(member_name, card.name))
                card.assign(member.id)
            except ResourceUnavailable as ru:
                self.myLogger.log_exception(ru)


    def get_member_by_card_name(self, card_name):
        return Configuration().get_assigned_user_for_company(card_name)
