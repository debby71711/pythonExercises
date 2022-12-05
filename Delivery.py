import pathlib

path=pathlib.path
file_path = pathlib.Path.home()/"my_folder"
file_path.mkdir(exist_ok=True)
new_file_path=file_path/"my file.txt"
new_file_path.touch()
print("does fle path exist")