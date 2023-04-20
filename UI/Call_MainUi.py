from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.Homepage.ui_MainUI import Ui_GBF_MAIN
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
import systemdata.icon.ICON
from Funtion.Setfuntion import *
import Funtion.Foundation
import json

from win32gui import *

from ctypes import windll, byref
from ctypes.wintypes import HWND, POINT
import time
import sys
import win32gui
import os
import pyautogui as pag

class MainPageWindow(QtWidgets.QMainWindow,Ui_GBF_MAIN):
    
    chooseSignal = pyqtSignal(str)    

    def __init__(self,parent=None):
        super(MainPageWindow, self).__init__(parent)        
        self.setupUi(self)
        self.initUiindex()
        self.initbuttonUI()
        self.defaultPage()#預設為page1
        self.GetScreenFunc()

    def initUiindex(self):
        titleicon = QtGui.QIcon()
        titleicon.addPixmap(QtGui.QPixmap(":/ICON.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Helpicon = QtGui.QIcon()
        Saveicon = QtGui.QIcon()
        Loadicon = QtGui.QIcon()
        Exiticon = QtGui.QIcon()
        self.setWindowIcon(titleicon)
        self.setWindowTitle('自動人 我的超人')#title
        Helpicon.addPixmap(QtGui.QPixmap(":/Heip.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionHelp.setIcon(Helpicon)#help
        Saveicon.addPixmap(QtGui.QPixmap(":/Save.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionAdd.setIcon(Saveicon)#help
        Loadicon.addPixmap(QtGui.QPixmap(":/Load.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionOpen.setIcon(Loadicon)#help
        Exiticon.addPixmap(QtGui.QPixmap(":/door.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionEXIT.setIcon(Exiticon)#help

    def initbuttonUI(self):
        self.actionHelp.triggered.connect(self.showDialog)
        self.Funtionlist.clicked.connect(self.showDialog)
        self.DebugButton.clicked.connect(self.showDialog)
        self.Screptrun_2.clicked.connect(self.showDialog)
        self.FuncStopButton.clicked.connect(self.showDialog)
        self.AllstopButton.clicked.connect(self.showDialog)
        self.SetButton_2.clicked.connect(self.showDialog)
        self.Times_spinBox_2.valueChanged.connect(self.showDialog)
        #self.changebutton.clicked.connect(self.showDialog)
    
    def showDialog(self):
        sender = self.sender()
        if sender == self.actionHelp:
            self.chooseSignal.emit('Help')        
        if  sender == self.Funtionlist:
            self.change_Page()
        if sender == self.DebugButton:           
            self.AppDataCheck()
            debugLog()
        if sender == self.Screptrun_2:
            RunFGscrept()
        if sender == self.FuncStopButton or sender == self.AllstopButton:
            Funtion.Foundation.StopFunction = True
        if sender == self.SetButton_2:
            self.SaveFile()
        if sender == self.Times_spinBox_2:            
            self.settingtext()

    def defaultPage(self):
        self.Page1.show() 
        self.Page2.hide()
        self.Page3.hide()

    def change_Page(self):
        text = self.Funtionlist.currentItem().text()
        if text == "轉世":
            self.Page1.show() 
            self.Page2.hide()
            self.Page3.hide()
            self.Info_broswer.setText("轉世")
        if text == "方陣":
            self.Page1.hide()
            self.Page2.show() 
            self.Page3.hide()
            self.Info_broswer.setText("方陣")
        if text == "方陣速刷":
            self.Page1.hide()
            self.Page2.hide() 
            self.Page3.show()
            self.Info_broswer.setText("方陣速刷")

    def settingtext(self):        
        Funtion.Foundation.IntFightCount = self.Times_spinBox_2.value()
        if Funtion.Foundation.IntFightCount == 0:
            self.label_10.setText("Set 無上限")
        else:
            self.label_10.setText("Set :"+str(Funtion.Foundation.IntFightCount))

    def SaveFile(self):
        Funtion.Foundation.IntFightCount = self.Times_spinBox_2.value()

        Savedata = {}
        Savedata['funtion'] = {'IntFightCount': Funtion.Foundation.IntFightCount, 'TypeSelect': 0}

        with open('systemdata/datasave/data.json', 'w') as datafile:
            json.dump(Savedata,datafile)
        self.label_10.setText("set成功")
        print("set成功")

    def AppDataCheck(self):        
        try:
            windowsgetIndex = self.WindowsComboBox.currentIndex()
            windowsgetstr = self.WindowsComboBox.currentText()

            if windowsgetIndex == 0:
                HWNS = win32gui.FindWindow(None, "グランブルーファンタジー - Google Chrome")
                left, top, right, bottom = win32gui.GetWindowRect(HWNS)
                posStr1 = str(left).rjust(4)+','+str(top).rjust(4)+','+str(right).rjust(4)+','+str(bottom).rjust(4)
                print("AppPos: ", posStr1)
            else:
                HWNS = win32gui.FindWindow(None, windowsgetstr)
                left, top, right, bottom = win32gui.GetWindowRect(HWNS)
                posStr1 = str(left).rjust(4)+','+str(top).rjust(4)+','+str(right).rjust(4)+','+str(bottom).rjust(4)
                print("AppPos: ", posStr1)
        except:
            def Mbox(title, text, style):
                return windll.user32.MessageBoxW(0, text, title, style)
            Mbox('沒有找到視窗', '請選擇GBF的視窗標題', 0)
        
        print("#------------------------------------")
        print("windowsgetIndex: ", windowsgetIndex)
        print("windowsgetstr: ", windowsgetstr)   
        


    def GetScreenFunc(self):
        titles = set()
        def foo(hwnd,mouse):
            if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
                titles.add(GetWindowText(hwnd))
        EnumWindows(foo, 0)
        lt = [t for t in titles if t]
        lt.sort()
        print("#Sortting Windows-------------")
        for t in lt:
            if t == "グランブルーファンタジー - Google Chrome":
                self.WindowsComboBox.addItem(t)
                self.WindowsComboBox.setCurrentText(t)
            else:
                self.WindowsComboBox.addItem(t)
            print (t)
        

       


    
