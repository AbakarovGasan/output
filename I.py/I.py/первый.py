#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(s):
        super().__init__()
        s.initUI()
        
    def initUI(s):
        s.setGeometry(300, 300, 300, 220)
        s.setWindowTitle('Icon')
        s.setWindowIcon(QIcon('web.png'))        
    
        s.show()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    o = Example()
    sys.exit(app.exec_())  



