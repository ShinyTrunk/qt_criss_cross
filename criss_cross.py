# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'criss_cross.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(724, 746)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn02 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn02.sizePolicy().hasHeightForWidth())
        self.btn02.setSizePolicy(sizePolicy)
        self.btn02.setObjectName("btn02")
        self.gridLayout.addWidget(self.btn02, 2, 0, 1, 1)
        self.btn21 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn21.sizePolicy().hasHeightForWidth())
        self.btn21.setSizePolicy(sizePolicy)
        self.btn21.setObjectName("btn21")
        self.gridLayout.addWidget(self.btn21, 1, 2, 1, 1)
        self.btn22 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn22.sizePolicy().hasHeightForWidth())
        self.btn22.setSizePolicy(sizePolicy)
        self.btn22.setObjectName("btn22")
        self.gridLayout.addWidget(self.btn22, 2, 2, 1, 1)
        self.btn01 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn01.sizePolicy().hasHeightForWidth())
        self.btn01.setSizePolicy(sizePolicy)
        self.btn01.setObjectName("btn01")
        self.gridLayout.addWidget(self.btn01, 1, 0, 1, 1)
        self.btn00 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn00.sizePolicy().hasHeightForWidth())
        self.btn00.setSizePolicy(sizePolicy)
        self.btn00.setObjectName("btn00")
        self.gridLayout.addWidget(self.btn00, 0, 0, 1, 1)
        self.btn12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn12.sizePolicy().hasHeightForWidth())
        self.btn12.setSizePolicy(sizePolicy)
        self.btn12.setObjectName("btn12")
        self.gridLayout.addWidget(self.btn12, 2, 1, 1, 1)
        self.btn20 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn20.sizePolicy().hasHeightForWidth())
        self.btn20.setSizePolicy(sizePolicy)
        self.btn20.setObjectName("btn20")
        self.gridLayout.addWidget(self.btn20, 0, 2, 1, 1)
        self.btn11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn11.sizePolicy().hasHeightForWidth())
        self.btn11.setSizePolicy(sizePolicy)
        self.btn11.setObjectName("btn11")
        self.gridLayout.addWidget(self.btn11, 1, 1, 1, 1)
        self.btn10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn10.sizePolicy().hasHeightForWidth())
        self.btn10.setSizePolicy(sizePolicy)
        self.btn10.setObjectName("btn10")
        self.gridLayout.addWidget(self.btn10, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_3.addWidget(self.pushButton_10)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 29)
        self.verticalLayout.setStretch(2, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "???????????????? - ????????????"))
        self.label.setText(_translate("MainWindow", "???????????????? - ????????????"))
        self.btn02.setText(_translate("MainWindow", "7"))
        self.btn21.setText(_translate("MainWindow", "6"))
        self.btn22.setText(_translate("MainWindow", "9"))
        self.btn01.setText(_translate("MainWindow", "4"))
        self.btn00.setText(_translate("MainWindow", "1"))
        self.btn12.setText(_translate("MainWindow", "8"))
        self.btn20.setText(_translate("MainWindow", "3"))
        self.btn11.setText(_translate("MainWindow", "5"))
        self.btn10.setText(_translate("MainWindow", "2"))
        self.label_2.setText(_translate("MainWindow", "?????? : X"))
        self.pushButton_10.setText(_translate("MainWindow", "??????????????"))
