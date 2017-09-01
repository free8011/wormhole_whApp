import sys
import os
import ftplib
from ConfigParser import SafeConfigParser

try:
    from PyQt4 import QtCore, QtGui, uic
    from PyQt4.QtGui import QApplication, QMainWindow, QPushButton, QWidget
except ImportError as a:
    print 'use PySide'
    from PySide import QtCore, QtGui
    from PySide.QtGui import QApplication, QMainWindow, QPushButton, QWidget
    import pyside_uicfix
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)




class Ftpuploader(QWidget):
    def __init__(self, parent=None,copyfile_list=None):
        super(Ftpuploader, self).__init__(parent)
        self.copyfile_list = copyfile_list
        self.env = self.parent().env
        self.uploadFTP_fn()

    def uploadFTP_fn(self ):

        # uploadFTP.upload(appDir,self.selectCopyFile)

        parserFTP = SafeConfigParser()
        FTPtmpPath = "%s%s/%s/wormhole/python/FTPReview/tmp/FTPsetting.env"%( self.env.ProjectHome, self.env.Company, self.env.Project)
        if not os.path.exists(os.path.dirname(FTPtmpPath)):
            os.makedirs(os.path.dirname(FTPtmpPath))

        etcstr = '#FTPDefaultDirRoot is the path before File server home directory path in FTP path. \n#e.g. in FTP path : "/home/wormhole_test/FILESERVERDIR/PROJECTID" \n#"/home/wormhole_test" is FTPDefaultDirRoot path \n'
        if not os.path.exists(FTPtmpPath):
            settingFile = open(FTPtmpPath, 'w')
            settingFile.write(etcstr)
            settingFile.close()

        parserFTP.read(FTPtmpPath)
        test = parserFTP._sections
        for FTPlist in test.keys():
            ftpuploadFile = []
            userFTP = test[FTPlist]

            FTPHOST = userFTP.get('host')
            FTPID = userFTP.get('id')
            FTPPW = userFTP.get('pw')
            FTPPORT = userFTP.get('port')
            FTPDefaultDirRoot  = userFTP.get('ftpdefaultdirroot')

            if FTPPORT == '':
                ftp = ftplib.FTP(FTPHOST)
            else:

                ftp = ftplib.FTP()
                ftp.connect(FTPHOST, FTPPORT)

            ftp.login(FTPID, FTPPW)

            for file in self.copyfile_list:
                self.ftpuploadValue = 0
                self.filesize = os.path.getsize(file)
                filepathlists = str(file).split(os.sep)
                filepathlists.pop(0)
                filepathlists.insert(0, FTPDefaultDirRoot)

                ftpfilepath = '/'.join(filepathlists)
                ftpuploadFile.append(ftpfilepath)

                dirList = ftpfilepath.split(os.sep)

                dircheck =[ '']
                for i in range(len(dirList)- 1 ):
                    self.label_10.setText('FTPUpload..')
                    if not dirList[i] == '':
                        dircheck.append(dirList[i])
                    tests = '/'.join(dircheck)
                    try:
                        ftp.cwd(tests)

                    except:
                        ftp.mkd(dirList[i])
                        ftp.cwd(tests)
                # self.progressBar = progressBar()
                self.progressBar = QtGui.QProgressBar()

                self.progressBar.setWindowTitle('ftp upload')
                self.progressBar.show()
                self.progressBar.progressBar.setValue(0)

                try:
                    UPloadFTPfile = open(file, 'rb')
                    ftp.storbinary('STOR %s'% ( filepathlists[-1].encode('utf-8')), UPloadFTPfile , callback=self.Reader,
                                   blocksize=1024)
                    self.progressBar.close()
                    UPloadFTPfile.close()
                except:
                    print 'error %s' % file


    def Reader(self, block):
        self.ftpuploadValue = self.ftpuploadValue + len(block)
        self.progressBar.progressBar.setValue(int(float(self.ftpuploadValue) / float(self.filesize) * 100))

