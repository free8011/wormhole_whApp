
import sys, os
from  PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QFileDialog, QAbstractItemView, QListView, QTreeView, QApplication, QDialog
#
# class getExistingDirectories(QFileDialog):
#     def __init__(self, *args):
#         super(getExistingDirectories, self).__init__(*args)
#         self.setOption(self.DontUseNativeDialog, True)
#         self.setFileMode(self.Directory)
#         # self.setOption(self.ShowDirsOnly, True)
#         self.findChildren(QListView)[0].setSelectionMode(QAbstractItemView.ExtendedSelection)
#         self.findChildren(QTreeView)[0].setSelectionMode(QAbstractItemView.ExtendedSelection)
#
# # qapp = QApplication(sys.argv)
# dlg = getExistingDirectories()
# if dlg.exec_() == QDialog.Accepted:
#     for fileq in dlg.selectedFiles():
#         print unicode(fileq)


class FileDialog(QtGui.QFileDialog):
    def __init__(self, *args):
        QtGui.QFileDialog.__init__(self, *args)
        self.setOption(self.DontUseNativeDialog, True)
        self.setFileMode(self.ExistingFiles)

        btns = self.findChildren(QtGui.QPushButton)
        self.openBtn = [x for x in btns if 'open' in str(x.text()).lower()][0]
        self.openBtn.clicked.disconnect()
        self.openBtn.clicked.connect(self.openClicked)
        self.tree = self.findChild(QtGui.QTreeView)

    def openClicked(self):
        inds = self.tree.selectionModel().selectedIndexes()
        files = []
        for i in inds:
            if i.column() == 0:
                files.append(os.path.join(str(self.directory().absolutePath()),str(i.data().toString())))
        self.selectedFiles = files
        # print files, self.selectedFiles
        self.hide()
    # @property
    def filesSelected(self):

        return self.selectedFiles

# app = QApplication(sys.argv)
# windows = FileDialog()
# if windows.exec_() == QDialog.Accepted:
#     windows.show()
