#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : build.py
# @Author: Wade Cheung， EditBy BH liu
# @Date  : 2019/2/23
# @Desc  : Use Cython.Build.cythonize take py Compile into.so file


import sys
import os
import shutil
from distutils.core import setup
from Cython.Build import cythonize

currdir = os.path.abspath('.')
parentpath = sys.argv[1] if len(sys.argv) > 1 else ""
setupfile = os.path.join(os.path.abspath('.'), __file__)
build_dir = "build"
build_tmp_dir = build_dir + "/temp"

filter_dir_set = {'dist', 'build', 'data', 'test', 'orm\\data'}

except_files = {
    __file__,
    'build.py','main.py',
    'frozen_dir.py',
    'libs\\time_it.py',
}


def filter_file(file_name):
    if file_name.__contains__(currdir):
        file_name = file_name.replace(currdir, '')
    if file_name in except_files:  # Filter file
        return True
    file_path = file_name.split("\\")
    if len(file_path) > 1:
        file_dir = ""
        for i in range(len(file_path)-1):
            file_dir = os.path.join(file_dir, file_path[i])
            if file_dir in filter_dir_set:
                return True
    return file_path[0] in filter_dir_set


def getpy(basepath=os.path.abspath('.'), parentpath='', name='',
          copyOther=False, delC=False):
    """
    //Get path to py file
    :param basepath: Root path
    :param parentpath: Parent path
    :param name: file/Clip
    :param copy: Whether copy Other documents
    :return: py Iterator of files
    """
    fullpath = os.path.join(basepath, parentpath, name)
    for fname in os.listdir(fullpath):
        ffile = os.path.join(fullpath, fname)
        if os.path.isdir(ffile) and fname != build_dir and not fname.startswith('.'):
            for f in getpy(basepath, os.path.join(parentpath, name), fname,
                          copyOther, delC):
                yield f
        elif os.path.isfile(ffile):
            ext = os.path.splitext(fname)[1]
            # delete.c Temporary file
            if ext == ".c":
                if delC:
                    os.remove(ffile)
            elif not filter_file(ffile) and (ext not in ('.pyc', '.pyx')
                                             and ext in ('.py', '.pyx')
                                             and not fname.startswith('__')):
                yield os.path.join(parentpath, name, fname)
            elif copyOther and ext not in ('.pyc', '.pyx'):  # Copy other files to./build Directory
                dstdir = os.path.join(basepath, build_dir, parentpath, name)
                if not os.path.isdir(dstdir):
                    os.makedirs(dstdir)
                shutil.copyfile(ffile, os.path.join(dstdir, fname))
        else:
            pass


# Obtain py list
module_set = set(getpy(basepath=currdir, parentpath=parentpath))

## Compile to. so file
try:
    setup(ext_modules=cythonize(module_set, language_level=3),
          script_args=["build_ext", "-b", build_dir, "-t", build_tmp_dir])
    pass
except Exception as ex:
    print("error! ", str(ex))
else:
    # Copy other files to./build Directory
    getpy(basepath=currdir, parentpath=parentpath, copyOther=True)

# Delete temporary files ~
getpy(basepath=currdir, parentpath=parentpath, delC=True)


if os.path.exists(build_tmp_dir):
    shutil.rmtree(build_tmp_dir)

print("Done !")