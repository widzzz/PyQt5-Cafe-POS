# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TransactionakNkbg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
import datetime
import sqlite3
import sys

connection = sqlite3.connect("projects.db")
cursor = connection.cursor()

class Ui_transaction(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 480)
        self.label_1 = QLabel(Dialog)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(250, 70, 171, 31))
        self.label_1.setStyleSheet(u"FONT-SIZE:20PT;;\n"
"")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(68, 240, 161, 16))
        self.paymentLineEdit = QLineEdit(Dialog)
        self.paymentLineEdit.setObjectName(u"paymentLineEdit")
        self.paymentLineEdit.setGeometry(QRect(230, 240, 281, 20))
        self.paymentLineEdit.setText("0")
        self.paymentLineEdit.textChanged.connect(self.show_change)
        self.comboBox_1 = QComboBox(Dialog)
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.setObjectName(u"comboBox_1")
        self.comboBox_1.setGeometry(QRect(70, 160, 91, 22))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 310, 171, 16))
        self.changeValue = QLabel(Dialog)
        self.changeValue.setObjectName(u"changeValue")
        self.changeValue.setGeometry(QRect(230, 310, 281, 51))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.changeValue.setFont(font)
        self.changeValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.changeValue.setWordWrap(True)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 400, 131, 51))
        font1 = QFont()
        font1.setPointSize(14)
        self.pushButton.setFont(font1)
        #
        self.pushButton.clicked.connect(self.onClicked_pushButton)
        #
        self.totalLineEdit = QLineEdit(Dialog)
        self.totalLineEdit.setObjectName(u"totalLineEdit")
        self.totalLineEdit.setGeometry(QRect(230, 210, 281, 20))
        self.totalLineEdit.setText("0")
        self.totalLineEdit.textChanged.connect(self.show_change)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 210, 161, 16))

        #
        #

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def show_change(self):

        value = int(self.paymentLineEdit.text()) - int(self.totalLineEdit.text())
  
        # setting value of spin box to the label
        self.changeValue.setText(str(value))

    def onClicked_pushButton(self):
        total = self.totalLineEdit.text()
        method = self.comboBox_1.currentText()
        timedate = datetime.datetime.now()

        cursor.execute("""INSERT INTO history (datetime,transactionValue,method)
                        VALUES(?,?,?);
                        """, [str(timedate),str(total),str(method)])
        connection.commit()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_1.setText(QCoreApplication.translate("Dialog", u"PEMBAYARAN", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"JUMLAH UANG YANG DIBAYAR :", None))
        self.comboBox_1.setItemText(0, QCoreApplication.translate("Dialog", u"E-Wallet", None))
        self.comboBox_1.setItemText(1, QCoreApplication.translate("Dialog", u"Cash", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"JUMLAH UANG KEMBALIAN       :", None))
        self.changeValue.setText("")
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Selesai", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Total :", None))
    # retranslateUi

class Exit(QWidget):
    app = QApplication(sys.argv)
    app.quit()