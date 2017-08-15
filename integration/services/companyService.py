from integration.gdrive.driveItem import ItemType
from integration.services.domain import Invoice
from integration.myLogging.loggerFactory import LoggerFactory
from integration.services.AddCardStatus import AddCardStatus
from integration.configuration.configuration import Configuration


class InvoiceFolderDoesntExist(Exception):
    def __init__(self, parent_folder_name, folder_name, company):
        message = "Invoice folder '{0}/{1}' does not exist for company '{2}'".format(parent_folder_name, folder_name, str(company))
        super(InvoiceFolderDoesntExist, self).__init__(message)


class InvoiceGroup:
    def __init__(self, name, invoice_count):
        self.name = name
        self.invoice_count = invoice_count

    def __str__(self):
        name_abbreviation = ''.join([i[0].upper() for i in self.name.split()])
        return '%s: %s' % (name_abbreviation, self.invoice_count)


class InvoiceGroups:
    def __init__(self, invoice_group_list):
        self.invoice_group_list = invoice_group_list

    def __str__(self):
        return ' | '.join(map(lambda ig: str(ig), self.invoice_group_list))

    def __len__(self):
        return len(self.invoice_group_list)


class AddTrelloCardResult:
    def __init__(self, added_card_status, company, invoice_groups):
        self.added_card_status = added_card_status
        self.company = company
        self.invoice_groups = invoice_groups


class CompanyService:
    def __init__(self, file_explorer, trello_card_writer):
        self.fileExplorer = file_explorer
        self.trello_card_writer = trello_card_writer

    def addTrelloCardFromCompanyDrive(self, company):
        invoice_group_names = Configuration().get_gdrive_invoice_groups()

        invoice_group_list = []
        for invoice_group_name in invoice_group_names:
            try:
                invoice_folder = self.__get_invoice_folder_for(company, invoice_group_name)
                invoices = self.__get_invoices_from(invoice_folder)
                if (len(invoices) > 0):
                    invoice_group_list.append(InvoiceGroup(invoice_group_name, len(invoices)))
            except InvoiceFolderDoesntExist as err:
                LoggerFactory().getLoggerInstance().log_exception(err)
                # Just continue with the next invoice group

        invoice_groups = InvoiceGroups(invoice_group_list)
        if (len(invoice_groups) == 0):
            return AddTrelloCardResult(AddCardStatus.ZERO_INVOICES, company, invoice_groups)

        are_invoices_added = self.trello_card_writer.add_invoices_for(company, invoice_groups)
        return AddTrelloCardResult(AddCardStatus.SUCCESS if are_invoices_added else AddCardStatus.SKIPPED, company,
                                   invoice_groups)

    def __get_invoice_folder_for(self, company, invoice_group_name):
        invoice_group_folder = self.__get_subfolder_for(company, invoice_group_name, company.name)
        invoice_folder_id = self.__get_subfolder_for(invoice_group_folder, 'Korpa', company.name)
        return invoice_folder_id

    def __get_subfolder_for(self, parent_folder, sub_folder_name, company_name):
        driveItems = self.fileExplorer.get_items_using_folder_id(parent_folder.id)
        subFolderList = [item for item in driveItems if
                         (item.type == ItemType.FOLDER and item.name == sub_folder_name)]
        if len(subFolderList) != 1:
            raise InvoiceFolderDoesntExist(parent_folder.name, sub_folder_name, company_name)

        return subFolderList[0]

    def __get_invoices_from(self, invoiceFolder):
        driveItems = self.fileExplorer.get_items_using_folder_id(invoiceFolder.id)
        invoices = [item for item in driveItems if item.type == ItemType.FILE]
        return list(map(lambda drive_item: Invoice(drive_item.id, drive_item.name), invoices))
