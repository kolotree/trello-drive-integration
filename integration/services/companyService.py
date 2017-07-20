from integration.gdrive.driveItem import ItemType
from integration.services.domain import Invoice


class InvoiceFolderDoesntExist(Exception):
    def __init__(self, folder_name, company):
        message = 'Invoice folder ' + folder_name + ' does not exist for company ' + str(company)
        super(InvoiceFolderDoesntExist, self).__init__(message)


input_invoice_folder_name = 'Ulazne fakture'
output_invoice_folder_name = 'Izlazne fakture'
invoice_folder_name = 'Korpa'


class AddTrelloCardResult:
    def __init__(self, is_success, company, input_invoices_count, output_invoices_count):
        self.is_success = is_success
        self.company = company
        self.input_invoices_count = input_invoices_count
        self.output_invoices_count = output_invoices_count


class CompanyService:
    def __init__(self, file_explorer, trello_card_writer):
        self.fileExplorer = file_explorer
        self.trello_card_writer = trello_card_writer

    def addTrelloCardFromCompanyDrive(self, company):
        input_invoices_folder = self.__get_input_invoice_folder_for(company)
        input_invoices = self.__get_invoices_from(input_invoices_folder)

        output_invoices_folder = self.__get_output_invoice_folder_for(company)
        output_invoices = self.__get_invoices_from(output_invoices_folder)

        are_invoices_added = self.trello_card_writer.add_invoices_for(company, len(input_invoices), len(output_invoices))
        return AddTrelloCardResult(are_invoices_added, company, len(input_invoices), len(output_invoices))

    def __get_input_invoice_folder_for(self, company):
        input_invoice_folder = self.__get_subfolder_for(company.id, input_invoice_folder_name, company.name)
        invoice_folder_id = self.__get_subfolder_for(input_invoice_folder.id, invoice_folder_name, company.name)
        return invoice_folder_id

    def __get_output_invoice_folder_for(self, company):
        output_invoice_folder = self.__get_subfolder_for(company.id, output_invoice_folder_name, company.name)
        output_folder_id = self.__get_subfolder_for(output_invoice_folder.id, invoice_folder_name, company.name)
        return output_folder_id

    def __get_subfolder_for(self, parentFolderId, subFolderName, companyName):
        driveItems = self.fileExplorer.get_items_using_folder_id(parentFolderId)
        subFolderList = [item for item in driveItems if
                                  (item.type == ItemType.FOLDER and item.name == subFolderName)]
        if len(subFolderList) != 1:
            raise InvoiceFolderDoesntExist(subFolderName, companyName)

        return subFolderList[0]

    def __get_invoices_from(self, invoiceFolder):
        driveItems = self.fileExplorer.get_items_using_folder_id(invoiceFolder.id)
        invoices = [item for item in driveItems if item.type == ItemType.FILE]
        return list(map(lambda drive_item: Invoice(drive_item.id, drive_item.name), invoices))