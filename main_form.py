# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import diary_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(816, 486)
        MainWindow.setStyleSheet("QFrame{\n"
"    border: 0px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setMaximumSize(QtCore.QSize(16777215, 65))
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo = QtWidgets.QFrame(self.header)
        self.logo.setMaximumSize(QtCore.QSize(300, 16777215))
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.logo)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.image = QtWidgets.QLabel(self.logo)
        self.image.setMaximumSize(QtCore.QSize(45, 45))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap(":/images/img/logo.png"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.horizontalLayout_3.addWidget(self.image)
        self.name = QtWidgets.QLabel(self.logo)
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.horizontalLayout_3.addWidget(self.name)
        self.horizontalLayout.addWidget(self.logo)
        self.tools = QtWidgets.QFrame(self.header)
        self.tools.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tools.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tools.setLineWidth(1)
        self.tools.setObjectName("tools")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tools)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.selDB = QtWidgets.QPushButton(self.tools)
        self.selDB.setMinimumSize(QtCore.QSize(0, 45))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/img/db.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selDB.setIcon(icon)
        self.selDB.setIconSize(QtCore.QSize(24, 24))
        self.selDB.setObjectName("selDB")
        self.horizontalLayout_4.addWidget(self.selDB, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.tools)
        self.verticalLayout.addWidget(self.header)
        self.body = QtWidgets.QFrame(self.centralwidget)
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.body)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.list = QtWidgets.QFrame(self.body)
        self.list.setMaximumSize(QtCore.QSize(300, 16777215))
        self.list.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.list.setFrameShadow(QtWidgets.QFrame.Raised)
        self.list.setObjectName("list")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.list)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.list_tools = QtWidgets.QFrame(self.list)
        self.list_tools.setMinimumSize(QtCore.QSize(0, 35))
        self.list_tools.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.list_tools.setFrameShadow(QtWidgets.QFrame.Raised)
        self.list_tools.setObjectName("list_tools")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.list_tools)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.list_tools)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/img/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.findWrite = QtWidgets.QLineEdit(self.list_tools)
        self.findWrite.setObjectName("findWrite")
        self.verticalLayout_4.addWidget(self.findWrite)
        self.verticalLayout_2.addWidget(self.list_tools)
        self.writeList = QtWidgets.QListView(self.list)
        self.writeList.setObjectName("writeList")
        self.verticalLayout_2.addWidget(self.writeList)
        self.horizontalLayout_2.addWidget(self.list)
        self.textedit = QtWidgets.QFrame(self.body)
        self.textedit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textedit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textedit.setObjectName("textedit")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.textedit)
        self.verticalLayout_3.setContentsMargins(0, -1, 4, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textedit_tools = QtWidgets.QFrame(self.textedit)
        self.textedit_tools.setMinimumSize(QtCore.QSize(0, 35))
        self.textedit_tools.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textedit_tools.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textedit_tools.setLineWidth(-4)
        self.textedit_tools.setObjectName("textedit_tools")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.textedit_tools)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.category = QtWidgets.QComboBox(self.textedit_tools)
        self.category.setMinimumSize(QtCore.QSize(150, 0))
        self.category.setObjectName("category")
        self.horizontalLayout_6.addWidget(self.category)
        self.save_write = QtWidgets.QPushButton(self.textedit_tools)
        self.save_write.setMaximumSize(QtCore.QSize(110, 16777215))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/img/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_write.setIcon(icon2)
        self.save_write.setObjectName("save_write")
        self.horizontalLayout_6.addWidget(self.save_write)
        self.delete_write = QtWidgets.QPushButton(self.textedit_tools)
        self.delete_write.setMaximumSize(QtCore.QSize(110, 16777215))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/img/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_write.setIcon(icon3)
        self.delete_write.setObjectName("delete_write")
        self.horizontalLayout_6.addWidget(self.delete_write)
        self.verticalLayout_3.addWidget(self.textedit_tools, 0, QtCore.Qt.AlignTop)
        self.text = QtWidgets.QTextEdit(self.textedit)
        self.text.setObjectName("text")
        self.verticalLayout_3.addWidget(self.text)
        self.imagesList = QtWidgets.QListWidget(self.textedit)
        self.imagesList.setObjectName("imagesList")
        self.verticalLayout_3.addWidget(self.imagesList)
        self.horizontalLayout_2.addWidget(self.textedit)
        self.verticalLayout.addWidget(self.body)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setText(_translate("MainWindow", "Дневник Енотика"))
        self.selDB.setText(_translate("MainWindow", "Выбор БД"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.findWrite.setPlaceholderText(_translate("MainWindow", "Поиск..."))
        self.save_write.setText(_translate("MainWindow", "Сохранить"))
        self.delete_write.setText(_translate("MainWindow", "Удалить"))
import diary_rc