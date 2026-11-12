from encoder import zip_zip as zz
from decoder import unzip_zip as uz

import os

file = os.path.join("sample/pdf.pdf")


with open("sample/pdf.pdf", "rb") as file:
    data = file.read()

file_zip_name = os.path.splitext("sample/pdf.pdf")[0]


zz = zz(data)
ids = zz.zip_ids (data)
zipped_file = zz.zipper(ids)

with open("sample/pdf.zipzip", "wb") as file:
    data_to_zip = file.write(zipped_file.encode("utf-8"))

with open("sample/pdf.zipzip", "r") as file:
    zipped_file = file.read()

dec = uz(zz.file_to_zip)
recover_bytes = dec.un_zipzip(zipped_file)

with open("sample/pdf_unziped.pdf", "wb") as file:
    file.write(recover_bytes)