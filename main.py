from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomLeftTabWidget()
        self.createBottomRightGroupBox()

        topLayout = QHBoxLayout()
        topLayout.addStretch(1)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomLeftTabWidget, 2, 0)
        mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Cafe Point-Of-Sales")
        self.changeStyle('Windows')

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create('Fusion'))

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Transaksi")

        pushButton1 = QPushButton("Proses")

        layout = QVBoxLayout()
        layout.addWidget(pushButton1)
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)    

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Foods")

        spinBox1 = QSpinBox(self.topRightGroupBox)
        spinBox1.setValue(0)
        spinBox2 = QSpinBox(self.topRightGroupBox)
        spinBox2.setValue(0)
        spinBox3 = QSpinBox(self.topRightGroupBox)
        spinBox3.setValue(0)
        spinBox4 = QSpinBox(self.topRightGroupBox)
        spinBox4.setValue(0)
        spinBox5 = QSpinBox(self.topRightGroupBox)
        spinBox5.setValue(0)
        spinBox6 = QSpinBox(self.topRightGroupBox)
        spinBox6.setValue(0)
        spinBox7 = QSpinBox(self.topRightGroupBox)
        spinBox7.setValue(0)
        spinBox8 = QSpinBox(self.topRightGroupBox)
        spinBox8.setValue(0)
        spinBox9 = QSpinBox(self.topRightGroupBox)
        spinBox9.setValue(0)

        layout = QGridLayout()

        layout.addWidget(spinBox1, 0, 0)

        layout.addWidget(spinBox2, 0, 1)
        layout.addWidget(spinBox3, 0, 2)
        layout.addWidget(spinBox4, 1, 0)
        layout.addWidget(spinBox5, 1, 1)
        layout.addWidget(spinBox6, 1, 2)
        layout.addWidget(spinBox7, 2, 0)
        layout.addWidget(spinBox8, 2, 1)
        layout.addWidget(spinBox9, 2, 2)
        self.topRightGroupBox.setLayout(layout)

    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QTabWidget()
        self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Ignored)

        tab1 = QWidget()
        tableWidget = QTableWidget(10, 10)

        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.addWidget(tableWidget)
        tab1.setLayout(tab1hbox)

        tab2 = QWidget()
        textEdit = QTextEdit()

        textEdit.setPlainText("Pusing coyyyy...")

        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(textEdit)
        tab2.setLayout(tab2hbox)

        self.bottomLeftTabWidget.addTab(tab1, "&Table")
        self.bottomLeftTabWidget.addTab(tab2, "Text &Edit")

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("Beverages")

    #    label1 = QLabel(self)
    #    picture1 = QPixmap('Café Espresso.jpg')
    #    picture1.scaled(50,50, Qt.IgnoreAspectRatio, Qt.FastTransformation)
    #    label1.setPixmap(picture1)

        spinBox1 = QSpinBox(self.bottomRightGroupBox)
        spinBox1.setValue(0)
        spinBox2 = QSpinBox(self.bottomRightGroupBox)
        spinBox2.setValue(0)
        spinBox3 = QSpinBox(self.bottomRightGroupBox)
        spinBox3.setValue(0)
        spinBox4 = QSpinBox(self.bottomRightGroupBox)
        spinBox4.setValue(0)
        spinBox5 = QSpinBox(self.bottomRightGroupBox)
        spinBox5.setValue(0)
        spinBox6 = QSpinBox(self.bottomRightGroupBox)
        spinBox6.setValue(0)
        spinBox7 = QSpinBox(self.bottomRightGroupBox)
        spinBox7.setValue(0)
        spinBox8 = QSpinBox(self.bottomRightGroupBox)
        spinBox8.setValue(0)
        spinBox9 = QSpinBox(self.bottomRightGroupBox)
        spinBox9.setValue(0)

        layout = QGridLayout()

        layout.addWidget(spinBox1, 0, 0)
   #     layout.addWidget(label1, 0, 0)
        layout.addWidget(spinBox2, 0, 1)
        layout.addWidget(spinBox3, 0, 2)
        layout.addWidget(spinBox4, 1, 0)
        layout.addWidget(spinBox5, 1, 1)
        layout.addWidget(spinBox6, 1, 2)
        layout.addWidget(spinBox7, 2, 0)
        layout.addWidget(spinBox8, 2, 1)
        layout.addWidget(spinBox9, 2, 2)
        self.bottomRightGroupBox.setLayout(layout)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec()) 