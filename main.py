from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
class MainGrid(QWidget):
    
    def __init__(self):
        super().__init__()
        
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
        self.changeStyle()

    def changeStyle(self):
        QApplication.setStyle(QStyleFactory.create('Fusion'))

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Transaksi")
        
        pushButton1 = QPushButton()
        pushButton1.setText("Proses")
        openInventory = InventoryWindow()
        pushButton1.clicked.connect(openInventory.show)
        
        layout = QVBoxLayout()
        layout.addWidget(pushButton1)
        layout.addStretch(1)
        '''
        openInvent = InventoryWindow()
         def on_pushButton_clicked():
            openInvent.show()  
        pushButton1.clicked.connect(on_pushButton_clicked)
       
        pushButton1.clicked.connect(openInventory)
        def openInventory():                                             # <===
            w = InventoryWindow()
            w.show()
            w.hide()
        '''
        self.topLeftGroupBox.setLayout(layout)

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Foods")

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        label5 = QLabel(self)
        label6 = QLabel(self)

        picture1 = QPixmap('Assets/foods/Beef Rice Bowl.jpeg')
        picture1.scaled(50,50, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        picture2 = QPixmap('Assets/foods/Chicken Teriyaki Rice Bowl.jpeg')
        picture2.scaled(50,50, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        picture3 = QPixmap('Assets/foods/Chicken Nuget.jpeg')
        picture3.scaled(50,50, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        picture4 = QPixmap('Assets/foods/French Fries.jpeg')
        picture4.scaled(50,50, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        picture5 = QPixmap('Assets/foods/onion rings.jpg')
        picture5.scaled(50,50, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        picture6 = QPixmap('Assets/foods/Sosis Goreng.jpeg')
        picture6.scaled(50,50, Qt.IgnoreAspectRatio, Qt.FastTransformation)

        label1.setPixmap(picture1)
        label2.setPixmap(picture2)
        label3.setPixmap(picture3)
        label4.setPixmap(picture4)
        label5.setPixmap(picture5)
        label6.setPixmap(picture6)

        priceLabel1 = QLabel(self)
        priceLabel2 = QLabel(self)
        priceLabel3 = QLabel(self)
        priceLabel4 = QLabel(self)
        priceLabel5 = QLabel(self)
        priceLabel6 = QLabel(self)
        

        priceLabel1.setText("20.000")
        priceLabel2.setText("15.000")
        priceLabel3.setText("12.000")
        priceLabel4.setText("10.000")
        priceLabel5.setText("11.000")
        priceLabel6.setText("12.000")
        

        priceLabel1.setAlignment(Qt.AlignCenter)
        priceLabel2.setAlignment(Qt.AlignCenter)
        priceLabel3.setAlignment(Qt.AlignCenter)
        priceLabel4.setAlignment(Qt.AlignCenter)
        priceLabel5.setAlignment(Qt.AlignCenter)
        priceLabel6.setAlignment(Qt.AlignCenter)
        

        textLabel1 = QLabel(self)
        textLabel2 = QLabel(self)
        textLabel3 = QLabel(self)
        textLabel4 = QLabel(self)
        textLabel5 = QLabel(self)
        textLabel6 = QLabel(self)

        textLabel1.setText("Beef Rice Bowl")
        textLabel2.setText("Chicken Rice Bowl")
        textLabel3.setText("Chicken Nugget")
        textLabel4.setText("French Fries")
        textLabel5.setText("Onion Rings")
        textLabel6.setText("Sosis Goreng")

        textLabel1.setAlignment(Qt.AlignCenter)
        textLabel2.setAlignment(Qt.AlignCenter)
        textLabel3.setAlignment(Qt.AlignCenter)
        textLabel4.setAlignment(Qt.AlignCenter)
        textLabel5.setAlignment(Qt.AlignCenter)
        textLabel6.setAlignment(Qt.AlignCenter)

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

        layout = QGridLayout()

        layout.addWidget(label1, 0, 0)
        layout.addWidget(label2, 0, 1)
        layout.addWidget(label3, 0, 2)
        layout.addWidget(label4, 4, 0)
        layout.addWidget(label5, 4, 1)
        layout.addWidget(label6, 4, 2)

        layout.addWidget(textLabel1, 1, 0)
        layout.addWidget(textLabel2, 1, 1)
        layout.addWidget(textLabel3, 1, 2)
        layout.addWidget(textLabel4, 5, 0)
        layout.addWidget(textLabel5, 5, 1)
        layout.addWidget(textLabel6, 5, 2)

        layout.addWidget(spinBox1, 3, 0)
        layout.addWidget(spinBox2, 3, 1)
        layout.addWidget(spinBox3, 3, 2)
        layout.addWidget(spinBox4, 7, 0)
        layout.addWidget(spinBox5, 7, 1)
        layout.addWidget(spinBox6, 7, 2)

        layout.addWidget(priceLabel1, 2, 0)
        layout.addWidget(priceLabel2, 2, 1)
        layout.addWidget(priceLabel3, 2, 2)
        layout.addWidget(priceLabel4, 6, 0)
        layout.addWidget(priceLabel5, 6, 1)
        layout.addWidget(priceLabel6, 6, 2)
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

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        label5 = QLabel(self)
        label6 = QLabel(self)
        label7 = QLabel(self)
        label8 = QLabel(self)
        label9 = QLabel(self)

        picture1 = QPixmap('Assets/beverages/Café Espresso.jpg')
        picture1.scaled(50,50, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        picture2 = QPixmap('Assets/beverages/Mocha .jpg')
        picture2.scaled(50,50, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        picture3 = QPixmap('Assets/beverages/Kopi susu gula aren.jpg')
        picture3.scaled(50,50, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        picture4 = QPixmap('Assets/beverages/Thai tea.jpg')
        picture4.scaled(50,50, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        picture5 = QPixmap('Assets/beverages/tea.jpg')
        picture5.scaled(50,50, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        picture6 = QPixmap('Assets/beverages/Chocolatte Milk tea.jpg')
        picture6.scaled(50,50, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        picture7 = QPixmap('Assets/beverages/Vanilla Latte .jpg')
        picture7.scaled(50,50, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        picture8 = QPixmap('Assets/beverages/Taro Latte .jpg')
        picture8.scaled(50,50, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        picture9 = QPixmap('Assets/beverages/air mineral.jpg')
        picture9.scaled(50,50, Qt.IgnoreAspectRatio, Qt.FastTransformation)

        label1.setPixmap(picture1)
        label2.setPixmap(picture2)
        label3.setPixmap(picture3)
        label4.setPixmap(picture4)
        label5.setPixmap(picture5)
        label6.setPixmap(picture6)
        label7.setPixmap(picture7)
        label8.setPixmap(picture8)
        label9.setPixmap(picture9)

        textLabel1 = QLabel(self)
        textLabel2 = QLabel(self)
        textLabel3 = QLabel(self)
        textLabel4 = QLabel(self)
        textLabel5 = QLabel(self)
        textLabel6 = QLabel(self)
        textLabel7 = QLabel(self)
        textLabel8 = QLabel(self)
        textLabel9 = QLabel(self)

        textLabel1.setText("Café Espresso")
        textLabel2.setText("Mocha")
        textLabel3.setText("Kopi susu gula aren")
        textLabel4.setText("Thai tea")
        textLabel5.setText("tea")
        textLabel6.setText("Chocolatte Milk tea")
        textLabel7.setText("Vanilla Latte")
        textLabel8.setText("Taro Latte")
        textLabel9.setText("air mineral")

        textLabel1.setAlignment(Qt.AlignCenter)
        textLabel2.setAlignment(Qt.AlignCenter)
        textLabel3.setAlignment(Qt.AlignCenter)
        textLabel4.setAlignment(Qt.AlignCenter)
        textLabel5.setAlignment(Qt.AlignCenter)
        textLabel6.setAlignment(Qt.AlignCenter)
        textLabel7.setAlignment(Qt.AlignCenter)
        textLabel8.setAlignment(Qt.AlignCenter)
        textLabel9.setAlignment(Qt.AlignCenter)

        priceLabel1 = QLabel(self)
        priceLabel2 = QLabel(self)
        priceLabel3 = QLabel(self)
        priceLabel4 = QLabel(self)
        priceLabel5 = QLabel(self)
        priceLabel6 = QLabel(self)
        priceLabel7 = QLabel(self)
        priceLabel8 = QLabel(self)
        priceLabel9 = QLabel(self)

        priceLabel1.setText("10.000")
        priceLabel2.setText("12.000")
        priceLabel3.setText("8.000")
        priceLabel4.setText("5.000")
        priceLabel5.setText("3.000")
        priceLabel6.setText("6.000")
        priceLabel7.setText("10.000")
        priceLabel8.setText("10.000")
        priceLabel9.setText("3.000")

        priceLabel1.setAlignment(Qt.AlignCenter)
        priceLabel2.setAlignment(Qt.AlignCenter)
        priceLabel3.setAlignment(Qt.AlignCenter)
        priceLabel4.setAlignment(Qt.AlignCenter)
        priceLabel5.setAlignment(Qt.AlignCenter)
        priceLabel6.setAlignment(Qt.AlignCenter)
        priceLabel7.setAlignment(Qt.AlignCenter)
        priceLabel8.setAlignment(Qt.AlignCenter)
        priceLabel9.setAlignment(Qt.AlignCenter)

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

        layout.addWidget(label1, 0, 0)
        layout.addWidget(label2, 0, 1)
        layout.addWidget(label3, 0, 2)
        layout.addWidget(label4, 4, 0)
        layout.addWidget(label5, 4, 1)
        layout.addWidget(label6, 4, 2)
        layout.addWidget(label7, 8, 0)
        layout.addWidget(label8, 8, 1)
        layout.addWidget(label9, 8, 2)

        layout.addWidget(textLabel1, 1, 0)
        layout.addWidget(textLabel2, 1, 1)
        layout.addWidget(textLabel3, 1, 2)
        layout.addWidget(textLabel4, 5, 0)
        layout.addWidget(textLabel5, 5, 1)
        layout.addWidget(textLabel6, 5, 2)
        layout.addWidget(textLabel7, 9, 0)
        layout.addWidget(textLabel8, 9, 1)
        layout.addWidget(textLabel9, 9, 2)

        layout.addWidget(spinBox1, 3, 0)
        layout.addWidget(spinBox2, 3, 1)
        layout.addWidget(spinBox3, 3, 2)
        layout.addWidget(spinBox4, 7, 0)
        layout.addWidget(spinBox5, 7, 1)
        layout.addWidget(spinBox6, 7, 2)
        layout.addWidget(spinBox7, 11, 0)
        layout.addWidget(spinBox8, 11, 1)
        layout.addWidget(spinBox9, 11, 2)

        layout.addWidget(priceLabel1, 2, 0)
        layout.addWidget(priceLabel2, 2, 1)
        layout.addWidget(priceLabel3, 2, 2)
        layout.addWidget(priceLabel4, 6, 0)
        layout.addWidget(priceLabel5, 6, 1)
        layout.addWidget(priceLabel6, 6, 2)
        layout.addWidget(priceLabel7, 10, 0)
        layout.addWidget(priceLabel8, 10, 1)
        layout.addWidget(priceLabel9, 10, 2)
        self.bottomRightGroupBox.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        centralGrid = MainGrid()
        self.setWindowTitle("Cafe Point-Of-Sales")
        self.setCentralWidget(centralGrid)

class InventoryWindow(QWidget):
    def __init__(self):
        super(InventoryWindow, self).__init__()
        self.resize(400, 300)

        # Label
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 400, 300)
        self.label.setText('Sub Window')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:40px')

if __name__ == '__main__':
     app = QApplication([])
     window = MainWindow()
     window.show()
     sys.exit(app.exec_())