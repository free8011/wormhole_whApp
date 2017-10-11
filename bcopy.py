# -*- coding:utf-8 -*-
import shutil
import os
import sys
try:
    from PyQt4 import QtCore, QtGui, uic
    from PyQt4.QtGui import QApplication, QMainWindow, QPushButton, QWidget
except ImportError as a:
    from PySide import QtCore, QtGui
    from PySide.QtGui import QApplication, QMainWindow, QPushButton, QWidget
    import pyside_uicfix



import sys
# from threading import Thread

class porgressCopy(QWidget):
    def __init__(self, parent=None):
        super(porgressCopy, self).__init__(parent)
        uipath = '%s/ui/uploadCheck.ui' % self.parent().env.WhAppPath
        try:
            pyside_uicfix.loadUi(uipath, self)
        except NameError:
            uic.loadUi(uipath, self)
    def copygui(self, copyinfo):
        if copyinfo['idx']:
            print 'change file'
        else:
            print 'keep going'
        print copyinfo
        return copyinfo

    def copyfile(self, source,target,callback,length=10485760):
        """copy data from file-like object source to file-like object target"""
        source = unicode(source)
        target = unicode(target)
        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(unicode(os.path.dirname(target)))
        fsrc = file(source, 'rb')
        fdst = file(target, 'wb')
        copyedsize = 0
        filesize = os.path.getsize(source)
        copyinfo = {}

        try:
            while 1:

                copyinfo['progressValue'] = 0
                copyinfo['filename'] = target
                copyinfo['idx'] = False

                buf = fsrc.read(length)
                if not buf:
                    break
                copyedsize += length
                fdst.write(buf)
                if filesize > copyedsize:
                    # progressValue = int(float(copyedsize) / float(filesize) * 100)
                    copyinfo['progressValue'] = int(float(copyedsize) / float(filesize) * 100)
                elif filesize <= copyedsize:
                    # progressValue = 100
                    copyinfo['progressValue'] = 100
                    copyinfo['idx'] = True

                callback(copyinfo)
            fsrc.close()
            fdst.close()


        except:
            fsrc.close()
            fdst.close()

    def copytree(self, source, target, symlinks=False, ignore=None):
        source = unicode(source)
        target = unicode(target)
        names = os.listdir(source)
        file_counter = sum([len(files) for r, d, files in os.walk(source)])
        copyed = 0

        if ignore is not None:
            ignored_names = ignore(source, names)
        else:
            ignored_names = set()
        if not os.path.exists(target):
            os.makedirs(target)

        errors = []
        for name in names:
            if name in ignored_names:
                continue
            srcname = os.path.join(source, name)
            dstname = os.path.join(target, name)
            try:
                if symlinks and os.path.islink(srcname):
                    linkto = os.readlink(srcname)
                    os.symlink(linkto, dstname)
                elif os.path.isdir(srcname):
                    self.copytree(srcname, dstname, symlinks, ignore)
                else:
                    self.copyfile(srcname, dstname, self.copygui)
                    copyed += 1

                    # XXX What about devices, sockets etc.?
            except (IOError, os.error) as why:
                errors.append((srcname, dstname, str(why)))
                # catch the Error from the recursive copytree so that we can
                # continue with other files

        try:
            shutil.copystat(source, target)
        except WindowsError:
            # can't copy file access times on Windows
            pass
        except OSError as why:
            errors.extend((source, target, str(why)))




#
#
# def test(copyinfo):
#
#     if copyinfo['idx']:
#         print 'change file'
#     else:
#         print 'keep going'
#     print copyinfo
#     return copyinfo
#
# def copyfile( source,target,callback,length=10485760):
# # def copyfile( source,target,callback,length=500):
#     '''
#     :param source:
#     :param target:
#     :param callback:
#     :param length:
#     :return:
#     '''
#
#     """copy data from file-like object source to file-like object target"""
#     source = unicode(source)
#     target = unicode(target)
#     if not os.path.exists(os.path.dirname(target)):
#         os.makedirs(unicode(os.path.dirname(target)))
#     fsrc = file(source, 'rb')
#     fdst = file(target, 'wb')
#     copyedsize = 0
#     filesize = os.path.getsize(source)
#     copyinfo = {}
#
#     try:
#         while 1:
#
#             copyinfo['progressValue'] = 0
#             copyinfo['filename'] = target
#             copyinfo['idx'] = False
#
#             buf = fsrc.read(length)
#             if not buf:
#                 break
#             copyedsize += length
#             fdst.write(buf)
#             if filesize > copyedsize:
#                 # progressValue = int(float(copyedsize) / float(filesize) * 100)
#                 copyinfo['progressValue'] = int(float(copyedsize) / float(filesize) * 100)
#             elif filesize <= copyedsize:
#                 # progressValue = 100
#                 copyinfo['progressValue'] =100
#                 copyinfo['idx'] = True
#
#             callback(copyinfo)
#         fsrc.close()
#         fdst.close()
#
#
#     except:
#         fsrc.close()
#         fdst.close()
#
#
# # #
# # source = "D:/temp/tree/arrow.png"
# # target = "D:/temp/arrow.png"
# # copyfile(source,target,test)
#
# def copytree(source, target,  symlinks=False, ignore=None):
#     source = unicode(source)
#     target = unicode(target)
#     names = os.listdir(source)
#     file_counter = sum([len(files) for r, d, files in os.walk(source)])
#     copyed = 0
#
#     if ignore is not None:
#         ignored_names = ignore(source, names)
#     else:
#         ignored_names = set()
#     if not os.path.exists(target):
#         os.makedirs(target)
#
#     errors = []
#     for name in names:
#         if name in ignored_names:
#             continue
#         srcname = os.path.join(source, name)
#         dstname = os.path.join(target, name)
#         try:
#             if symlinks and os.path.islink(srcname):
#                 linkto = os.readlink(srcname)
#                 os.symlink(linkto, dstname)
#             elif os.path.isdir(srcname):
#                 copytree(srcname, dstname, symlinks, ignore)
#             else:
#                 copyfile(srcname, dstname, test)
#                 copyed += 1
#
#                 # XXX What about devices, sockets etc.?
#         except (IOError, os.error) as why:
#             errors.append((srcname, dstname, str(why)))
#             # catch the Error from the recursive copytree so that we can
#             # continue with other files
#
#     try:
#         shutil.copystat(source, target)
#     except WindowsError:
#         # can't copy file access times on Windows
#         pass
#     except OSError as why:
#         errors.extend((source, target, str(why)))
#
#
# copytree("D:\\tmp\\wormholeTest","D:\\tmp\\pub_core2")
