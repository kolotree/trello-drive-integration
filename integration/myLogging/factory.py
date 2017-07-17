from .myLogger import MyLogger
from .mailNotifier import MailNotifier

def get_my_logger_instance(logFilePath, logLevel, from_address, from_password, to_list):
    return MailNotifier(MyLogger(logFilePath, logLevel), from_address, from_password, to_list)