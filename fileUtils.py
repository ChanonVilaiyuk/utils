# file utilities

import os,traceback
import shutil

def createFile(file) : 
    if '\\' in file : 
        file = file.replace('\\', '/')

    dir = file.replace(file.split('/')[-1], '')
    if not os.path.exists(dir) : 
        os.makedirs(dir)

    f = open(file, 'w')
    f.close()
    return True

def writeFile(file, data) : 
    f = open(file, 'w')
    f.write(data)
    f.close()
    return True

def readFile(file) : 
    f = open(file, 'r')
    data = f.read()
    return data


'''
# copy single file only. If copy folder, use copyTree
# example 
# fileUtils.copy('C:/text.txt', 'C:/text2.txt')
'''
def copy(src, dst) : 
    if os.path.exists(src) : 
        dstDir = dst.replace(dst.split('/')[-1], '')
        if not os.path.exists(dstDir) :
            os.makedirs(dstDir)

        shutil.copy2(src, dst)
    return dst


'''
# copy directory. 
# example
# fileUtils.copyTree('C:/test1', 'C:/test2')
'''
def copyTree(src, dst) : 
    if os.path.exists(src) :
        shutil.copytree(src, dst, symlinks=False, ignore=None)
    return dst

'''
# return lines as a list
'''
def readLine(file) : 
	f = open(file)
	lines = f.readlines()
	f.close()

	return lines