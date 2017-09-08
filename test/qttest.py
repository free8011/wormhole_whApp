 # -*- coding:utf-8 -*-
 import os
 import sys

 from PyQt4 import QtCore, QtGui
 from PyQt4 import uic

 from api import whimage





 # app = QtGui.QApplication(sys.argv)
# window = uic.loadUi("D:/Dev_project/wormhole/python/testProject/PyQtTest/testui.ui")
# window.show()

print os.path.abspath('')
MainWindowForm, MainWindowBase = uic.loadUiType("./ui/testui.ui")

class MainWindow(MainWindowBase,MainWindowForm):
    # nam = QNetworkAccessManager()

    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        userimage = "./image/test3.jpg"
        maskimage = "./image/mask.png"
        outputimage = "./image/user/test3.png"
        whimage.circular(ofile=userimage, output=outputimage, mask=maskimage)
        pixmap = QtGui.QPixmap(outputimage)
        self.userIcon.setPixmap(pixmap)

        QtCore.QObject.connect(self.attach_btn, QtCore.SIGNAL("clicked()"),self.selfile)
        QtCore.QObject.connect(self.send_btn, QtCore.SIGNAL("clicked()"), self.send)


        self.show()
    def selfile(self):
        filenames = QtGui.QFileDialog.getOpenFileNames(self, 'Select Files', '.')
        self.addfilesgui(filenames)

    def addfilesgui(self, files):
        for filename in files:
            self.filelabel = QtGui.QLabel(filename)
            self.verticalLayout_4.addWidget(self.filelabel)
        self.verticalLayout_4.setAlignment(Qt.AlignTop)

    def send(self):
        num = self.verticalLayout_4.count()
        for i in range(num):
            widget = self.verticalLayout_4.itemAt(i).widget()
            file = widget.text()


            try:
                dirpath = os.path.dirname(str(file))+'2'
                filename = os.path.basename(str(file))
                os.makedirs(unicode(dirpath))

            except OSError as exc:
                print exc
            except Exception as err:
                print err
            finally:
                print 'done'


EditForm, EditBase = uic.loadUiType('./ui/ui1.ui')
class EditUI(EditForm, EditBase ):
    def __init__(self, filepath):
        self.setupUi(self)


def run():
    app = None
    if ( not app ):
        app = QtGui.QApplication(sys.argv)

    window = MainWindow()


    if ( app ):
        sys.exit(app.exec_())

if __name__ == "__main__":
    run()
