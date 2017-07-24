# coding:utf-8
import sys
import os
import locale
from api import whAPI
from api import whDataModels
from wormholeAPI.whDataModels import whEnvData
from wormholeAPI.whAPIModels import whCompany
from whimage import Whimage
from pprint import pprint
try:
    from PyQt4 import QtCore, QtGui, uic
    from PyQt4.QtGui import QApplication, QMainWindow, QPushButton, QWidget
except ImportError as a:
    # print 'use PySide'
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




userpath = os.path.join(os.path.expanduser("~"), 'wormhole','presets')
locale,unicode_locale = locale.getdefaultlocale()


gotListOfDataType = ['singleimage', 'sequenceimage', 'modeldata', 'script', 'photoshop', 'cache', 'mocap',
                             'nuke', 'modo', 'houdini', 'maya', 'AfterEffects', 'etc']


class LocalPub(QWidget):
    def __init__(self,parent=None):
        super(LocalPub, self).__init__(parent)
        self.selectedFile = ""
        self.selectedPreview = ""
        self.nametype = 'name'


        self.whcom = whCompany()
        self.envs = whEnvData('./wormHole_shot.env')
        # self.env = gettaskinfo(self.envs)
        self.whdatas = whDataModels.WormholeData(self.envs)
        self.env = self.whdatas.gettaskinfo()
        # self.projectPubPaths = self.whdatas.ProjectFilePath()

        uipath = './ui/localpubtool.ui'
        try:
            pyside_uicfix.loadUi(uipath, self)
        except NameError:
            uic.loadUi(uipath, self)
        self.setinfo()

        # download useriamge
        imageWh = Whimage(self)
        userimage = imageWh.getUserThumbnail(host=self.env.ServerName,corpPrefix=self.env.Company, rootdir=self.env.SysUserHome,userId=self.env.UserID)
        outputimage = os.path.join(os.path.dirname(userimage),'circular',os.path.split(userimage)[1])
        maskimage = "./image/mask.png"
        imageWh.circular(ofile=userimage, output=outputimage, mask=maskimage)
        pixmap = QtGui.QPixmap(outputimage)
        self.userIcon.setPixmap(pixmap)

        # download task image
        taskthumbnailURL = self.whdatas.ThumbnailPath()
        taskthumbnail = imageWh.getThumbnail(self.env, url=taskthumbnailURL)
        pixmap2 = QtGui.QPixmap(taskthumbnail)
        self.label_2.setPixmap(pixmap2)

        self.listwidget = QtGui.QListWidget()
        self.previewfile = QtGui.QLabel()
        self.previewfile.setTextFormat(QtCore.Qt.RichText)

        self.previewfile.setStyleSheet(
            "QLabel{color: rgb(125, 125, 125);}")


        # tableWidget
        self.tableWidget.setColumnCount(3)
        column_headers = [u'선택한 파일', u'복사 위치', u'Type']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.setFixedHeight(800)

        # project pub path rool





        # button signal
        self.attach_btn.clicked.connect(self.attach)
        self.review_btn.clicked.connect(self.selpreview)
        # self.attachdir_btn.clicked.connect(self.seldir)
        self.send_btn.clicked.connect(self.send)

        # test
        # self.test = QtGui.QTableWidget()
        self.tableWidget.itemSelectionChanged.connect(self.setpubFile)

    def setpubFile(self):
        original,target,type = self.tableWidget.selectedIndexes()
        self.selectedFile = self.tableWidget.item(target.row(),1).text()

    def setinfo(self):
        # print self.env.__dict__
        self.projIdV_lb.setText(unicode(self.env.Project))
        self.projNmV_lb.setText(unicode(self.env.ProjectName))
        if self.env.DirType == "asset":
            self.assetIdV_lb.setText(unicode(self.env.AssetPrefix))
            self.assetNmV_lb.setText(unicode(self.env.AssetName))
            self.seqId_lb.hide()
            self.seqIdV_lb.hide()
            self.seqNm_lb.hide()
            self.seqNmV_lb.hide()
            self.shotId_lb.hide()
            self.shotIdV_lb.hide()
            self.shotNm_lb.hide()
            self.shotNmV_lb.hide()
        elif self.env.DirType == 'shot':
            self.assetIdV_lb.hide()
            self.assetId_lb.hide()
            self.assetNmV_lb.hide()
            self.assetNm_lb.hide()

            self.seqIdV_lb.setText(self.env.SeqId)
            self.seqNmV_lb.setText(self.env.SeqName) #----시퀀스 이름 변경할것
            self.shotIdV_lb.setText(self.env.ShotId)
            self.shotNmV_lb.setText(self.env.ShotName)#----시퀀스 이름 변경할것

        self.taskTypeV_lb.setText(unicode(self.env.TaskType))
        self.userIdV_lb.setText(self.env.UserID)
        self.userNmV_lb.setText(self.env.UserName)




    def gettargetpath(self):
        # data = {'[VERSIONNUMBER]':'10','[PDATATYPE]':'IMAGE'}
        paths = self.whdatas.ProjectFilePath(nametype=self.nametype)
        if self.env.DirType == 'shot':
            targetpath = paths['fixShotPubPath']
        elif self.env.DirType == 'asset':
            targetpath = paths['fixAssetPubPath']
        # targetpath = u"C:\\Users\\simo\\Pictures\\pubtest임"
        return targetpath

    def getpreviewtargetpath(self):
        previewtargetpath =u"C:\\Users\\simo\\Pictures\\pubtest임"
        return previewtargetpath

    def selpreview(self):
        file = QtGui.QFileDialog.getOpenFileName(self, 'Select File', '.')
        filename = os.path.basename(unicode(file))
        if not filename == '':
            name = "<img src='./image/attach-file.png' >  "+filename
            self.previewpath = filename
            self.previewfile.setText(QtCore.QString(unicode(name)))
            self.previewfile.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

            targetpath = os.path.join(self.getpreviewtargetpath(), filename)
            self.previewfile.setStatusTip(targetpath)
            self.previewfile.setToolTip(targetpath)

            self.preview_VLayout.addWidget(self.previewfile)
        self.selectedPreview = file
        self.preview_VLayout.setContentsMargins(30,0,0,0)



    def attach(self):
        self.dialog = QtGui.QFileDialog(self,'Title', ".")
        self.dialog.setOption(self.dialog.DontUseNativeDialog, True)
        self.dialog.setFileMode(self.dialog.ExistingFiles)
        btns = self.dialog.findChildren(QtGui.QPushButton)
        self.dialog.openBtn = [x for x in btns if 'open' in str(x.text()).lower()][0]
        self.dialog.openBtn.clicked.disconnect()
        # self.dialog.openBtn.clicked.connect(self.openClicked)
        self.dialog.openBtn.clicked.connect(self.dialog.hide)
        self.dialog.tree = self.dialog.findChild(QtGui.QTreeView)
        if self.dialog.exec_():
            inds = self.dialog.tree.selectionModel().selectedIndexes()
            files = []
            for i in inds:
                print str(i.data().toString())
                if i.column() == 0:
                    files.append(os.path.join(str(self.dialog.directory().absolutePath()), str(i.data().toString())))
            self.dialog.selectedFiles = files
        # print self.selectedFiles

            # self.hide()
        #
        # file_path = QtGui.QFileDialog.getSaveFileName(self, 'Title', "d:\\temp", "", "",
        #                                               QtGui.QFileDialog.DontUseNativeDialog)
        self.selfiles =  self.dialog.selectedFiles()
        self.settablewidget()

    def settablewidget(self):
        i = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(self.tableWidget.rowCount()+self.selfiles.count())
        for file in self.selfiles:

            if os.path.isfile(file):
                file = str(file)
                target = file.replace(os.path.dirname(file), self.gettargetpath())

                self.tableWidget.setItem(i, 0, QtGui.QTableWidgetItem(unicode(file)))
                self.tableWidget.setItem(i, 1, QtGui.QTableWidgetItem(unicode(target)))
                self.tableWidget.setItem(i, 2, QtGui.QTableWidgetItem(unicode('file')))

            elif os.path.isdir(file):
                dir = str(file)
                target = os.path.join(self.gettargetpath(), os.path.basename(dir))

                self.tableWidget.setItem(i, 0, QtGui.QTableWidgetItem(unicode(dir)))
                self.tableWidget.setItem(i, 1, QtGui.QTableWidgetItem(unicode(target)))
                self.tableWidget.setItem(i, 2, QtGui.QTableWidgetItem(unicode('directory')))
            i+=1
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        # print self.tableWidget.setRowCount()
    # def openClicked(self):
    #
    #
    #     self.dialog.hide()


    def selfile(self):
        filenames = QtGui.QFileDialog.getOpenFileNames(self, 'Select Files', '.')
        # print len(filenames)
        # print filenames
        self.tableWidget.setRowCount(len(filenames))
        i=0
        for files in filenames:
            if os.path.isfile(files):
                file = str(files)
                target = file.replace(os.path.dirname(file), self.gettargetpath())
                oitem = QtGui.QTableWidgetItem(file)
                titem = QtGui.QTableWidgetItem(target)
                pathtype = QtGui.QTableWidgetItem(unicode('file'))

                # self.tableWidget.insertRow(i)
                self.tableWidget.setItem(i, 0, oitem)
                self.tableWidget.setItem(i, 1, titem)
                self.tableWidget.setItem(i, 2, pathtype)
                # print i, ':::' ,oitem, '    --->   ', titem, ' : ',pathtype
                i += 1

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()


    def send(self):
        pass

class ResultUI(QWidget):
    def __init__(self, parent=None):
        super(ResultUI, self).__init__(parent)

        uipath = './ui/replacePath.ui'
        # print uipath
        try:
            pyside_uicfix.loadUi(uipath, self)
        except NameError:
            uic.loadUi(uipath, self)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.start()

    def start(self):
        self.resize(1058,800)
        self.pubtool = LocalPub(self)
        self.setWindowTitle("Local Publish Tool")
        self.setCentralWidget(self.pubtool)
        self.pubtool.send_btn.clicked.connect(self.resultUI)
        self.show()

    def resultUI(self):
        self.resize(1058, 295)
        self.resultui = ResultUI(self)
        self.setCentralWidget(self.resultui)
        self.setWindowTitle("Check target path")
        self.show()
        # print self.pubtool.selectedFile
        # print 'count = ',self.pubtool.listwidget.count()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())


