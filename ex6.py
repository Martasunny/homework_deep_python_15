import os.path
from os import listdir
import argparse
import logging
from collections import namedtuple

logging.basicConfig(filename='log6.log', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)

file = namedtuple(typename='file', field_names='file_path, ext, folder, parent_folder')

def directory_info(file_p: str):
    files_list = listdir(file_p)
    p = file_p.split(os.path.pathsep)
    for item in files_list:
        if os.path.isfile(item):
            temp = item.split('.')
            obj = file(temp[0], temp[1], p[-1], f'\\'.join(p[:-1]))
        else:
            obj = file(item, '', p[-1], f'{os.path.pathsep}'.join(p[:-1]))
        logger.info(obj)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, help='путь до папки')
    args = parser.parse_args()
    directory_info(args.path)
