from integration.configuration.configuration import Configuration
from integration.gdrive.serviceProvider import ServiceProvider
from integration.gdrive.fileExplorer import FileExplorer
from integration.trellow.trelloCardWriter import TrelloCardWriter
from integration.services.companyService import CompanyService
from integration.services.rootService import RootService
from integration.myLogging.myLogger import get_my_logger_instance
import traceback

def get_file_explorer_instance(gdrive_client_id, gdrive_client_secret):
    gdrive_service = ServiceProvider(gdrive_client_id, gdrive_client_secret).getDriveServiceInstance()
    return FileExplorer(gdrive_service)

def get_trello_card_writer_instance():
    return TrelloCardWriter()

def get_company_service_instance(file_explorer, trello_card_writer):
    return CompanyService(file_explorer, trello_card_writer)

def get_root_service_instance(file_explorer, company_service):
    return RootService(file_explorer, company_service)

def get_root_service_instance_using(config):
    file_explorer = get_file_explorer_instance(config.get_gdrive_client_id(), config.get_gdrive_client_secret())
    trello_card_writer = get_trello_card_writer_instance()
    company_service = get_company_service_instance(file_explorer, trello_card_writer)
    root_service = get_root_service_instance(file_explorer, company_service)

    return root_service

def get_my_logger_instance_using(config):
    return get_my_logger_instance(config.get_logging_file_path(), config.get_logging_log_level())

# Read configuration, create service instances and process the root folder
configuration = Configuration()
myLogger = get_my_logger_instance_using(configuration)
try:
    root_service = get_root_service_instance_using(configuration)
    results = root_service.visit_companies_and_add_invoices_for(configuration.get_gdrive_root_folder_id())
    myLogger.log_trello_card_results(results)
except:
    tb = traceback.format_exc()
    myLogger.log_exception(tb)