import os
from pathlib import Path
from decoder import unzip_zip as uz
from encoder import zip_zip as zz


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
                uz(unzip_file_path)
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
    zipped_file = encoder_instance.zipper(ids)

    new_zip_path = path_zip.with_suffix(".zipzip")

    with open(new_zip_path, "wb") as file:
        if isinstance(zipped_file, str):
            file.write(zipped_file.encode("utf-8"))
        else:
            file.write(zipped_file)

    print(f"File successfully compressed to: {new_zip_path}")


if __name__ == "__main__":
    main()
