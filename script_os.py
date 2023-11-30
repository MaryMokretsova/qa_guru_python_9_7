import os.path

current_file = os.path.abspath(__file__)

CURRENT_DIR = os.path.dirname(current_file)
print(CURRENT_DIR)


TMP_DIR = os.path.join(CURRENT_DIR, "tmp")
print(TMP_DIR)

