from pathlib import Path

# 3 txt file létrehozása a files_to_rename könyvtárban
for i in range(3):
    path = Path(fr"C:\Users\janos\PycharmProjects\pathlib_practicePython39\files_to_rename\txt_file_to_rename{i}.txt")
    # path.write_text("#!/usr/bin/env python\n")
    path.write_text("import datetime;print(datetime.datetime.now())")