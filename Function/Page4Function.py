from threading import Thread
from Function.DiscordBlockDet import GetBlockDET
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Function.Picture import GetPicFunction
import cv2
import os
import sys
import time
import Function.Foundation as Fun
import pyautogui
import time
import win32gui
import pyperclip

#外放舔關內容
#1.該模式為接外放
#2.接外放有兩種模式可以選擇，1T mode 及 貢獻mode
#3.請預先測試過隊伍沒問題在使用腳本
#4.貢獻mode 可以指定貢獻度 若達到目標則跳出主畫面
#7.腳本自動 會自動執行並檢測指定技能是否可以使用。
#8.如果遇到關卡滿載，處理以下事件
#8-1.救援數最大3，每10秒點擊一次reload並點擊外放關卡，檢測一次關卡數量
#8-2.若總數量達到最大視窗出現，返回主畫面並回收所有獎勵直到沒有領取按鈕出現。

class RunFunction4:
     #===================================debug
    def debugLog(self):
        print("StopFunction: ", Fun.StopFunction)
        print("Function1FightCount: ", Fun.Function1FightCount)
        print("TypeSelect: ", Fun.TypeSelect)
        print("RunFlag: ", Fun.RunFlag)    
    #====================================function
    def RunFGscrept(self):
        x = GetPicFunction()
        if Fun.RunFlag == False:
            Fun.RunFlag = True
            Fun.StopFunction = False
            if Fun.Function1FightCount == 0:
                #無限迴圈
                def GBFloop():
                    while Fun.StopFunction == False:
                        try:
                            print(f"test run run run: 無上限") 
                            time.sleep(1)
                            print("stopfuntion=",Fun.StopFunction)
                            print("Function1FightCount=",Fun.Function1FightCount)
                            Fun.RunFlag = False
                        except:
                            print("Function fail")
                            Fun.RunFlag = False
            else:
                #有限迴圈
                def GBFloop():
                    for i in range(Fun.Function1FightCount):
                        try:
                            C=i+1
                            TC=Fun.Function1FightCount                            
                            print(f"test run run run: {C}/{TC}")
                            Picture=cv2.imread("./systemdata/img/systemimg/Arcarum.PNG")
                            Flag = True
                            while(Flag):
                                lox,loy = x.PicDet(Picture)
                                if any(lox):
                                    pyautogui.click(lox+50,loy+55)
                                    Flag=False
                                    time.sleep(0.5)
                                else:
                                    pyautogui.scroll(-12)
                            x.GoHome()

                            time.sleep(1)

                            print("stopfunction=",Fun.StopFunction)
                            print("Function1FightCount=",Fun.Function1FightCount)
                            if Fun.StopFunction:
                                break
                        except:
                            print("Function fail")
                            Fun.RunFlag = False
                    Fun.RunFlag = False
        
            global functionthread
            functionthread = Thread(target=GBFloop)
            functionthread.setDaemon(True)
            functionthread.start()
        
   