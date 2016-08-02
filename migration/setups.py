# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import os, subprocess, sys
from config import ENV_PATH
from ORM.ormpymysql import execute
import fnmatch


def run_install_modules():
    if sys.platform == 'win32':
        bin = 'Scripts'
    else:
        bin = 'bin'
    subprocess.call([os.path.join(ENV_PATH, bin, 'pip'), 'install', 'flask'])
    subprocess.call([os.path.join(ENV_PATH, bin, 'pip'), 'install', 'flask_login'])
    subprocess.call([os.path.join(ENV_PATH, bin, 'pip'), 'install', 'flask_pagedown'])
    subprocess.call([os.path.join(ENV_PATH, bin, 'pip'), 'install', 'flask-mail'])
    subprocess.call([os.path.join(ENV_PATH, bin, 'pip'), 'install', 'flask-wtf'])
    subprocess.call([os.path.join(ENV_PATH, bin, 'pip'), 'install', 'markdown'])
    subprocess.call([os.path.join(ENV_PATH, bin, 'pip'), 'install', 'pymysql'])
    subprocess.call([os.path.join(ENV_PATH, bin, 'pip'), 'install', 'Pillow'])

    # subprocess.call([os.path.join(ENV_PATH, bin, 'pip'), 'uninstall', 'flask'])
    # subprocess.call([os.path.join(ENV_PATH, bin, 'pip'), 'uninstall', 'flask_login'])
    # subprocess.call([os.path.join(ENV_PATH, bin, 'pip'), 'uninstall', 'flask-mail'])
    # subprocess.call([os.path.join(ENV_PATH, bin, 'pip'), 'uninstall', 'flask-wtf'])
    # subprocess.call([os.path.join(ENV_PATH, bin, 'pip'), 'uninstall', 'markdown'])
    # subprocess.call([os.path.join(ENV_PATH, bin, 'pip'), 'uninstall', 'pymysql'])
    # subprocess.call([os.path.join(ENV_PATH, bin, 'pip'), 'uninstall', 'Pillow'])


def get_files(path, filepat):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, filepat):
            yield os.path.join(dirpath, filename)


def get_openr(filenames):
    for filename in filenames:
        f = open(filename, 'r')
        yield f
        f.close()


def get_concatenate(files):
    for it in files:
        yield from it


def get_sqls(files):
    lists = list()
    for line in files:
        if line.strip() == "" and len(lists) > 0:
            yield ' '.join(lists)
        elif line.strip().endswith(';'):
            lists.append(line.strip()[0:-1])
            yield ' '.join(lists)
        elif line.strip().startswith('--'):
            continue
        else:
            lists.append(line.strip())


def create_tables(sqls):
    for sql in sqls:
        yield execute(sql)


def run_create_tables():
    filenames = get_files(os.path.dirname(__file__), '*.sql')
    files = get_openr(filenames)
    lines = get_concatenate(files)
    sqls = get_sqls(lines)
    values = create_tables(sqls)
    for value in values:
        print(value)



if __name__ == '__main__':
    # run_install_modules()
    run_create_tables()
