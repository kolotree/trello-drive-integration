class Invoice:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Company:
    def __init__(self, id, name, invoices=[]):
        self.id = id
        self.name = name
        self.invoices = invoices

    def add_invoices(self, invoiceList):
        invoices = list(self.invoices)
        invoices.extend(invoiceList)
        return Company(self.id, self.name, invoices)