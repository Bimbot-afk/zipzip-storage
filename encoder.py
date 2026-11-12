import re
import random

class zip_zip:
    def __init__(self, data: bytes):
        unique_bytes = range(256)
        self.file_to_zip = {byte_val: idx for idx, byte_val in enumerate(unique_bytes)}
        

    def zip_ids(self, data:bytes):
        return [self.file_to_zip[b] for b in data]



    def zipper(self, ids):
        file_zipped = [] 
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
                else:
                    file_zipped.append("zap")

                if line_zips == 67:
                    file_zipped.append("\n")
                    line_zips = 0
                zip += 1
                line_zips += 1

            file_zipped.append("zip|")
            line_zips += 1

        return "".join(file_zipped)

