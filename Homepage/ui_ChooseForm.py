# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ChooseForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChooseForm(object):
    def setupUi(self, ChooseForm):
        ChooseForm.setObjectName("ChooseForm")
        ChooseForm.resize(612, 389)
        self.gridLayout = QtWidgets.QGridLayout(ChooseForm)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(ChooseForm)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(ChooseForm)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(ChooseForm)
        self.treeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setIndentation(20)
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setAnimated(False)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.gridLayout_2.addWidget(self.treeWidget, 0, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.retranslateUi(ChooseForm)
        QtCore.QMetaObject.connectSlotsByName(ChooseForm)

    def retranslateUi(self, ChooseForm):
        _translate = QtCore.QCoreApplication.translate
        ChooseForm.setWindowTitle(_translate("ChooseForm", "選擇執行單元"))
        self.pushButton.setText(_translate("ChooseForm", "確認"))
        self.pushButton_2.setText(_translate("ChooseForm", "取消"))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, _translate("ChooseForm", "執行單元"))
        self.treeWidget.headerItem().setText(1, _translate("ChooseForm", "功能說明"))
        self.treeWidget.headerItem().setText(2, _translate("ChooseForm", "功能設定1"))
        self.treeWidget.headerItem().setText(3, _translate("ChooseForm", "功能設定2"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("ChooseForm", "刷轉世"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("ChooseForm", "執行轉世腳本"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("ChooseForm", "刷方陣"))
        self.treeWidget.topLevelItem(1).setText(1, _translate("ChooseForm", "執行方陣腳本"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
