from integration.services.rootService import RootService
from tests.services.companyServiceTests import get_test_company_service_instance
from tests.gdrive.fileExplorerTests import get_test_file_explorer_instance
from unittest import TestCase


def get_test_root_service_instance():
    file_explorer = get_test_file_explorer_instance()
    company_service = get_test_company_service_instance()
    return RootService(file_explorer, company_service)

root_folder_id = '0B1gzQBsHQ8rvaVA1WmlEVm1obDQ'

class RootServiceTests(TestCase):
    def test_some_companies_processed(self):
        root_service = get_test_root_service_instance()
        results = root_service.visit_companies_and_add_invoices_for(root_folder_id)
        self.assertNotEquals(len(results), 0)