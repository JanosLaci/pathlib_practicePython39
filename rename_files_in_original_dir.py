# create_files_to_rename futtatása először

import pathlib
import os
from pathlib import Path
from typing import Any, Union

# os_get_current_working_directory = os.getcwd()
# print(os_get_current_working_directory)
# print(type(os_get_current_working_directory))

# os.walk yielding 3-tuples:
# dirpath (root)
# dirnames
# filenames (list of non-directory files' names)
for root, _, filenames in os.walk(r'C:\Users\janos\PycharmProjects\pathlib_practicePython39\files_to_rename\\'):
    for filename_to_rename in filenames:

        # Create the full path to the file by using os.path.join()
        full_path: str = os.path.join(root, filename_to_rename)
        print(f"Processing file: {full_path}")

        # Rename file
        if "rename" in filename_to_rename:
            path: Union[Path, Any] = pathlib.Path(full_path)
            index_of_filename: str = filename_to_rename.split("rename")[1]  # az indexet a filenév "rename" utáni része tartalmazza
            # fr"\files_to_rename\txt_file_renamed{index_of_filename}.txt" nem működik (\ kezdet)
            # a név része a working dir utáni dir is
            # fr egymás után (\ escape kerülése)
            new_name = fr"files_to_rename\txt_file_renamed{index_of_filename}.txt"
            print(f"Renaming file {filename_to_rename} to {new_name}")
            path.rename(new_name)