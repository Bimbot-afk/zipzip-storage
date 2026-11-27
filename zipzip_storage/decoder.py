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

        file_type_zip = zipped_text.split("|")[0]

        clean_text = zipped_text.replace("\n", "").replace("\r", "")

        blocks = [b for b in clean_text.split("|") if b]

        if len(file_type_zip) == 5:
            file_type_ext = self.wich_file_type(blocks.pop(0))
                
        ids = [(len(block) // 3) - 1 for block in blocks]

        if self.zip_to_file is not None:
            recovered = bytes(self.zip_to_file[i] for i in ids)
            if not recovered.startswith(b"zipzapzip"):
                raise ValueError("Invalid zip key")
            return recovered[9:], file_type_ext

        return bytes(ids), file_type_ext

    def wich_file_type(self, file_type):
        zip_file_type_d = {
            "zpziz": ".txt",
            "zppaz": ".pdf",
            "zizzp": ".docx",
            "zzzpp": ".xlsx",
            "zzpaz": ".pptx",
            "zapiz": ".jpg",
            "zaizz": ".png",
            "zapap": ".mp3",
            "zpaip": ".mp4",
            "zaipa": ".zip",
            "zpzzi": ".html",
            "zzzzi": ".css",
            "zpiiz": ".js",
            "ziapp": ".py",
            "zzpzi": ".json",
        }
        try:
            return zip_file_type_d[file_type]
        except KeyError:
            return ".txt"