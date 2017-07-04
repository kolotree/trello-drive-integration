from unittest import TestCase
from integration.services.domain import Company
from integration.services.domain import Invoice


class CompanyTests(TestCase):
    def test_company_base_info_filled(self):
        company = Company('id', 'KoloTree')

        self.assertEquals(company.name, 'KoloTree')
        self.assertEquals(company.id, 'id')

    def test_two_invoices_added(self):
        company = self.makeDefaultInstance()
        company = company.add_invoices([Invoice(id = 'id1', name = 'name1'), Invoice(id = 'id2', name = 'name2')])

        self.assertEquals(len(company.invoices), 2)

    def makeDefaultInstance(self):
        return Company('KoloTree', 'folder_id')