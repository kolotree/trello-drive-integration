from integration.gdrive.driveItem import ItemType
from integration.services.domain import Invoice


class InvoiceFolderDoesntExist(Exception):
    def __init__(self, folder_name, company):
        message = 'Invoice folder ' + folder_name + ' does not exist for company ' + str(company)
        super(InvoiceFolderDoesntExist, self).__init__(message)


invoice_folder_name = 'Korpa'


class AddTrelloCardResult:
    def __init__(self, is_success, company, invoice):
        self.is_success = is_success
        self.company = company
        self.invoice = invoice


class CompanyService:
    def __init__(self, file_explorer, trello_card_writer):
        self.fileExplorer = file_explorer
        self.trello_card_writer = trello_card_writer

    def addTrelloCardsFromCompanyDrive(self, company):
        invoiceFolder = self.__get_invoice_folder_for(company)
        invoices = self.__get_invoices_from(invoiceFolder)
        add_trello_card_results = self.__add_invoices_to_trello_for(company, invoices)
        return add_trello_card_results

    def __get_invoice_folder_for(self, company):
        driveItems = self.fileExplorer.get_items_using_folder_id(company.id)
        invoiceFolderList = [item for item in driveItems if
                             (item.type == ItemType.FOLDER and item.name == invoice_folder_name)]
        if len(invoiceFolderList) != 1:
            raise InvoiceFolderDoesntExist(invoice_folder_name, company)

        return invoiceFolderList[0]

    def __get_invoices_from(self, invoiceFolder):
        driveItems = self.fileExplorer.get_items_using_folder_id(invoiceFolder.id)
        invoices = [item for item in driveItems if item.type == ItemType.FILE]
        return list(map(lambda drive_item: Invoice(drive_item.id, drive_item.name), invoices))

    def __add_invoices_to_trello_for(self, company, invoices):
        add_trello_card_results = map(
            lambda invoice: AddTrelloCardResult(self.trello_card_writer.add_invoice_for(company, invoice), company, invoice),
            invoices)
        return list(add_trello_card_results)
