import configparser
import os

config_file = os.path.join(os.path.dirname(__file__), 'config.ini')

class Configuration():
    def __init__(self):
        pass

    def get_configuration(self):
        config = configparser.ConfigParser()
        config.read(config_file)
        return config

    def read_auth_data_from_config(self):
        config = self.get_configuration()
        auth_dict = {key: value for key, value in config['TRELLO_OAUTH'].items()}
        return auth_dict

    def get_client_key(self):
        return self.read_auth_data_from_config()['client_key']

    def get_client_secret(self):
        return self.read_auth_data_from_config()['client_secret']

    def read_board_id_config(self):
        return self.read_property('TRELLO_BOARD','board_id')

    def read_list_name_config(self):
        return self.read_property('TRELLO_LIST','list_name')

    def get_request_url(self):
        return self.read_property('TRELLO_OAUTH_URLS','requestURL')

    def get_access_url(self):
        return self.read_property('TRELLO_OAUTH_URLS','accessURL')

    def get_authorize_url(self):
        return self.read_property('TRELLO_OAUTH_URLS','authorizeURL')

    def get_gdrive_root_folder_id(self):
        return self.read_property('GDRIVE','root_folder_id')

    def get_gdrive_client_id(self):
        return self.read_property('GDRIVE','client_id')

    def get_gdrive_client_secret(self):
        return self.read_property('GDRIVE', 'client_secret')

    def get_logging_file_path(self):
        return self.read_property('LOGGING', 'file_path')

    def get_logging_log_level(self):
        return self.read_property('LOGGING', 'log_level')

    def read_property(self, section, key):
        return self.get_configuration()[section][key]

    def save_property(self, key, value, section='OAUTH'):
        config = self.get_configuration()
        config.set(section, key, value)
        with open(config_file, 'w') as configfile:
            config.write(configfile)