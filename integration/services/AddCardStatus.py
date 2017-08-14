from enum import Enum

class AddCardStatus(Enum):
    SUCCESS = 1
    SKIPPED = 2
    ZERO_INVOICES = 3