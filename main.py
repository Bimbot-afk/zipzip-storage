import os
from pathlib import Path
from decoder import unzip_zip as uz
from encoder import zip_zip as zz
from zip_listen import zip_listen as zl

def main():
    print("""

               .dMMMMMMMMMMMMMMMMMMMMMMb.
            .dMMMMMMMMMMMMMMMMMMMMMMMMMMMMb.
          .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.
         dMMMMMMMP'        ``YMMMMMMM       `YMMb
        dMMMMMMM'             `MMMMMM'         `MMb
       dMMMMMMM'               `MMMM'           `MMb
       MMMMMMMM                 MMMM             MMM
       MMMMMMMM                 MMMM             MMM
       MMMMMMMMb               dMMMM            dMM'
       YMMMMMMMMb             dMMMMMb          dMM'
        YMMMMMMMMMb.       .dMMMMMMMMMb.      dMMP
         `YMMMMMMMMMMMbbMMMMMMMMMMMMMMMMMbb.dMMP'
           `YMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMP'
             `YMMMMMMMMMMMMMMMMMMMMMMMMMMMMP'
                `TMMMMMMMMMMMMMMMMMMMMMMMP'
                   `TMMMMMMMMMMMMMMMMP'

                        |MMMMMMM|
                        |MMMMMMM|
                        |MMMMMMM|
                       dMMMMMMMMMb
                     .MMMMMMMMMMMMM.
                   .MMMMMMMMMMMMMMMMM.
    """)
    print("Welcome to zip zip")
    print("---------------------------------")
    print("""
    1. zip zip a file
    2. Un zip zip a file
    3. Exit
    """)

    options = {"1", "2", "3"}
    option = input("pick the number >>> ").strip()
    error = None

    if option in options:
        if option == "1":
            zip_file_path = input("Enter the absolute path to the route >>> ").strip("\"' ")
            if Path(zip_file_path).is_absolute():
                zip_file(zip_file_path)
            else:
                print("Make sure you enter an absolute path")

        elif option == "2":
            unzip_file_path = input("Enter the absolute path to the route >>> ").strip("\"' ")
            if Path(unzip_file_path).is_absolute():
                error = None
            else:
                error = True

            if error is None:
                key = input("Enter the decryption key >>> ").strip()
                un_zip(unzip_file_path, key)
            else:
                print("Make sure you enter an absolute path")

        elif option == "3":
            exit()
    else:
        print("Invalid option. Please pick 1, 2, or 3.")


def zip_file(path):
    path_zip = Path(path)
    with open(path_zip, "rb") as file:
        data = file.read()

    encoder_instance = zz(data)
    ids = encoder_instance.zip_ids(data)
    file_type = path_zip.suffix
    file_type = file_type.lower()
    zipped_file = encoder_instance.zipper(ids, file_type)

    file_name = path_zip.name

    new_zip_path = path_zip.with_suffix(".zipzip")

    zl(zipped_file, file_name)

    with open(new_zip_path, "wb") as file:
        if isinstance(zipped_file, str):
            file.write(zipped_file.encode("utf-8"))
        else:
            file.write(zipped_file)

    print(f"File successfully compressed to: {new_zip_path}")
    print(f"🔑 Decryption key (save this to unzip!): {encoder_instance.key}")

    try:
        os.remove(path_zip)
    except FileNotFoundError:
        print("File already deleted")


def un_zip(path, key):

    zipped_path = Path(path)

    with open(zipped_path, "r", encoding="utf-8") as unzip:
        zipped_content = unzip.read()

    dec = uz(key)
    recover_bytes, ext = dec.un_zipzip(zipped_content)

    recovered_path = zipped_path.with_suffix(ext)

    with open(recovered_path, "wb") as file:
        file.write(recover_bytes)

    print(f"File successfully recovered to: {recovered_path}")

    try:
        os.remove(zipped_path)
    except FileNotFoundError:
        print("File already deleted")


if __name__ == "__main__":
    main()
