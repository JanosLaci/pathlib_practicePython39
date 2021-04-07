from subprocess import run, PIPE
from pathlib import Path

# 3 python file létrehozása, beleírás
for i in range(3):
    path = Path(fr"C:\Users\janos\PycharmProjects\pathlib_practicePython39\files_to_run\file_{i}.py")
    # path.write_text("#!/usr/bin/env python\n")
    path.write_text("import datetime;print(datetime.datetime.now())")


# raw használata, utolsó idézőjel escape elkerülése egy újabb \ beírásával, hogy a Windows path felismerhető legyen:

path_string = r'C:\Users\janos\PycharmProjects\pathlib_practicePython39\files_to_run\\'


# az összes Python file végrehajtása az adott könyvtárban, "python3" nem működik
# Python was not found; run without arguments to install from the Microsoft Store
# or disable this shortcut from Settings > Manage App Execution Aliases
#python -V
#Python 3.8.5

# generator létrehozása: Generator[Path, None, None]
for file in Path(path_string).glob("*.py"):
    # Gets the resolved full path
    full_path = str(file.resolve())
    print(type(file.resolve()))
    # <class 'pathlib.WindowsPath'>
    print(file.resolve())
    # C:\Users\janos\PycharmProjects\pathlib_practicePython39\files_to_run\file_1.py
    proc = run(["python", full_path], stdout=PIPE)
    print(proc)
# CompletedProcess(args=['python', 'C:\\Users\\janos\\PycharmProjects\\pathlib_practicePython39\\files_to_run\\file_0.py'], returncode=0, stdout=b'2021-04-07 12:18:00.019468\r\n')
# CompletedProcess(args=['python', 'C:\\Users\\janos\\PycharmProjects\\pathlib_practicePython39\\files_to_run\\file_2.py'], returncode=0, stdout=b'2021-04-07 12:18:00.941685\r\n')
# CompletedProcess(args=['python', 'C:\\Users\\janos\\PycharmProjects\\pathlib_practicePython39\\files_to_run\\file_1.py'], returncode=0, stdout=b'2021-04-07 12:18:00.474042\r\n')
