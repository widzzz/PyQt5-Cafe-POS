# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginkblUEv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_login(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 480)
        self.label_1 = QLabel(Form)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(250, 10, 221, 51))
        self.label_1.setStyleSheet(u"font-size:20pt;;")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 130, 121, 16))
        self.label_2.setStyleSheet(u"font-size: 15pt;;")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 180, 121, 16))
        self.label_3.setStyleSheet(u"font-size: 15pt;;")
        self.lineEdit_1 = QLineEdit(Form)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setGeometry(QRect(220, 130, 241, 25))
        self.lineEdit_1.setStyleSheet(u"font-size:15pt;;")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(220, 180, 241, 25))
        self.lineEdit_2.setStyleSheet(u"font-size:15pt;;")
        self.pushButton_1 = QPushButton(Form)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(370, 220, 91, 31))
        self.pushButton_1.setStyleSheet(u"background-color: rgb(12, 255, 40);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_1.setText(QCoreApplication.translate("Form", u"LOGIN FORM", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"USERNAME :", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"PASSWORD:", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"LOGIN", None))
    # retranslateUi