# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import os, subprocess, sys

def run():
    if sys.platform == 'win32':
        bin = 'Scripts'
    else:
        bin = 'bin'
    subprocess.call([os.path.join('E:\PythonTest\env', bin, 'pip'), 'install', 'flask'])
    subprocess.call([os.path.join('E:\PythonTest\env', bin, 'pip'), 'install', 'flask_login'])
    subprocess.call([os.path.join('E:\PythonTest\env', bin, 'pip'), 'install', 'flask-mail'])
    subprocess.call([os.path.join('E:\PythonTest\env', bin, 'pip'), 'install', 'flask-wtf'])
    subprocess.call([os.path.join('E:\PythonTest\env', bin, 'pip'), 'install', 'markdown'])
    subprocess.call([os.path.join('E:\PythonTest\env', bin, 'pip'), 'install', 'pymysql'])
    subprocess.call([os.path.join('E:\PythonTest\env', bin, 'pip'), 'install', 'Pillow'])

if __name__ == '__main__':
    run()
