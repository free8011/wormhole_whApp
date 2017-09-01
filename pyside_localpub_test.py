# coding:utf-8
import locale
import os
import shutil
import sys

from api import whAPI
from api import whDataModels
from api.whimage import Whimage
from wormholeAPI.whAPIModels import whCompany
from wormholeAPI.whDataModels import whEnvData

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




userpath = os.path.join(os.path.expanduser("~"), 'wormhole','presets')
locale,unicode_locale = locale.getdefaultlocale()


getListOfDataType = ['singleimage', 'sequenceimage', 'modeldata', 'script', 'photoshop', 'cache', 'mocap',
                             'nuke', 'modo', 'houdini', 'maya', 'AfterEffects', 'etc']


class LocalPub(QWidget):
    def __init__(self,parent=None):
        super(LocalPub, self).__init__(parent)
        self.Column_originFile = 0
        self.Column_targetFile = 1
        self.Column_type = 2
        self.selectedFile = ""
        self.selectedPreview = {'ofile':'',
                                'tfile':''}
        self.nametype = self.parent().Nametype

        self.whcom = whCompany()
        self.envs = whEnvData('./wormHole.env')
        # self.env = gettaskinfo(self.envs)
        self.whdatas = whDataModels.WormholeData(self.envs)
        self.env = self.whdatas.gettaskinfo()
        # self.projectPubPaths = self.whdatas.ProjectFilePath()

        uipath = '%s/ui/localpubtool.ui'%self.env.WhAppPath
        try:
            pyside_uicfix.loadUi(uipath, self)
        except NameError:
            uic.loadUi(uipath, self)
        self.setinfo()
        self.pdatatype_cb.addItems(getListOfDataType)
        # self.pdatatype_cb.setStyleSheet(QComboBox{})

        # download useriamge
        imageWh = Whimage(self)
        userimage = imageWh.getUserThumbnail(host=self.env.ServerName,corpPrefix=self.env.Company, rootdir=self.env.SysUserHome,userId=self.env.UserID)
        outputimage = os.path.join(os.path.dirname(userimage),'circular',os.path.split(userimage)[1])
        maskimage = "%s/image/mask.png"%self.env.WhAppPath
        imageWh.circular(ofile=userimage, output=outputimage, mask=maskimage)
        pixmap = QtGui.QPixmap(outputimage)

        self.userIcon.setPixmap(pixmap)

        # download task image
        taskthumbnailURL = self.whdatas.ThumbnailPath()
        taskthumbnail = imageWh.getThumbnail(self.env, url=taskthumbnailURL)
        pixmap2 = QtGui.QPixmap(taskthumbnail)
        self.label_2.setPixmap(pixmap2)

        # self.progressBar = QtGui.QProgressBar(self)

        self.previewfile = QtGui.QLabel()
        self.previewfile.setTextFormat(QtCore.Qt.RichText)

        self.previewfile.setStyleSheet(
            "QLabel{color: rgb(125, 125, 125);}")


        # tableWidget
        self.tableWidget.setColumnCount(3)
        self.setFixedHeight(800)

        # set version
        self.versionV_lb.setText(self.env.VersionNumber)

        # button signal
        self.attach_btn.clicked.connect(self.attach)
        self.preview_btn.clicked.connect(self.selpreview)
        self.send_btn.clicked.connect(self.send)

        self.tableWidget.itemSelectionChanged.connect(self.setpubFile)
        self.pdatatype_cb.currentIndexChanged.connect(self.setTargetPath)
        self.pdatatype_cb.editTextChanged.connect(self.setTargetPath)
        self.path_setting_btn.clicked.connect(self.reTargetpath)

        # column_headers = [u'선택한 파일', u'복사 위치', u'Type']
        column_headers = [u'selected file', u'copy path', u'Type']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        if self.parent().languageSets == 'cn':
            self.setMenuText()

    def reTargetpath(self):
        self.uis = EditDirPathUI(self)

        self.uis.setGeometry(0,0,self.width(),self.height())
        self.uis.ok_btn2.clicked.connect(self.resetTargetPath)
        self.uis.show()

    def setMenuText(self):
        column_headers = [u'已选文件', u'发送文件位置', u'文件类型']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        self.attach_btn.setText(u'+ 添加附件')
        self.path_setting_btn.setText(u'路径设置')
        self.send_btn.setText(u'文件上传')
        self.preview_btn.setText(u'+ 添加预览附件')
        self.comments_lb.setText(u'评论')
        self.projId_lb.setText(u'项目ID')
        self.projNm_lb.setText(u'项目名称')
        self.assetId_lb.setText(u'资产ID')
        self.assetNm_lb.setText(u'资产名称')
        self.seqId_lb.setText(u'场次ID')
        self.seqNm_lb.setText(u'场次名称')
        self.shotId_lb.setText(u'镜头ID')
        self.shotNm_lb.setText(u'镜头名称')
        self.Version_lb.setText(u'上传版本')
        self.taskType_lb.setText(u'任务类型')
        self.UserNm_lb.setText(u'用户名称')
        self.UserId_lb.setText(u'用户ID')

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

    def gettargetpath(self,pathtype = 'file'):
        '''

        :param pathtype: 'file' or 'preview'. default value : 'file'
        :return:
        '''
        # data = {'[VERSIONNUMBER]':'10','[PDATATYPE]':'IMAGE'}
        paths = self.whdatas.ProjectFilePath(nametype=self.nametype,
                                             pdatatype=unicode(self.pdatatype_cb.currentText()))
        # pprint(paths)
        if self.env.DirType == 'shot':
            targetpath = paths['fixShotPubPath']
            targetpreview = paths['fixShotMovPath']
        elif self.env.DirType == 'asset':
            targetpath = paths['fixAssetPubPath']
            targetpreview = paths['fixAssetMovPath']
        # targetpath = u"C:\\Users\\simo\\Pictures\\pubtest임"
        # pprint(paths)
        if pathtype == 'file':
            return targetpath
        elif pathtype == 'preview':
            return targetpreview

    def selpreview(self):
        file = QtGui.QFileDialog.getOpenFileName(self, 'Select File', '.')
        if not file =='' :
            filename = os.path.basename(unicode(file))
            if not filename == '':
                name = "<img src='./image/attach-file.png' >  "+filename
                self.previewpath = filename
                self.previewfile.setText(QtCore.QString(unicode(name)))
                self.previewfile.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
                name,ext = os.path.splitext(filename)
                filename = '%s_%05d%s'%(name,int(self.env.MovAbsNumber),ext)
                targetpath = os.path.join(unicode(self.gettargetpath('preview')), unicode(filename))
                self.previewfile.setStatusTip(targetpath)
                self.previewfile.setToolTip(targetpath)

                self.preview_VLayout.addWidget(self.previewfile)
            self.selectedPreview['ofile'] = file
            self.selectedPreview['tfile'] = targetpath
            # self.selectedPreview = file
            self.preview_VLayout.setContentsMargins(30,0,0,0)



    def attach(self):
        self.selfiles = None
        self.dialog = QtGui.QFileDialog(self,'Title', u".")
        self.dialog.setOption(self.dialog.DontUseNativeDialog, True)
        self.dialog.setFileMode(self.dialog.ExistingFiles)
        btns = self.dialog.findChildren(QtGui.QPushButton)
        self.dialog.openBtn = [x for x in btns if 'open' in str(x.text()).lower()][0]
        self.dialog.openBtn.clicked.disconnect()
        self.dialog.openBtn.clicked.connect(self.dialog.hide)
        self.dialog.tree = self.dialog.findChild(QtGui.QTreeView)
        self.selectedFiles2 = []
        # self.dialog.tree.doubleClicked.connect(self.test)
        if self.dialog.exec_():
            inds = self.dialog.tree.selectionModel().selectedIndexes()
            files = []
            for i in inds:
                # print str(i.data().toString())
                if i.column() == 0:
                    filepath = os.path.join(unicode(self.dialog.directory().absolutePath()), unicode(i.data().toString()))
                    files.append(unicode(os.path.normpath(filepath)))
                    self.selectedFiles2.append(unicode(filepath))
            self.dialog.selectedFiles = files
        self.selfiles =  self.dialog.selectedFiles()
        self.settablewidget()
    # def test(self,index):
    #     item = self.dialog.selectedIndexes()[0]
    #     print item.model().itemFromIndex(index).text()

    def settablewidget(self):
        i = self.tableWidget.rowCount()

        self.tableWidget.setRowCount(self.tableWidget.rowCount()+self.selfiles.count())
        for file in self.selfiles:
            file = unicode(file)
            if os.path.isfile(file):
                target = os.path.normpath(file.replace(os.path.dirname(file), self.gettargetpath()))
                self.tableWidget.setItem(i, 0, QtGui.QTableWidgetItem(unicode(file)))
                self.tableWidget.setItem(i, 1, QtGui.QTableWidgetItem(unicode(target)))
                self.tableWidget.setItem(i, 2, QtGui.QTableWidgetItem(unicode('file')))

            elif os.path.isdir(file):
                dir = unicode(file)
                target = os.path.join(self.gettargetpath(), os.path.basename(dir))
                self.tableWidget.setItem(i, 0, QtGui.QTableWidgetItem(unicode(dir)))
                self.tableWidget.setItem(i, 1, QtGui.QTableWidgetItem(unicode(target)))
                self.tableWidget.setItem(i, 2, QtGui.QTableWidgetItem(unicode('directory')))
            i+=1
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def setTargetPath(self):

        for i in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(i, self.Column_type).text() == 'file':
                ofile = unicode(self.tableWidget.item(i, self.Column_originFile).text())
                target = os.path.normpath(ofile.replace(os.path.dirname(ofile), self.gettargetpath()))
                self.tableWidget.setItem(i, self.Column_targetFile, QtGui.QTableWidgetItem(unicode(target)))

            elif self.tableWidget.item(i, self.Column_type).text() == 'directory':
                odir = unicode(self.tableWidget.item(i, self.Column_originFile).text())
                target = os.path.join(self.gettargetpath(), os.path.basename(odir))
                self.tableWidget.setItem(i, self.Column_targetFile, QtGui.QTableWidgetItem(unicode(target)))
            i += 1
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def resetTargetPath(self):

        if self.uis.preview_le2.text() != '':
            # print 'tpreviewpath : none'
            tpreviewpath = self.selectedPreview['tfile'].replace(
                os.path.dirname(unicode(self.selectedPreview['tfile'])),
                unicode(self.uis.tpreviewpath))

            self.previewfile.setStatusTip(tpreviewpath)
            self.previewfile.setToolTip(tpreviewpath)
            self.selectedPreview['tfile'] = tpreviewpath

        if self.uis.pub_le2.text() != '':
            # print 'tpreviewpath : none'
            tpubpath = unicode(self.uis.tpubpath)
            for i in range(self.tableWidget.rowCount()):
                if self.tableWidget.item(i, self.Column_type).text() == 'file':
                    otfile = unicode(self.tableWidget.item(i, self.Column_targetFile).text())
                    target = os.path.normpath(otfile.replace(os.path.dirname(otfile), tpubpath))

                    self.tableWidget.setItem(i, self.Column_targetFile, QtGui.QTableWidgetItem(unicode(target)))

                elif self.tableWidget.item(i, self.Column_type).text() == 'directory':
                    otdir = unicode(self.tableWidget.item(i, self.Column_targetFile).text())
                    target = os.path.join(tpubpath, os.path.basename(otdir))

                    self.tableWidget.setItem(i, self.Column_targetFile, QtGui.QTableWidgetItem(unicode(target)))
                i += 1
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()


        self.uis.close()

    def send(self):
        pubfile = unicode(self.selectedFile)
        opubfile = ''
        # pub files copy
        uploadFiles = []
        if pubfile == '':
            reply = QtGui.QMessageBox.question(self, 'Message',
                                               "please select one file", QtGui.QMessageBox.Ok ,
                                               QtGui.QMessageBox.Ok)

            if reply == QtGui.QMessageBox.Yes:
                print 'yes'
            else:
                print 'no'
        else:
            for i in range(self.tableWidget.rowCount()):
                if self.tableWidget.item(i,self.Column_type).text() == 'file':
                    ofile = unicode(self.tableWidget.item(i,self.Column_originFile).text())
                    tfile = unicode(self.tableWidget.item(i,self.Column_targetFile).text())
                    self.copyfileobj(unicode(ofile), unicode(tfile))
                    uploadFiles.append(tfile)
                    if ofile == pubfile:
                        opubfile = ofile
                elif self.tableWidget.item(i,self.Column_type).text() == 'directory':
                    odir = self.tableWidget.item(i,self.Column_originFile).text()
                    tdir = self.tableWidget.item(i,self.Column_targetFile).text()

                    self.copytree(unicode(odir),unicode(tdir))
                    for subdir, dirs, files in os.walk(unicode(tdir,'utf-8')):

                        print '-' * 20
                        print subdir
                        print dirs
                        print files
                        for file in files:
                            uploadFiles.append(os.path.join(subdir,file))
                        print '-' * 20

            data = {}

            # movie file copy
            if not self.selectedPreview['ofile'] == '':
                omovie = self.selectedPreview['ofile']
                tmovie = self.selectedPreview['tfile']
                uploadFiles.append(tmovie)
                self.copyfileobj(unicode(omovie),unicode(tmovie))
                data["movie"] = tmovie
                data["originalSelectedMovie"] = omovie
            else:
                data["movie"] = ''
                data["originalSelectedMovie"] = ''

            comments =  unicode(self.textEdit.toPlainText())

            self.whUpdate = whAPI.Post(self.env.Company,self.env.ServerName)
            data["projectId"] = self.env.Project
            data["versionNumber"] = self.env.VersionNumber
            data["publisherId"] = self.env.UserID
            data["taskTypeCd"] = self.env.TaskTypeCode
            data["originalSelectedFile"] = opubfile
            data["publishComment"] = comments

            if self.env.DirType == 'shot':
                data["shotId"] = self.env.ShotId
                data["file"] = pubfile
                data["PdataType"] = unicode(self.pdatatype_cb.currentText())
                self.whUpdate.publishShot(data=data,dictype=True)

            elif self.env.DirType == 'asset':
                data["assetId"] = self.env.AssetPrefix
                data["filePublish"] = pubfile
                data["PdataType"] = unicode(self.pdatatype_cb.currentText())
                self.whUpdate.publishAsset(data=data, dictype=True)

            self.parent().closed()


    def copyfileobj(self, source, target,  length=10485760):
        '''

        :param fsrc: file(sourceFile,'rb')
        :param fdst: file(targetFile,'wb')
        :param path: sourceFile
        :param length:
        :return:
        '''
        """copy data from file-like object fsrc to file-like object fdst"""
        print os.path.dirname(unicode(target))
        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(unicode(os.path.dirname(target)))
        fsrc = file(source,'rb')
        fdst = file(target,'wb')
        buffersize = 0
        filesize = os.path.getsize(source)
        self.progressBar = QtGui.QProgressBar(self)
        self.progressBar.show()

        self.progressBar.setGeometry(self.width()/5,self.height()/3,self.width()/2,self.height()/15)
        self.progressBar.setValue(0)
        QApplication.processEvents()

        try:
            while 1:
                buf = fsrc.read(length)
                if not buf:
                    break
                buffersize += length
                fdst.write(buf)
                if filesize > buffersize:
                    self.progressBar.setValue(int(float(buffersize) / float(filesize) * 100))
                    QApplication.processEvents()
            fsrc.close()
            fdst.close()
            self.progressBar.setValue(100)
        except:
            fsrc.close()
            fdst.close()
        self.progressBar.hide()

    def copytree(self, src, dst, symlinks=False, ignore=None):
        names = os.listdir(src)
        if ignore is not None:
            ignored_names = ignore(src, names)
        else:
            ignored_names = set()
        if not os.path.exists(dst):
            os.makedirs(dst)
        errors = []
        for name in names:
            if name in ignored_names:
                continue
            srcname = os.path.join(src, name)
            dstname = os.path.join(dst, name)
            try:
                if symlinks and os.path.islink(srcname):
                    linkto = os.readlink(srcname)
                    os.symlink(linkto, dstname)
                elif os.path.isdir(srcname):
                    self.copytree(srcname, dstname, symlinks, ignore)
                else:
                    shutil.copy2(srcname, dstname)
                # XXX What about devices, sockets etc.?
            except (IOError, os.error) as why:
                errors.append((srcname, dstname, str(why)))
            # catch the Error from the recursive copytree so that we can
            # continue with other files

        try:
            shutil.copystat(src, dst)
        except WindowsError:
            # can't copy file access times on Windows
            pass
        except OSError as why:
            errors.extend((src, dst, str(why)))

class EditDirPathUI(QWidget):
    def __init__(self, parent=None):
        super(EditDirPathUI, self).__init__(parent)
        
        self.tpreviewpath = ''
        self.tpubpath = ''
        uipath = '%s/ui/replacePath.ui'%self.parent().env.WhAppPath
        # print uipath
        try:
            pyside_uicfix.loadUi(uipath, self)
        except NameError:
            uic.loadUi(uipath, self)
        self.preview_btn2.clicked.connect(self.getpreviewpath)
        self.pub_btn2.clicked.connect(self.getpubpath)
        self.cancle_btn2.clicked.connect(self.close)

        if self.parent().parent().languageSets == 'cn':
            self.setMenuText()

    def getpreviewpath(self):
        # dir = QtGui.QFileDialog.DirectoryOnly(self, 'Select Directory', '.')
        self.tpreviewpath = unicode(QtGui.QFileDialog.getExistingDirectory(self, 'selectDirectory','.'))
        self.preview_le2.setText(self.tpreviewpath)


    def getpubpath(self):
        # dir = QtGui.QFileDialog.DirectoryOnly(self, 'Select Directory', '.')
        self.tpubpath = unicode(QtGui.QFileDialog.getExistingDirectory(self, 'selectDirectory','.'))
        self.pub_le2.setText(self.tpubpath)

    def setMenuText(self):
        self.parent().setWindowTitle(u'更改路径')
        self.preview_lb2.setText(u'预览文件路径')
        self.pub_lb2.setText(u'上传文件路径')
        self.cancle_btn2.setText(u'取消')
        self.ok_btn2.setText(u'确认')


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        app_icon = QtGui.QIcon('WH_Icon16.png')
        self.setWindowIcon(app_icon)

        self.settings = QtCore.QSettings("__settings.ini", QtCore.QSettings.IniFormat)

        menubar = self.menuBar()
        settingmenu = menubar.addMenu("setting")
        editmenu = menubar.addMenu('Edit')


        self.setkeyname = QtGui.QAction(settingmenu)
        self.setkeyname.setCheckable(True)
        self.setkeyname.setText(_translate("MainWindow", "name", None))
        self.setkeyname.triggered.connect(lambda: self.setNametype(name=True))

        self.setkeyid = QtGui.QAction(editmenu)
        self.setkeyid.setCheckable(True)
        self.setkeyid.setText(_translate("MainWindow", "ID", None))
        self.setkeyid.triggered.connect(lambda: self.setNametype(id=True))

        settingmenu.addAction(self.setkeyname)
        settingmenu.addAction(self.setkeyid)

        Languagemenu = editmenu.addMenu('Language')

        self.actionEnglish = QtGui.QAction(editmenu)
        self.actionEnglish.setCheckable(True)
        self.actionEnglish.setText(_translate("MainWindow", "English", None))
        self.actionEnglish.triggered.connect(lambda: self.languagecheck(en=True))

        self.actionChinese = QtGui.QAction(editmenu)
        self.actionChinese.setCheckable(True)
        self.actionChinese.setText(_translate("MainWindow", "Chinese", None))
        self.actionChinese.triggered.connect(lambda: self.languagecheck(cn=True))

        Languagemenu.addAction(self.actionEnglish)
        Languagemenu.addAction(self.actionChinese)
        if self.settings.value('languageSet').toString() == 'en':
            self.languageSets = 'en'
            self.actionEnglish.setChecked(True)
        elif self.settings.value('languageSet').toString() == 'cn':
            self.languageSets = 'cn'
            self.actionChinese.setChecked(True)

        self.languageSets = self.settings.value('languageSet').toString()

        if self.settings.value('defaultkey').toString() == 'name':
            self.setkeyname.setChecked(True)
        elif self.settings.value('defaultkey').toString() == 'id':
            self.setkeyid.setChecked(True)
        self.Nametype = self.settings.value('defaultkey').toString()

        self.start()

    def closeEvent(self, event):
        if self.actionEnglish.isChecked():
            self.settings.setValue('languageSet','en')
        elif self.actionChinese.isChecked():
            self.settings.setValue('languageSet','cn')

        if self.setkeyname.isChecked():
            self.settings.setValue('defaultkey','name')
        elif self.setkeyid.isChecked():
            self.settings.setValue('defaultkey','id')

    def languagecheck(self,en=False,cn=False):
        self.actionEnglish.setChecked(en)
        self.actionChinese.setChecked(cn)
        if en:
            self.languageSets = 'en'
            self.setWindowTitle(u"Local Publish Tool")
        elif cn:
            self.languageSets = 'cn'
            self.setWindowTitle(u"发布其他文件")
        self.pubtool.close()
        self.start()

    def setNametype(self,name=False,id=False):
        self.setkeyname.setChecked(name)
        self.setkeyid.setChecked(id)
        if name:
            self.Nametype = 'name'
        elif id:
            self.Nametype = 'id'
        self.pubtool.close()
        self.start()

    def preference(self):
        print 'preference'

    def start(self):

        self.resize(1058,800)
        self.pubtool = LocalPub(self)
        if self.settings.value('languageSet').toString() == 'en':
            self.setWindowTitle(u"Local Publish Tool")
        elif self.settings.value('languageSet').toString() == 'cn':
            self.setWindowTitle(u"发布其他文件")

        self.setCentralWidget(self.pubtool)
        # self.pubtool.path_setting_btn.clicked.connect(self.resultUI)
        self.show()

    def editdirpathUI(self):
        self.resize(1058, 295)
        self.edp = EditDirPathUI(self)
        self.setCentralWidget(self.edp)
        self.setWindowTitle("Check target path")
        self.edp.ok_btn2.clicked.connect(self.pubtool)
        self.show()


    def closed(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())


