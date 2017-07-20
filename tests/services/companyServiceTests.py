from unittest import TestCase
from integration.services.companyService import CompanyService
from integration.services.domain import Company
from tests.gdrive.fileExplorerTests import get_test_file_explorer_instance
from tests.trello.trelloCardWriterTests import get_test_trello_card_writer_instance

def get_test_company_service_instance():
    return CompanyService(get_test_file_explorer_instance(), get_test_trello_card_writer_instance())

company_id = '0B1gzQBsHQ8rvdGZUUWN3RW5EcnM'
company_name= 'Company0'
company = Company(company_id, company_name)


class CompanyServiceTests(TestCase):
    def test_card_is_added_for_company(self):
        companyService = get_test_company_service_instance()
        add_trello_card_result = companyService.addTrelloCardFromCompanyDrive(company)
        self.assertTrue(add_trello_card_result.is_success)
