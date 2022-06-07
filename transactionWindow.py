# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TransactionOYlkKn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from genericpath import exists
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3
import datetime
import sys

if exists("projects.db"):
    connection = sqlite3.connect("projects.db")
    cursor = connection.cursor()

class Ui_transaction(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 480)
        self.label_1 = QLabel(Dialog)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(230, 40, 171, 31))
        self.label_1.setStyleSheet(u"FONT-SIZE:20PT;;\n""")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 200, 161, 16))
        self.paymentLineEdit = QLineEdit(Dialog)
        self.paymentLineEdit.setObjectName(u"paymentLineEdit")
        self.paymentLineEdit.setGeometry(QRect(80, 220, 221, 20))
        self.paymentLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.comboBox_1 = QComboBox(Dialog)
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.setObjectName(u"comboBox_1")
        self.comboBox_1.setGeometry(QRect(80, 110, 91, 22))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 260, 151, 16))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.changeValue = QLabel(Dialog)
        self.changeValue.setObjectName(u"changeValue")
        self.changeValue.setGeometry(QRect(360, 280, 181, 41))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.changeValue.setFont(font)
        self.changeValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.changeValue.setWordWrap(True)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 370, 301, 51))
        font1 = QFont()
        font1.setPointSize(14)
        self.pushButton.setFont(font1)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 150, 161, 16))
        self.totalLabel = QLabel(Dialog)
        self.totalLabel.setObjectName(u"totalLabel")
        self.totalLabel.setGeometry(QRect(80, 170, 151, 21))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.totalLabel.setFont(font2)
        self.plainTextEdit = QPlainTextEdit(Dialog)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(80, 270, 221, 51))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 250, 161, 16))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 90, 161, 16))

        #
        #
        self.importTotal()
        self.pushButton.clicked.connect(self.onClicked_pushButton)
        self.paymentLineEdit.textChanged.connect(self.show_change)
        self.onlyInt = QIntValidator()
        self.paymentLineEdit.setValidator(self.onlyInt)
        #
        #

        self.retranslateUi(Dialog)
        self.totalLabel.setText(str(self.totalValue))

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    #
    #
    def show_change(self):
        payment = self.paymentLineEdit.text()
        if payment == '':
            payment = 0

        value = int(payment) - int(self.totalValue)
  
        self.changeValue.setText(str(value))

    def importTotal(self):
        self.totalValue = cursor.execute("SELECT * FROM temp")
        t = cursor.fetchone()
        self.totalValue = sum(t)

    def onClicked_pushButton(self):
        total = self.totalLabel.text()
        method = self.comboBox_1.currentText()
        timedate = datetime.datetime.now()
        note = self.plainTextEdit.toPlainText()

        cursor.execute("""INSERT INTO history (datetime,transactionValue,method,note)
                        VALUES(?,?,?,?);
                        """, [str(timedate),str(total),str(method),str(note)])
        connection.commit()
    #
    #

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_1.setText(QCoreApplication.translate("Dialog", u"PEMBAYARAN", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Jumlah uang yang dibayar :", None))
        self.paymentLineEdit.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.comboBox_1.setItemText(0, QCoreApplication.translate("Dialog", u"Cash", None))
        self.comboBox_1.setItemText(1, QCoreApplication.translate("Dialog", u"E-Wallet", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"Jumlah uang kembalian :", None))
        # self.changeValue.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Simpan Transaksi", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Total :", None))
        self.totalLabel.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Note :", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Metode :", None))
    # retranslateUi

class TransactionWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.ui = Ui_transaction()
        self.ui.setupUi(self)

        self.changeStyle()
        self.show()

    def changeStyle(self):
        QApplication.setStyle(QStyleFactory.create('Fusion'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TransactionWindow()
    window.show()
    app.exec()