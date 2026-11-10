import re

class zip_zip:
    def __init__(self, data: bytes):
        unique_bytes = sorted(set(data))
        self.file_to_zip = {byte_val: idx for idx, byte_val in enumerate(unique_bytes)}
        

    def zip_ids(self, data:bytes):
        return [self.file_to_zip[b] for b in data]



    def zipper(self, ids):
        file_zipped = ""

        for id in ids:
            id = id
            zip = 0
            zipped = ""
            while zip != id:
                file_zipped += "zip"
                zip += 1
            file_zipped += "zip|"

        return file_zipped

