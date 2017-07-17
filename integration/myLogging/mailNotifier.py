import yagmail
from datetime import datetime

class MailNotifier:
    def __init__(self, my_logger, from_address, from_password, to_list):
        self.my_logger = my_logger
        self.from_address = from_address
        self.from_password = from_password
        self.to_list = to_list.split(',')

    def log_trello_card_results(self, trello_card_results):
        self.my_logger.log_trello_card_results(trello_card_results)

        subject = self.__create_subject_for_sucessful_processing(trello_card_results)
        body = self.__create_mail_body_from_results(trello_card_results)
        self.__send_mail(subject, body)

    def log_exception(self, exception):
        self.my_logger.log_exception(exception)

        subject = self.__create_subject_for_failed_processing()
        body = self.__create_mail_body_from_exception(exception)
        self.__send_mail(subject, body)

    def __create_subject_for_sucessful_processing(self, trello_card_results):
        added_cards_count = len([r for r in trello_card_results if r.is_success])
        skipped_cards_count = len([r for r in trello_card_results if not r.is_success])
        datetime_now = str(datetime.now())
        return 'Trello-Drive-Integration tool successfully executed (' + datetime_now + '). Added cards: ' + str(added_cards_count) + '. Skipeed cards: ' + str(skipped_cards_count)

    def __create_subject_for_failed_processing(self):
        datetime_now = str(datetime.now())
        return 'Trello-Drive-Integration tool execution failed! (' + datetime_now + ')'

    def __create_mail_body_from_results(self, trello_card_results):
        added_cards = [('Company: %s: Invoice: %s') % (r.company.name, r.invoice.name) for r in trello_card_results if r.is_success]
        skipped_cards = [('Company: %s: Invoice: %s') % (r.company.name, r.invoice.name) for r in trello_card_results if not r.is_success]

        added_cards_body = 'The following cards are added:\n- ' + '\n- '.join(added_cards)
        skipped_cards_body = '\nThe following cards are skipped since they exist:\n- ' + '\n- '.join(skipped_cards)
        body = added_cards_body + '\n\n' + skipped_cards_body
        return body

    def __create_mail_body_from_exception(self, exception):
        return 'Processing failed with the following exception: ' + exception + '. See log files for more details.'

    def __send_mail(self, subject, body):
        yag = yagmail.SMTP(self.from_address, self.from_password)
        yag.send(self.to_list, subject, body)