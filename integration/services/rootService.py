from integration.gdrive.driveItem import ItemType
from integration.services.domain import Company
import itertools


class RootService:
    def __init__(self, file_explorer, company_service):
        self.file_explorer = file_explorer
        self.company_service = company_service

    def visit_companies_and_add_invoices_for(self, folder_id):
        companies = self.__get_companies_for(folder_id)
        results = self.__add_trello_cards_from_company_drives(companies)
        return results

    def __get_companies_for(self, folder_id):
        driveItems = self.file_explorer.get_items_using_folder_id(folder_id)
        company_drive_items = [item for item in driveItems if item.type == ItemType.FOLDER]
        companies = map(lambda folder_item: Company(folder_item.id, folder_item.name), company_drive_items)
        return list(companies)

    def __add_trello_cards_from_company_drives(self, companies):
        results = map(lambda company: self.company_service.addTrelloCardsFromCompanyDrive(company), companies)
        flat_results = list(itertools.chain(results))
        return flat_results