# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TransactionWzJfJb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import datetime

class Ui_transaction(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 480)
        self.label_1 = QLabel(Dialog)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(230, 70, 171, 31))
        self.label_1.setStyleSheet(u"FONT-SIZE:20PT;;\n"
"")
        self.pushButton_1 = QPushButton(Dialog)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(10, 450, 75, 23))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(418, 240, 161, 23))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(68, 240, 171, 16))
        self.lineEdit_1 = QLineEdit(Dialog)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setGeometry(QRect(230, 240, 181, 20))
        self.comboBox_1 = QComboBox(Dialog)
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.setObjectName(u"comboBox_1")
        self.comboBox_1.setGeometry(QRect(70, 160, 69, 22))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(68, 270, 171, 16))
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(230, 270, 181, 20))
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(560, 450, 75, 23))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_1.setText(QCoreApplication.translate("Dialog", u"PEMBAYARAN", None))
        self.pushButton_1.setText(QCoreApplication.translate("Dialog", u"KEMBALI", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"HITUNG JUMLAH KEMBALIAN", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"JUMLAH UANG YANG DIBAYAR :", None))
        self.comboBox_1.setItemText(0, QCoreApplication.translate("Dialog", u"E-Wallet", None))
        self.comboBox_1.setItemText(1, QCoreApplication.translate("Dialog", u"Cash", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"JUMLAH UANG KEMBALIAN       :", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"SELESAI", None))
    # retranslateUi

