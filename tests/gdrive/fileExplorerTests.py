from unittest import TestCase
from integration.gdrive.serviceProvider import ServiceProvider
from integration.gdrive.fileExplorer import FileExplorer
import json

# In order for test to pass you have to fill valid client ID, secret and folder ID in test.json file
test_config = json.load(open("tests/gdrive/test.json"))
client_id = test_config["client_id"]
client_secret = test_config["client_secret"]
folder_id = test_config["folder_id"]

service = ServiceProvider(client_id, client_secret).getDriveServiceInstance()

def get_test_file_explorer_instance():
    return FileExplorer(service)


class FileExplorerTests(TestCase):
    def test_get_items_using_folder_id(self):
        file_explorer = FileExplorer(service)
        drive_items = file_explorer.get_items_using_folder_id(folder_id)
        self.assertNotEquals(len(drive_items), 0)

    def test_drive_item_is_correctly_filled(self):
        file_explorer = FileExplorer(service)
        drive_items = file_explorer.get_items_using_folder_id(folder_id)

        first_item = drive_items[0]
        self.assertIsNotNone(first_item.id)
        self.assertIsNotNone(first_item.name)
        self.assertIsNotNone(first_item.type)