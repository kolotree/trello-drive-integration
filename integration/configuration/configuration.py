import configparser
import os
import sys

class Configuration():
    def __init__(self):
        pass

    def get_config_file(self):
        return self.find_data_file('config.ini')

    def find_data_file(self, filename):
        if getattr(sys, 'frozen', False):
            # The application is frozen
            datadir = os.path.dirname(sys.executable)
        else:
            # The application is not frozen
            # Change this bit to match where you store your data files:
            datadir = os.path.dirname(__file__)

        return os.path.join(datadir, filename)

    def get_configuration(self):
        config = configparser.ConfigParser()
        config.read(self.get_config_file())
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

    def get_gdrive_root_folder_ids(self):
        return self.read_property('GDRIVE','root_folder_ids')

    def get_gdrive_client_id(self):
        return self.read_property('GDRIVE','client_id')

    def get_gdrive_client_secret(self):
        return self.read_property('GDRIVE', 'client_secret')

    def get_gdrive_invoice_groups(self):
        return self.read_property('GDRIVE', 'invoice_groups').split(',')

    def get_logging_file_path(self):
        return self.read_property('LOGGING', 'file_path')

    def get_logging_log_level(self):
        return self.read_property('LOGGING', 'log_level')

    def get_logging_from_address(self):
        return self.read_property('LOGGING', 'from_address')

    def get_logging_from_password(self):
        return self.read_property('LOGGING', 'from_password')

    def get_logging_to_list(self):
        return self.read_property('LOGGING', 'to_list')

    def read_property(self, section, key):
        return self.get_configuration()[section][key]

    def save_property(self, key, value, section='TRELLO_OAUTH'):
        config = self.get_configuration()
        config.set(section, key, value)
        with open(self.get_config_file(), 'w') as configfile:
            config.write(configfile)

    def get_dict_in_section(self, section='AUTO_ASSIGN_MEMBER_TO_CARD'):
        return dict(self.get_configuration().items(section))

    def get_assigned_user_for_company(self, company_name):
        users = self.get_dict_in_section()
        for user, all_companies in users.items():
            list_of_companies = all_companies.split(',')
            for company in list_of_companies:
                if company_name.find(company.strip()) >= 0:
                    return user
        return None

    def get_label_color_for_company(self, company_name):
        labels_with_companies = self.get_dict_in_section('LABELS')
        for color, all_companies in labels_with_companies.items():
            list_of_companies = all_companies.split(',')
            for company in list_of_companies:
                if company_name.find(company.strip()) >= 0:
                    return color
        return None
