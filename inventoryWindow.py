# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inventoryzYawRs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3
import sys

connection = sqlite3.connect("projects.db")
cursor = connection.cursor()

class Ui_inventory(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 569)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(210, 10, 421, 546))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_text7 = QLabel(self.layoutWidget)
        self.label_text7.setObjectName(u"label_text7")

        self.gridLayout_2.addWidget(self.label_text7, 9, 0, 1, 1)

        self.spinBox = QSpinBox(self.layoutWidget)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout_2.addWidget(self.spinBox, 4, 0, 1, 1)

        self.label_pict8 = QLabel(self.layoutWidget)
        self.label_pict8.setObjectName(u"label_pict8")
        self.label_pict8.setPixmap(QPixmap(u"Assets/foods/French Fries.jpeg"))
        self.label_pict8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_pict8, 8, 1, 1, 1)

        self.label_pict3 = QLabel(self.layoutWidget)
        self.label_pict3.setObjectName(u"label_pict3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_pict3.sizePolicy().hasHeightForWidth())
        self.label_pict3.setSizePolicy(sizePolicy)
        self.label_pict3.setPixmap(QPixmap(u"Assets/beverages/Chocolatte Milk tea.jpg"))
        self.label_pict3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_pict3, 1, 2, 1, 1)

        self.label_text8 = QLabel(self.layoutWidget)
        self.label_text8.setObjectName(u"label_text8")

        self.gridLayout_2.addWidget(self.label_text8, 9, 1, 1, 1)

        self.spinBox_9 = QSpinBox(self.layoutWidget)
        self.spinBox_9.setObjectName(u"spinBox_9")

        self.gridLayout_2.addWidget(self.spinBox_9, 11, 2, 1, 1)

        self.label_text6 = QLabel(self.layoutWidget)
        self.label_text6.setObjectName(u"label_text6")

        self.gridLayout_2.addWidget(self.label_text6, 6, 2, 1, 1)

        self.spinBox_10 = QSpinBox(self.layoutWidget)
        self.spinBox_10.setObjectName(u"spinBox_10")

        self.gridLayout_2.addWidget(self.spinBox_10, 15, 0, 1, 1)

        self.label_text5 = QLabel(self.layoutWidget)
        self.label_text5.setObjectName(u"label_text5")
        self.label_text5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_text5, 6, 1, 1, 1)

        self.label_pic5 = QLabel(self.layoutWidget)
        self.label_pic5.setObjectName(u"label_pic5")
        self.label_pic5.setPixmap(QPixmap(u"Assets/beverages/Thai tea.jpg"))
        self.label_pic5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_pic5, 5, 1, 1, 1)

        self.spinBox_3 = QSpinBox(self.layoutWidget)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.gridLayout_2.addWidget(self.spinBox_3, 4, 2, 1, 1)

        self.label_text12 = QLabel(self.layoutWidget)
        self.label_text12.setObjectName(u"label_text12")

        self.gridLayout_2.addWidget(self.label_text12, 14, 2, 1, 1)

        self.label_text10 = QLabel(self.layoutWidget)
        self.label_text10.setObjectName(u"label_text10")

        self.gridLayout_2.addWidget(self.label_text10, 14, 0, 1, 1)

        self.spinBox_4 = QSpinBox(self.layoutWidget)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.gridLayout_2.addWidget(self.spinBox_4, 7, 0, 1, 1)

        self.label_pict2 = QLabel(self.layoutWidget)
        self.label_pict2.setObjectName(u"label_pict2")
        self.label_pict2.setPixmap(QPixmap(u"Assets/beverages/Caf\u00e9 Espresso.jpg"))
        self.label_pict2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_pict2, 1, 1, 1, 1)

        self.spinBox_11 = QSpinBox(self.layoutWidget)
        self.spinBox_11.setObjectName(u"spinBox_11")

        self.gridLayout_2.addWidget(self.spinBox_11, 15, 1, 1, 1)

        self.label_pict12 = QLabel(self.layoutWidget)
        self.label_pict12.setObjectName(u"label_pict12")
        self.label_pict12.setPixmap(QPixmap(u"Assets/foods/Chicken Teriyaki Rice Bowl.jpeg"))
        self.label_pict12.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_pict12, 13, 2, 1, 1)

        self.spinBox_2 = QSpinBox(self.layoutWidget)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.gridLayout_2.addWidget(self.spinBox_2, 4, 1, 1, 1)

        self.label_pict11 = QLabel(self.layoutWidget)
        self.label_pict11.setObjectName(u"label_pict11")
        self.label_pict11.setPixmap(QPixmap(u"Assets/foods/onion rings.jpg"))
        self.label_pict11.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_pict11, 13, 1, 1, 1)

        self.label_text2 = QLabel(self.layoutWidget)
        self.label_text2.setObjectName(u"label_text2")
        sizePolicy.setHeightForWidth(self.label_text2.sizePolicy().hasHeightForWidth())
        self.label_text2.setSizePolicy(sizePolicy)
        self.label_text2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_text2, 3, 1, 1, 1)

        self.spinBox_8 = QSpinBox(self.layoutWidget)
        self.spinBox_8.setObjectName(u"spinBox_8")

        self.gridLayout_2.addWidget(self.spinBox_8, 11, 1, 1, 1)

        self.spinBox_7 = QSpinBox(self.layoutWidget)
        self.spinBox_7.setObjectName(u"spinBox_7")

        self.gridLayout_2.addWidget(self.spinBox_7, 11, 0, 1, 1)

        self.label_text11 = QLabel(self.layoutWidget)
        self.label_text11.setObjectName(u"label_text11")

        self.gridLayout_2.addWidget(self.label_text11, 14, 1, 1, 1)

        self.label_text9 = QLabel(self.layoutWidget)
        self.label_text9.setObjectName(u"label_text9")

        self.gridLayout_2.addWidget(self.label_text9, 9, 2, 1, 1)

        self.label_pict6 = QLabel(self.layoutWidget)
        self.label_pict6.setObjectName(u"label_pict6")
        self.label_pict6.setPixmap(QPixmap(u"Assets/beverages/Mocha .jpg"))
        self.label_pict6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_pict6, 5, 2, 1, 1)

        self.label_pict4 = QLabel(self.layoutWidget)
        self.label_pict4.setObjectName(u"label_pict4")
        self.label_pict4.setPixmap(QPixmap(u"Assets/beverages/tea.jpg"))
        self.label_pict4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_pict4, 5, 0, 1, 1)

        self.label_pict10 = QLabel(self.layoutWidget)
        self.label_pict10.setObjectName(u"label_pict10")
        self.label_pict10.setPixmap(QPixmap(u"Assets/foods/Sosis Goreng.jpeg"))
        self.label_pict10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_pict10, 13, 0, 1, 1)

        self.label_pict9 = QLabel(self.layoutWidget)
        self.label_pict9.setObjectName(u"label_pict9")
        self.label_pict9.setPixmap(QPixmap(u"Assets/foods/Chicken Nuget.jpeg"))
        self.label_pict9.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_pict9, 8, 2, 1, 1)

        self.spinBox_6 = QSpinBox(self.layoutWidget)
        self.spinBox_6.setObjectName(u"spinBox_6")

        self.gridLayout_2.addWidget(self.spinBox_6, 7, 2, 1, 1)

        self.label_text4 = QLabel(self.layoutWidget)
        self.label_text4.setObjectName(u"label_text4")
        self.label_text4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_text4, 6, 0, 1, 1)

        self.spinBox_5 = QSpinBox(self.layoutWidget)
        self.spinBox_5.setObjectName(u"spinBox_5")

        self.gridLayout_2.addWidget(self.spinBox_5, 7, 1, 1, 1)

        self.spinBox_12 = QSpinBox(self.layoutWidget)
        self.spinBox_12.setObjectName(u"spinBox_12")

        self.gridLayout_2.addWidget(self.spinBox_12, 15, 2, 1, 1)

        self.label_pict7 = QLabel(self.layoutWidget)
        self.label_pict7.setObjectName(u"label_pict7")
        self.label_pict7.setPixmap(QPixmap(u"Assets/foods/Beef Rice Bowl.jpeg"))
        self.label_pict7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_pict7, 8, 0, 1, 1)

        self.label_text3 = QLabel(self.layoutWidget)
        self.label_text3.setObjectName(u"label_text3")

        self.gridLayout_2.addWidget(self.label_text3, 3, 2, 1, 1)

        self.label_text1 = QLabel(self.layoutWidget)
        self.label_text1.setObjectName(u"label_text1")
        sizePolicy.setHeightForWidth(self.label_text1.sizePolicy().hasHeightForWidth())
        self.label_text1.setSizePolicy(sizePolicy)
        self.label_text1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_text1, 3, 0, 1, 1)

        self.label_pict1 = QLabel(self.layoutWidget)
        self.label_pict1.setObjectName(u"label_pict1")
        self.label_pict1.setPixmap(QPixmap(u"Assets/beverages/air mineral.jpg"))
        self.label_pict1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_pict1, 1, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 230, 131, 51))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 270, 111, 91))
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setWordWrap(True)

        ##
        sqlite_select_query_stock = """SELECT stock FROM inventory"""
        cursor.execute(sqlite_select_query_stock)

        ## F*CK LOOPING
        t = cursor.fetchone()
        t = sum(t)
        self.value_spinBox = int(t)
        t = cursor.fetchone()
        t = sum(t)
        self.value_spinBox2 = int(t)
        t = cursor.fetchone()
        t = sum(t)
        self.value_spinBox3 = int(t)
        t = cursor.fetchone()
        t = sum(t)
        self.value_spinBox4 = int(t)
        t = cursor.fetchone()
        t = sum(t)
        self.value_spinBox5 = int(t)
        t = cursor.fetchone()
        t = sum(t)
        self.value_spinBox6 = int(t)
        t = cursor.fetchone()
        t = sum(t)
        self.value_spinBox7 = int(t)
        t = cursor.fetchone()
        t = sum(t)
        self.value_spinBox8 = int(t)
        t = cursor.fetchone()
        t = sum(t)
        self.value_spinBox9 = int(t)
        t = cursor.fetchone()
        t = sum(t)
        self.value_spinBox10 = int(t)
        t = cursor.fetchone()
        t = sum(t)
        self.value_spinBox11 = int(t)
        t = cursor.fetchone()
        t = sum(t)
        self.value_spinBox12 = int(t)

        self.spinBox.setValue(self.value_spinBox)
        self.spinBox_2.setValue(self.value_spinBox2)
        self.spinBox_3.setValue(self.value_spinBox3)
        self.spinBox_4.setValue(self.value_spinBox4)
        self.spinBox_5.setValue(self.value_spinBox5)
        self.spinBox_6.setValue(self.value_spinBox6)
        self.spinBox_7.setValue(self.value_spinBox7)
        self.spinBox_8.setValue(self.value_spinBox8)
        self.spinBox_9.setValue(self.value_spinBox9)
        self.spinBox_10.setValue(self.value_spinBox10)
        self.spinBox_11.setValue(self.value_spinBox11)
        self.spinBox_12.setValue(self.value_spinBox12)
        
        self.spinBox.valueChanged.connect(self.updateQueryspin1)
        self.spinBox_2.valueChanged.connect(self.updateQueryspin2)
        self.spinBox_3.valueChanged.connect(self.updateQueryspin3)
        self.spinBox_4.valueChanged.connect(self.updateQueryspin4)
        self.spinBox_5.valueChanged.connect(self.updateQueryspin5)
        self.spinBox_6.valueChanged.connect(self.updateQueryspin6)
        self.spinBox_7.valueChanged.connect(self.updateQueryspin7)
        self.spinBox_8.valueChanged.connect(self.updateQueryspin8)
        self.spinBox_9.valueChanged.connect(self.updateQueryspin9)
        self.spinBox_10.valueChanged.connect(self.updateQueryspin10)
        self.spinBox_11.valueChanged.connect(self.updateQueryspin11)
        self.spinBox_12.valueChanged.connect(self.updateQueryspin12)

        self.connection = sqlite3.connect("projects.db")
        self.cursor = self.connection.cursor()
        
        ##

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def updateQueryspin1(self, value):
        cursor.execute("""UPDATE inventory SET stock = ? WHERE name=1""", [str(value)])
        connection.commit()
    
    def updateQueryspin2(self, value):
        cursor.execute("""UPDATE inventory SET stock = ? WHERE name=2""", [str(value)])
        connection.commit()
    
    def updateQueryspin3(self, value):
        cursor.execute("""UPDATE inventory SET stock = ? WHERE name=3""", [str(value)])
        connection.commit()

    def updateQueryspin4(self, value):
        cursor.execute("""UPDATE inventory SET stock = ? WHERE name=4""", [str(value)])
        connection.commit()

    def updateQueryspin5(self, value):
        cursor.execute("""UPDATE inventory SET stock = ? WHERE name=5""", [str(value)])
        connection.commit()

    def updateQueryspin6(self, value):
        cursor.execute("""UPDATE inventory SET stock = ? WHERE name=6""", [str(value)])
        connection.commit()

    def updateQueryspin7(self, value):
        cursor.execute("""UPDATE inventory SET stock = ? WHERE name=7""", [str(value)])
        connection.commit()

    def updateQueryspin8(self, value):
        cursor.execute("""UPDATE inventory SET stock = ? WHERE name=8""", [str(value)])
        connection.commit()

    def updateQueryspin9(self, value):
        cursor.execute("""UPDATE inventory SET stock = ? WHERE name=9""", [str(value)])
        connection.commit()

    def updateQueryspin10(self, value):
        cursor.execute("""UPDATE inventory SET stock = ? WHERE name=10""", [str(value)])
        connection.commit()

    def updateQueryspin11(self, value):
        cursor.execute("""UPDATE inventory SET stock = ? WHERE name=11""", [str(value)])
        connection.commit()

    def updateQueryspin12(self, value):
        cursor.execute("""UPDATE inventory SET stock = ? WHERE name=12""", [str(value)])
        connection.commit()

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_text7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Rice Bowl</p><p align=\"center\">23.000</p></body></html>", None))
        self.label_pict8.setText("")
        self.label_pict3.setText("")
        self.label_text8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">French Fries</p><p align=\"center\">12.000</p></body></html>", None))
        self.label_text6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Mocha</p><p align=\"center\">20.000</p></body></html>", None))
        self.label_text5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Thai Tea</p><p>17.000</p></body></html>", None))
        self.label_pic5.setText("")
        self.label_text12.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Chicken Teriyaki</p><p align=\"center\">20.000</p></body></html>", None))
        self.label_text10.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Sosis Goreng</p><p align=\"center\">13.000</p></body></html>", None))
        self.label_pict2.setText("")
        self.label_pict12.setText("")
        self.label_pict11.setText("")
        self.label_text2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Espresso</p><p>20.000</p></body></html>", None))
        self.label_text11.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Onion Rings</p><p align=\"center\">15.000</p></body></html>", None))
        self.label_text9.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Chicken Nugget</p><p align=\"center\">14.000</p></body></html>", None))
        self.label_pict6.setText("")
        self.label_pict4.setText("")
        self.label_pict10.setText("")
        self.label_pict9.setText("")
        self.label_text4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Ice Tea</p><p>15.000</p></body></html>", None))
        self.label_pict7.setText("")
        self.label_text3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Boba Milk Tea</p><p align=\"center\">19.000</p></body></html>", None))
        self.label_text1.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Air Mineral</p><p>8.000</p></body></html>", None))
        self.label_pict1.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Inventori</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Anda diharuskan<span style=\" font-weight:600;\"> keluar</span> dari aplikasi untuk menyimpan stok barang</p></body></html>", None))
    # retranslateUi

class InventoryWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.ui = Ui_inventory()
        self.ui.setupUi(self)

        self.changeStyle()
        self.show()

    def changeStyle(self):
        QApplication.setStyle(QStyleFactory.create('Fusion'))