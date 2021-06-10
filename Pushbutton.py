import serial
from PyQt5 import QtWidgets
from GUI_Pushbutton import Ui_MainWindow
from PyQt5.QtGui import *

ser = serial.Serial('COM3', 9600)


def Anticlockwise():
    if ser.isOpen():
        ser.write("A".encode('utf-8'))
        
def Off():
    if ser.isOpen():
        ser.write("O".encode('utf-8'))

def Clockwise():
    if ser.isOpen():
        ser.write("C".encode('utf-8'))

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

ui.Anticlockwise_pushButton.setStyleSheet("font: bold;background-color: rgb(146, 249, 255); border-radius: 10px; font-size:20px;")
ui.Anticlockwise_pushButton.setGeometry(50,100,200,50)
ui.Anticlockwise_pushButton.clicked.connect(Anticlockwise)

ui.Off_pushButton.setStyleSheet("font: bold;background-color: red; border-radius: 10px; font-size:20px;")
ui.Off_pushButton.setGeometry(300,100,200,50)
ui.Off_pushButton.clicked.connect(Off)

ui.Cloclwise_pushButton.setStyleSheet("font: bold;background-color: rgb(246, 214, 187); border-radius: 10px; font-size:20px;")
ui.Cloclwise_pushButton.clicked.connect(Clockwise)
ui.Cloclwise_pushButton.setGeometry(550,100,200,50)
MainWindow.show()
sys.exit(app.exec_())
