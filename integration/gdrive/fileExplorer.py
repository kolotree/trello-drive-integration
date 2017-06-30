from .driveItem import DriveItem


class FileExplorer:
    def __init__(self, service):
        self.service = service

    def get_items_using_folder_id(self, folder_id):
        page_token = None
        result_items = []
        while True:
            param = {'q': "'" + folder_id + "'" + ' in parents'}
            if page_token:
                param['pageToken'] = page_token

            folder_items = self.service.files().list(**param).execute()

            result_items.extend(map(DriveItem, folder_items['files']))
            page_token = folder_items.get('nextPageToken')
            if not page_token:
                break

        return result_items
