import random

class unzip_zip:
    def __init__(self, key_or_dict=None):
        if isinstance(key_or_dict, dict):
            self.zip_to_file = {idx: byte_val for byte_val, idx in key_or_dict.items()}
        elif isinstance(key_or_dict, str):
            unique_bytes = list(range(256))
            random.Random(key_or_dict).shuffle(unique_bytes)
            self.zip_to_file = {idx: byte_val for idx, byte_val in enumerate(unique_bytes)}
        else:
            self.zip_to_file = None

    def un_zipzip(self, zipped_text) -> bytes:
        if isinstance(zipped_text, bytes):
            zipped_text = zipped_text.decode("utf-8")

        clean_text = zipped_text.replace("\n", "").replace("\r", "")
        blocks = [b for b in clean_text.split("|") if b]
        ids = [(len(block) // 3) - 1 for block in blocks]

        if self.zip_to_file is not None:
            return bytes(self.zip_to_file[i] for i in ids)
        return bytes(ids)