import os

# lista létrehozása a path-str-k tárolására
matches = []

# utolsó könyvtárnév után nincs \

# dirpath, dirnames, filenames

for root, _, files in os.walk(r'C:\Users\janos\PycharmProjects\pathlib_practicePython39\txt_files'):
    for name in files:
        # Create the full path to the file by using os.path.join()
        fullpath = os.path.join(root, name)
        print(f"Processing file: {fullpath}")
        # Split off the extension and discard the rest of the path
        _, ext = os.path.splitext(fullpath)
        # Match the extension pattern .csv
        if ext == ".csv":
            matches.append(fullpath)

# Print the matches you find
print(matches)
