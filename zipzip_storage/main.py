import os
import sys
import cmd
from pathlib import Path
from .decoder import unzip_zip as uz
from .encoder import zip_zip as zz
from .zip_listen import zip_listen as zl
from .cutezip import print_zipzipzip, colors

class zipzip(cmd.Cmd):
    prompt = f"{colors('GREEN')}>>> {colors('RESET')}"
    intro = f"{colors('GREEN')}Welcome to zip zip. Type help or ? to list commands.{colors('RESET')}"
    current_files = {}
    selected_file = None
    print_zipzipzip(str(Path.cwd()))

    def do_zip(self, arg):
        """zZips the selected file"""
        print(colors("CYAN") + "You will zip zip a file" + colors("RESET"))
        zip_file_path = self.selected_file
        if self.selected_file == None:
            print(colors("RED") + "Make sure to select a file" + colors("RESET"))
        else:
            print_zipzipzip(str(Path.cwd()))
            zip_file(zip_file_path, arg)
        self.selected_file = None


    def do_unzip(self, arg):
        """Unzips the selected file"""
        print(colors("CYAN") + "You will unzip a zipzip file" + colors("RESET"))
        if self.selected_file is not None and self.selected_file.suffix == ".zipzip":
            unzip_file_path = self.selected_file
            key = input("Enter the decryption key >>> ").strip()
            print_zipzipzip(str(Path.cwd()))
            un_zip(unzip_file_path, key, arg)
        else:
            print(colors("RED") + "Make sure to select a zipzip file" + colors("RESET"))
        self.selected_file = None

    def do_ls(self, arg):
        """List the files of the current directory"""
        i = 0
        files = {}
        for item in os.listdir("."):
            i+=1
            files[str(i)] = Path(item).absolute()
            print(f"{colors('YELLOW')}# {i} {colors('RESET')}{item}")
        
        self.current_files = files

    def do_zap(self, arg):
        """Selects a file to zip or unzip"""
        files = self.current_files
        if not files:
            print(f"{colors('RED')}'check with 'ls' first ;){colors('RESET')}")
            return
        total_files = len(files)
        file_index = int(arg.strip()) - 1

        if file_index < 0 or file_index >= total_files:
            print(f"{colors('RED')}'{arg}' is not a valid file number{colors('RESET')}")
            return 
        
        self.selected_file = files[str(file_index)]
        print(f"{colors('CYAN')}File {self.selected_file} selected{colors('RESET')}")

    def do_chezip(self, arg):
        """Shows whats the current selected file"""
        if self.selected_file == None:
            print(colors("RED") + "No file selected" + colors("RESET"))
        else:
            print(f"{colors('CYAN')}File {self.selected_file} selected{colors('RESET')}")

    def do_cleanzip(self, arg):
        """Clean the current selected file"""
        self.selected_file = None
        print(f"{colors('CYAN')}File selection cleared{colors('RESET')}")

    def do_cd(self, folder):
        """Change directory"""
        try: 
            os.chdir(folder)
            print(f"{colors('CYAN')}Current Folder: {Path.cwd()}{colors('RESET')}")
        except FileNotFoundError:
            print(f"{colors('RED')}Folder not found{colors('RESET')}")


    def do_exitzip(self, arg):
        """Exits zipzip"""
        print(f"{colors('CYAN')}zipzap :c{colors('RESET')}")
        exit()

def zip_file(path, arg):
    path_zip = Path(path)
    args_list = arg.split()

    with open(path_zip, "rb") as file:
        data = file.read()

    encoder_instance = zz(data)
    ids = encoder_instance.zip_ids(data)
    file_type = path_zip.suffix
    file_type = file_type.lower()
    zipped_file = encoder_instance.zipper(ids, file_type)

    file_name = path_zip.name

    new_zip_path = path_zip.with_suffix(".zipzip")

    if  "-l" in args_list:
        zl(zipped_file, file_name)

    with open(new_zip_path, "wb") as file:
        if isinstance(zipped_file, str):
            file.write(zipped_file.encode("utf-8"))
        else:
            file.write(zipped_file)

    total_zip, total_zap = encoder_instance.total_zipzap()

    print(f"{colors('CYAN')}File successfully compressed to: {new_zip_path}{colors('RESET')}")
    print(f"{colors('CYAN')}🔑 Decryption key (save this to unzip!): {encoder_instance.key}{colors('RESET')}")
    print(f"{colors('CYAN')}Total zip: {total_zip}{colors('RESET')}")
    print(f"{colors('CYAN')}Total zap: {total_zap}{colors('RESET')}")
    print(f"{colors('CYAN')}Total characters: {len(zipped_file)}{colors('RESET')}")

    if "-r" not in args_list:
        try:
            os.remove(path_zip)
        except FileNotFoundError:
            print(f"{colors('RED')}'{zipped_path}' already deleted{colors('RESET')}")


def un_zip(path, key, arg):

    arg_list = arg.split()

    zipped_path = Path(path)

    with open(zipped_path, "r", encoding="utf-8") as unzip:
        zipped_content = unzip.read()

    dec = uz(key)
    try:
        recover_bytes, ext = dec.un_zipzip(zipped_content)
    except ValueError as e:
        print(f"{colors('RED')}{e}{colors('RESET')}")
        return
    
    recovered_path = zipped_path.with_suffix(ext)

    with open(recovered_path, "wb") as file:
        file.write(recover_bytes)

    print(f"{colors('CYAN')}File successfully recovered to: {recovered_path}{colors('RESET')}")

    if "-r" not in arg_list:
        try:
            os.remove(zipped_path)
        except FileNotFoundError:
            print(f"{colors('RED')}'{zipped_path}' already deleted{colors('RESET')}")

def main():
    zipzip().cmdloop()

if __name__ == "__main__":
    main()
