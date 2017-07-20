import logging


class MyLogger:
    def __init__(self, logFilePath, logLevel):
        fileHandler = logging.FileHandler(logFilePath)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        fileHandler.setFormatter(formatter)

        self.logger = logging.getLogger('trello-drive-integration')
        self.logger.addHandler(fileHandler)
        self.logger.setLevel(logLevel)

    def log_trello_card_results(self, trello_card_results):
        for result in trello_card_results:
            self.logger.info('Company: %s, Is card added: %s. (UF: %s, IF: %s)' % (result.company, result.is_success, str(result.input_invoices_count), str(result.output_invoices_count)))

    def log_exception(self, exception):
        self.logger.error(exception)

    def log_info(self, message):
        self.logger.info(message)