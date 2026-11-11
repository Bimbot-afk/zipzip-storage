from encoder import zip_zip as zz
import os
import pyttsx3

file = os.path.join("sample/pdf.pdf")

motor = pyttsx3.init()
motor.say("ziiip zip zip")
motor.runAndWait()

with open("sample/pdf.pdf", "rb") as file:
    data = file.read()

file_zip_name = os.path.splitext("sample/pdf.pdf")[0]


zz = zz(data)
ids = zz.zip_ids (data)
zipped_file = zz.zipper(ids)

with open("sample/pdf.zipzip", "wb") as file:
    data_to_zip = file.write(zipped_file.encode("utf-8"))