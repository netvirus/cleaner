# Cleaner v 2.0
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

with open('files.txt') as f:
    content_list = f.read().splitlines()

for root, dirs, files in os.walk(path_to_look_for):
    files_list_txt = list(filter(lambda x: x.endswith(file_extension), files))
    files_list.update(dict(zip(map(lambda x: os.path.join(root, x), files_list_txt), files_list_txt,)))
    if log_enabled:
        logging.info("Found " + str(len(files_list)) + " files")

if len(files_list) != 0:
    for keys, values in files_list.items():
        if values in content_list:
            os.remove(keys)
            if log_enabled:
                logging.info("Remove file: " + keys)
else:
    if log_enabled:
        logging.info("There is nothing to remove!")
