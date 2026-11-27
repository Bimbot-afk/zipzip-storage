import os
import sys
import cmd
from pathlib import Path
from .decoder import unzip_zip as uz
from .encoder import zip_zip as zz
from .zip_listen import zip_listen as zl

def print_zipzipzip():
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
    print(f"Current Folder: {Path.cwd()}")

class zipzip(cmd.Cmd):
    prompt = ">>> "
    intro = "Welcome to zip zip. Type help or ? to list commands."
    current_files = {}
    selected_file = None
    print_zipzipzip()

    def do_zip(self, arg):
        """zZips the selected file"""
        print("You will zip zip a file")
        zip_file_path = self.selected_file
        if self.selected_file == None:
            print("Make sure to select a file")
        else:
            print_zipzipzip()
            zip_file(zip_file_path, arg)
        self.selected_file = None


    def do_unzip(self, arg):
        """Unzips the selected file"""
        print("You will unzip a zipzip file")
        if self.selected_file is not None and self.selected_file.suffix == ".zipzip":
            unzip_file_path = self.selected_file
            key = input("Enter the decryption key >>> ").strip()
            print_zipzipzip()
            un_zip(unzip_file_path, key, arg)
        else:
            print("Make sure to select a zipzip file")
        self.selected_file = None

    def do_ls(self, arg):
        """List the files of the current directory"""
        i = 0
        files = {}
        for item in os.listdir("."):
            i+=1
            files[str(i)] = Path(item).absolute()
            print(f"{i}_{item}")
        
        self.current_files = files

    def do_zap(self, arg):
        """Selects a file to zip or unzip"""
        files = self.current_files
        file_number = arg.strip()
        self.selected_file = files[file_number]
        print(f"File {self.selected_file} selected")

    def do_chezip(self, arg):
        """Shows whats the current selected file"""
        if self.selected_file == None:
            print("No file selected")
        else:
            print(f"Selected file: {self.selected_file}")

    def do_cleanzip(self, arg):
        """Clean the current selected file"""
        self.selected_file = None
        print("File selection cleared")

    def do_cd(self, folder):
        """Change directory"""
        try: 
            os.chdir(folder)
            print(f"Current Folder: {Path.cwd()}")
        except FileNotFoundError:
            print("Folder not found")


    def do_exitzip(self, arg):
        """Exits zipzap"""
        print("zipzap :c")
        exit()

def zip_file(path, arg):
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

    if arg.strip() == "-l":
        zl(zipped_file, file_name)

    with open(new_zip_path, "wb") as file:
        if isinstance(zipped_file, str):
            file.write(zipped_file.encode("utf-8"))
        else:
            file.write(zipped_file)

    total_zip, total_zap = encoder_instance.total_zipzap()

    print(f"File successfully compressed to: {new_zip_path}")
    print(f"🔑 Decryption key (save this to unzip!): {encoder_instance.key}")
    print(f"Total zip: {total_zip}")
    print(f"Total zap: {total_zap}")
    print(f"Total characters: {len(zipped_file)}")

    if arg.strip() != "-r":
        try:
            os.remove(path_zip)
        except FileNotFoundError:
            print("File already deleted ")


def un_zip(path, key, arg):

    zipped_path = Path(path)

    with open(zipped_path, "r", encoding="utf-8") as unzip:
        zipped_content = unzip.read()

    dec = uz(key)
    try:
        recover_bytes, ext = dec.un_zipzip(zipped_content)
    except ValueError as e:
        print(e)
        return
    
    recovered_path = zipped_path.with_suffix(ext)

    with open(recovered_path, "wb") as file:
        file.write(recover_bytes)

    print(f"File successfully recovered to: {recovered_path}")

    if arg.strip() != "-r":
        try:
            os.remove(zipped_path)
        except FileNotFoundError:
            print("File already deleted")

def main():
    zipzip().cmdloop()

if __name__ == "__main__":
    main()
