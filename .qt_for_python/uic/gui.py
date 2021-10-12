# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\User\Desktop\Coding\qf205-stock-moving\gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background-color: rgb(39, 50, 61);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.fileNameInput = QtWidgets.QLineEdit(self.frame_4)
        self.fileNameInput.setMinimumSize(QtCore.QSize(0, 30))
        self.fileNameInput.setStyleSheet("background-color: rgb(46, 60, 74);\n"
"border-color: rgb(46, 60, 74);\n"
"color: rgb(193,196,200);\n"
"")
        self.fileNameInput.setObjectName("fileNameInput")
        self.gridLayout.addWidget(self.fileNameInput, 0, 1, 1, 1)
        self.dateRangeInput = QtWidgets.QLineEdit(self.frame_4)
        self.dateRangeInput.setMinimumSize(QtCore.QSize(0, 30))
        self.dateRangeInput.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.dateRangeInput.setStyleSheet("background-color: rgb(46, 60, 74);\n"
"color: rgb(193,196,200);\n"
"")
        self.dateRangeInput.setReadOnly(True)
        self.dateRangeInput.setObjectName("dateRangeInput")
        self.gridLayout.addWidget(self.dateRangeInput, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.errorMessage = QtWidgets.QLabel(self.frame_4)
        self.errorMessage.setStyleSheet("color: rgb(255, 0, 0);")
        self.errorMessage.setText("")
        self.errorMessage.setObjectName("errorMessage")
        self.gridLayout.addWidget(self.errorMessage, 3, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame_4)
        self.loadCsvButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadCsvButton.sizePolicy().hasHeightForWidth())
        self.loadCsvButton.setSizePolicy(sizePolicy)
        self.loadCsvButton.setMinimumSize(QtCore.QSize(100, 0))
        self.loadCsvButton.setMaximumSize(QtCore.QSize(16777215, 65))
        self.loadCsvButton.setStyleSheet("background-color: rgb(46, 60, 74);\n"
"color: rgb(193,196,200);\n"
"font-weight: bold;\n"
"")
        self.loadCsvButton.setObjectName("loadCsvButton")
        self.horizontalLayout.addWidget(self.loadCsvButton)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.startDateLabel = QtWidgets.QLabel(self.frame_6)
        self.startDateLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.startDateLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.startDateLabel.setStyleSheet("color: rgb(193,196,200);\n"
"font-weight: bold;\n"
"")
        self.startDateLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.startDateLabel.setObjectName("startDateLabel")
        self.gridLayout_3.addWidget(self.startDateLabel, 0, 0, 1, 1)
        self.endDateLabel = QtWidgets.QLabel(self.frame_6)
        self.endDateLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.endDateLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.endDateLabel.setStyleSheet("color: rgb(193,196,200);\n"
"font-weight: bold;\n"
"")
        self.endDateLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.endDateLabel.setObjectName("endDateLabel")
        self.gridLayout_3.addWidget(self.endDateLabel, 1, 0, 1, 1)
        self.startDateCombo = QtWidgets.QComboBox(self.frame_6)
        self.startDateCombo.setMinimumSize(QtCore.QSize(100, 30))
        self.startDateCombo.setStyleSheet("background-color: rgb(46, 60, 74);\n"
"color: rgb(193,196,200);\n"
"")
        self.startDateCombo.setObjectName("startDateCombo")
        self.gridLayout_3.addWidget(self.startDateCombo, 0, 1, 1, 1)
        self.endDateCombo = QtWidgets.QComboBox(self.frame_6)
        self.endDateCombo.setMinimumSize(QtCore.QSize(70, 30))
        self.endDateCombo.setStyleSheet("background-color: rgb(46, 60, 74);\n"
"color: rgb(193,196,200);\n"
"")
        self.endDateCombo.setObjectName("endDateCombo")
        self.gridLayout_3.addWidget(self.endDateCombo, 1, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sma2Input = QtWidgets.QLineEdit(self.frame_5)
        self.sma2Input.setMinimumSize(QtCore.QSize(0, 30))
        self.sma2Input.setStyleSheet("background-color: rgb(46, 60, 74);\n"
"color: rgb(193,196,200);\n"
"")
        self.sma2Input.setObjectName("sma2Input")
        self.gridLayout_2.addWidget(self.sma2Input, 1, 1, 1, 1)
        self.sma1Input = QtWidgets.QLineEdit(self.frame_5)
        self.sma1Input.setMinimumSize(QtCore.QSize(0, 30))
        self.sma1Input.setStyleSheet("background-color: rgb(46, 60, 74);\n"
"color: rgb(193,196,200);\n"
"")
        self.sma1Input.setObjectName("sma1Input")
        self.gridLayout_2.addWidget(self.sma1Input, 0, 1, 1, 1)
        self.sma1CheckBox = QtWidgets.QCheckBox(self.frame_5)
        self.sma1CheckBox.setStyleSheet("color: rgb(193,196,200);\n"
"font-weight: bold;\n"
"")
        self.sma1CheckBox.setObjectName("sma1CheckBox")
        self.gridLayout_2.addWidget(self.sma1CheckBox, 0, 0, 1, 1)
        self.sma2CheckBox = QtWidgets.QCheckBox(self.frame_5)
        self.sma2CheckBox.setStyleSheet("color: rgb(193,196,200);\n"
"font-weight: bold;\n"
"")
        self.sma2CheckBox.setObjectName("sma2CheckBox")
        self.gridLayout_2.addWidget(self.sma2CheckBox, 1, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.updateButton = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateButton.sizePolicy().hasHeightForWidth())
        self.updateButton.setSizePolicy(sizePolicy)
        self.updateButton.setMinimumSize(QtCore.QSize(100, 0))
        self.updateButton.setMaximumSize(QtCore.QSize(16777215, 65))
        self.updateButton.setStyleSheet("background-color: rgb(46, 60, 74);\n"
"color: rgb(193,196,200);\n"
"font-weight: bold;\n"
"")
        self.updateButton.setText("Update Window")
        self.updateButton.setObjectName("updateButton")
        self.horizontalLayout_2.addWidget(self.updateButton)
        self.verticalLayout.addWidget(self.frame_2)
        self.MplWidget = MplWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MplWidget.sizePolicy().hasHeightForWidth())
        self.MplWidget.setSizePolicy(sizePolicy)
        self.MplWidget.setMinimumSize(QtCore.QSize(500, 300))
        self.MplWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MplWidget.setObjectName("MplWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.MplWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addWidget(self.MplWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stock Chart & Moving Average Crossover"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#c1c4c8;\">Date Range</span></p></body></html>"))
        self.fileNameInput.setPlaceholderText(_translate("MainWindow", "Enter the full file path to your CSV file"))
        self.dateRangeInput.setPlaceholderText(_translate("MainWindow", "The date range of your CSV files will be shown here"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#c1c4c8;\">File Path</span></p></body></html>"))
        self.loadCsvButton.setText(_translate("MainWindow", "Load CSV"))
        self.startDateLabel.setText(_translate("MainWindow", "Start Date"))
        self.endDateLabel.setText(_translate("MainWindow", "End Date"))
        self.sma2Input.setText(_translate("MainWindow", "50"))
        self.sma1Input.setText(_translate("MainWindow", "15"))
        self.sma1CheckBox.setText(_translate("MainWindow", "SMA-1 (<= 252)"))
        self.sma2CheckBox.setText(_translate("MainWindow", "SMA-2 (<= 252)"))

from mplwidget import MplWidget
