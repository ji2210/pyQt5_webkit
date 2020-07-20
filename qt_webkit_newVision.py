# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:39:43 2020

@author: j-3
"""


##os.chdir(os.path.dirname(os.path.abspath(__file__)))
##
##返回脚本绝对路径
#os.path.abspath(__file__)
##返回脚本上级路径
#os.path.dirname(os.path.abspath(__file__))
##返回脚本上两层目录路径
#os.chdir(os.path.dirname(os.path.abspath(__file__)))
##
import sys,os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtCore 

from apscheduler.schedulers.background import BackgroundScheduler


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args ,**kwargs)
        self.setWindowTitle('My ADs')
        self.setWindowIcon(QIcon('favicon.ico'))
        self.resize(900,600)
        self.show()
        
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)#让窗口置顶
        
        url = 'https://www.baidu.com'
        self.browser = QWebEngineView()
        self.browser.load(QUrl(url))
        self.setCentralWidget(self.browser)
        
        self.timer = QTimer(self)
        self.timer.start(10000) #单位是毫秒，5000是5秒
        self.timer.timeout.connect(self.close) #self.closes 是终止程序
        
           
        
        

if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

     
     
     
    
#    schedule = BackgroundScheduler()
#    schedule.add_job(
#                     func=app.exec_(),
#                     trigger='interval',
#                     seconds=5, #minutes
#                     )
#    schedule.start()
        