# -*- coding:utf-8 -*-
import shutil
import os
import sys
# from threading import Thread


def test(copyedsize):
    print copyedsize
def copytree(source,target,callback,length=10485760):
    for subdir, dirs, files in os.walk(unicode(source, 'utf-8')):
        print os.listdir(source)
        for file in files:
            targetpath = os.path.join(subdir, file)
            callback(targetpath)
            #     if not os.path.exists(subdir):
            #         os.makedirs(dst)
            #     uploadFiles.append(os.path.join(subdir, file))
copytree("D:\\temp\\pub_core","D:\\temp\\pub_core2",test)
def copyfile( source,target,callback,length=10485760):
    '''
    :param source:
    :param target:
    :param callback:
    :param length:
    :return:
    '''

    """copy data from file-like object source to file-like object target"""
    source = unicode(source)
    target = unicode(target)
    if not os.path.exists(os.path.dirname(target)):
        os.makedirs(unicode(os.path.dirname(target)))
    fsrc = file(source, 'rb')
    fdst = file(target, 'wb')
    copyedsize = 0

    try:
        while 1:
            buf = fsrc.read(length)
            if not buf:
                break
            copyedsize += length
            callback(copyedsize)
            fdst.write(buf)

        fsrc.close()
        fdst.close()

    except:
        fsrc.close()
        fdst.close()

#
# source = "D:/temp/tree/arrow.png"
# target = "D:/temp/arrow.png"
# copyfile(source,target,test)