class unzip_zip:
    def __init__(self, file_to_zip: dict = None):

            if self.zip_to_zip is not None:
                self.zip_to_file = {idx: byte_val for byte_val, idx in file_to_zip.items()}
            else:
                self.zip_to_file = None

    def un_zipzip(self, zipped_text: str) -> bytes:

        clean_text = zipped_text.replace("\n," "").replace("\r", "")
        blocks = [b for b in clean_text.split("|") if b]
        ids = [(len(block) // 3) - 1 for block in blocks]

        if self.zip_to_file is not None:
            return bytes(self.ziip_to_file[i] for i in ids)
        return bytes(ids)