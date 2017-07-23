from enum import Enum

class AddCardStatus(Enum):
    SUCCESS = 1
    SKIPPED = 2
    BAD_FOLDER_STRUCTURE = 3
    ZERO_INVOICES = 4