from enum import Enum


class ItemType(Enum):
    FILE = 1
    FOLDER = 2


class DriveItem:
    def __init__(self, google_drive_item):
        self.id = google_drive_item['id']
        self.name = google_drive_item['name']
        self.type = DriveItem.resolve_item_type(google_drive_item['mimeType'])

    @staticmethod
    def resolve_item_type(google_drive_item_type):
        if google_drive_item_type == 'application/vnd.google-apps.folder':
            return ItemType.FOLDER
        else:
            return ItemType.FILE

    def __str__(self):
        return '%s - %s' % (self.type, self.name)
