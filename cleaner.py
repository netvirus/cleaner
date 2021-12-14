# Cleaner v 1.0
# Author netvirus
# https://github.com/yaroslav-tsuprak

import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("cleaner.log"),
        logging.StreamHandler()
    ]
)

# Default True but you can disable it write False
log_enabled = True
path_to_look_for = "c:\\Users\\Administrator\\AppData\\Roaming\\MetaQuotes\\Terminal"
file_extension = ".tkc"

files_list = {}

f = open('files.txt', 'r')
content_list = f.readlines()

for root, dirs, files in os.walk(path_to_look_for):
    for file in files:
        if file.endswith(file_extension):
            files_list[file] = os.path.join(root, file)
            if log_enabled:
                logging.info("Found " + len(files_list) + " files")

if len(files_list) != 0:
    for c in content_list:
        file_name = c.rstrip('\n')
        if files_list.get(file_name) is not None:
            file_name_with_full_path = files_list.get(file_name)
            try:
                os.remove(file_name_with_full_path)
                if log_enabled:
                    logging.info("Remove file: " + file_name_with_full_path)
            except:
                if log_enabled:
                    logging.info("Error while deleting file " + file_name_with_full_path)
else:
    if log_enabled:
        logging.info("There is nothing to remove!")
