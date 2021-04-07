import mypy
from typing import NewType


import pathlib


# file listát tartalmazó txt beolvasása, open létrehozza a rows_from_txt TextIOWrapper objektumot:
with open(r"C:\Users\janos\PycharmProjects\pathlib_practicePython39\txt_files\file_lista.txt") as rows_from_txt:
    #TextIOWrapper-ből lista létrehozása a .readlines() metódussal, lista bejárása:
    for txt_row in rows_from_txt.readlines():


        # pathlib objektum létrehozása beolvasott str-ből: .strip() metódus a tab-ot és a szóközt is levágja
        path = pathlib.Path(txt_row.strip())


        # Check if the file exists on disk
        if path.exists():
            print(f"Megtalált txt file: \n{txt_row.strip()}")
        else:
            print(f"Hiányzó txt file: \n{txt_row.strip()}")

with open(r"C:\Users\janos\PycharmProjects\pathlib_practicePython39\txt_files\file_lista.txt") as all_rows_from_txt:
    print(type(all_rows_from_txt))
    #<class '_io.TextIOWrapper'>
    print(all_rows_from_txt)
    #<_io.TextIOWrapper name='C:\\Users\\janos\\PycharmProjects\\pathlib_practicePython39\\txt_files\\file_lista.txt' mode='r' encoding='cp1252'>
    print(all_rows_from_txt.name)
    #'C:\\Users\\janos\\PycharmProjects\\pathlib_practicePython39\\txt_files\\file_lista.txt'
    print(all_rows_from_txt.readlines())
    print("A readlines metódus által létrehozott objektum típusa list:")
    print(type(all_rows_from_txt.readlines()))