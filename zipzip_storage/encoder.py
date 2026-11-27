import re
import random
import secrets

class zip_zip:
    def __init__(self, data: bytes, key: str = None):
        self.key = key if key is not None else secrets.token_hex(3).upper()
        unique_bytes = list(range(256))
        random.Random(self.key).shuffle(unique_bytes)
        self.file_to_zip = {byte_val: idx for idx, byte_val in enumerate(unique_bytes)}
        self.firmkey = "zipzapzip"
        self.total_zip = 0
        self.total_zap = 0
        

    def zip_ids(self, data:bytes):
        data_w_firm = self.firmkey.encode("utf-8") + data
        return [self.file_to_zip[b] for b in data_w_firm]

    def zip_file_type(self, file_type):
        #only combinations of z-i-p-a max 5 letters
            zip_file_type_d = {
            ".txt": "zpziz",
            ".pdf": "zppaz",
            ".docx": "zizzp",
            ".xlsx": "zzzpp",
            ".pptx": "zzpaz",
            ".jpg": "zapiz",
            ".png": "zaizz",
            ".mp3": "zapap",
            ".mp4": "zpaip",
            ".zip": "zaipa",
            ".html": "zpzzi",
            ".css": "zzzzi",
            ".js": "zpiiz",
            ".py": "ziapp",
            ".json": "zzpzi"
            }

            if file_type not in zip_file_type_d:
                return "zpziz"
            else:
                return zip_file_type_d[file_type]

    def zipper(self, ids, file_type: str):
        zip_file_type = self.zip_file_type(file_type)
        file_zipped = [f"{zip_file_type}|"]
        total_zip_bar = "" 
        progress = 0
        zip_bar = "===="
        total_zip = len(ids)
        line_zips = 0

        checks = [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0]
        check_points = [round(total_zip * p) for p in checks]


        for pos, id in enumerate(ids, start=1):
            id = id
            zip = 0

            if pos in check_points:
                total_zip_bar += zip_bar 
                progress += 12.5
                print(f"{progress}% {total_zip_bar}" )
                if pos == total_zip:
                    print("ZIP ZIP COMPLETE :D")

            while zip != id:
                if random.randint(1, 5)  != random.randint(1, 5):
                    file_zipped.append("zip")
                    self.total_zip += 1
                else:
                    file_zipped.append("zap")
                    self.total_zap += 1

                if line_zips == 67:
                    file_zipped.append("\n")
                    line_zips = 0
                zip += 1
                line_zips += 1

            file_zipped.append("zip|")
            self.total_zip += 1
            line_zips += 1

        return "".join(file_zipped)

    def return_file_to_zip(self):
        return self.file_to_zip

    def total_zipzap(self):
        return self.total_zip, self.total_zap