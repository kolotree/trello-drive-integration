from integration.configuration.configuration import Configuration
from integration.myLogging.myLogger import MyLogger

class LoggerFactory:
    logger_instance = None

    def __init__(self, config = Configuration()):
        self.config = config

    def getLoggerInstance(self):
        return self.get_my_logger_instance_using(self.config)

    def get_my_logger_instance_using(self, config):
        return self.get_my_logger_instance(config.get_logging_file_path(), config.get_logging_log_level())

    def get_my_logger_instance(self, logFilePath, logLevel):
        if (LoggerFactory.logger_instance == None):
            LoggerFactory.logger_instance = MyLogger(logFilePath, logLevel)
        return LoggerFactory.logger_instance

