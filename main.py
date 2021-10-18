import SMA
from datetime import datetime
import csv
import random
import datetime as dt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import matplotlib
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
matplotlib.use('Qt5Agg')

qtCreatorFile = "gui.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

### NOTES FOR REFERENCE ###
'''
Object names:
fileNameInput
dateRangeInput
loadCsvButton
startDateCombo
endDateCombo
sma1CheckBox
sma2CheckBox
sma1Input
sma2Input
updateButton

Grab text e.g. self.fileNameInput.text()
Grab checkbox e.g. self.sma1CheckBox.isChecked()
Add item to combo box (dropdown) e.g. self.startDateCombo.addItem('11/10/2020')
Get text from combo box e.g. self.startDateCombo.currentText()
'''


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.window_width, self.window_height = 1200, 800
        self.setMinimumSize(self.window_width, self.window_height)

        # Connect buttons
        self.loadCsvButton.clicked.connect(self.loadCsv)
        self.updateButton.clicked.connect(self.updateChart)

        # Setup state change detection for the SMA-1 and SMA-2 check for live updating to chart
        self.sma1CheckBox.stateChanged.connect(self.updateChart)
        self.sma2CheckBox.stateChanged.connect(self.updateChart)

        # Data from CSV parsing
        self.y = pd.DataFrame()
        self.x = pd.DataFrame()
        self.dateRange = []

        self.show()

    # When the Update Window button is clicked
    def updateChart(self):

        # df.rename(columns={'Adj Close': 'Adj_Close'}, inplace=True)

        sma1, sma2, crossBuy, crossSell = SMA.getSMAPlots(
            self.y, int(self.sma1Input.text()), int(self.sma2Input.text()))

        sma1, self.x = SMA.balanceLengths(
            sma1, self.x)

        sma2, self.x = SMA.balanceLengths(
            sma2, self.x)

        crossBuy, self.x = SMA.balanceLengths(
            crossBuy, self.x)

        crossSell, self.x = SMA.balanceLengths(
            crossSell, self.x)

        # retrieve the current index of the date selected
        startIdx = self.startDateCombo.currentIndex()
        endIdx = self.endDateCombo.currentIndex()

        # check that the end date is larger than the start date
        if endIdx < startIdx:
            self.errorMessage.setText('End date should be later than start date.')
        
        else:
            # remove error message
            self.errorMessage.setText('')

            # slice the required data based on date range
            xDataToPlot = self.dateRange[startIdx:endIdx+1]
            yDataToPlot = self.y[startIdx:endIdx+1]
            sma1 = sma1[startIdx:endIdx+1]
            sma2 = sma2[startIdx:endIdx+1]
            crossBuy = crossBuy[startIdx:endIdx+1]
            crossSell = crossSell[startIdx:endIdx+1]

            # crossBuy = [0]*(len(self.x) - len(crossBuy)) + crossBuy
            # crossSell = [0]*(len(self.x) - len(crossSell)) + crossSell

            # sma1 and sma2 are already the same size
            # crossBuy is an array of 0s and 1s, 1 is the point to buy
            # crossSell is an array of 0s and -1s, -1 is the point to sell
            # print(crossBuy, crossSell)

            # rolling_mean = df.Adj_Close.rolling(window=15).mean()
            # rolling_mean2 = df.Adj_Close.rolling(window=50).mean()

            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(xDataToPlot, yDataToPlot)

            if self.sma1CheckBox.isChecked():
                self.MplWidget.canvas.axes.plot(
                    xDataToPlot, sma1, label='15 Day SMA', color='orange')  # placeholder

            if self.sma2CheckBox.isChecked():
                self.MplWidget.canvas.axes.plot(
                    xDataToPlot, sma2, label='50 Day SMA', color='magenta')  # placeholder

            if self.sma1CheckBox.isChecked() and self.sma2CheckBox.isChecked():
                # self.MplWidget.canvas.axes.plot(xDataToPlot, crossBuy)
                # self.MplWidget.canvas.axes.plot(xDataToPlot, crossSell)
                buy_idx = [i for i, e in enumerate(crossBuy) if e == 1]
                for i in buy_idx:
                    self.MplWidget.canvas.axes.plot(
                        xDataToPlot[i], sma1[i], 'go')

                sell_idx = [i for i, e in enumerate(crossSell) if e == -1]
                for i in sell_idx:
                    self.MplWidget.canvas.axes.plot(
                        xDataToPlot[i], sma1[i], 'ro')

            # chart legends
            self.MplWidget.canvas.axes.legend(('Close', self.sma1Input.text(
            ) + 'd', self.sma2Input.text() + 'd'), loc='upper right')

            # chart title
            self.MplWidget.canvas.axes.set_title('Stock Price (' + self.startDateCombo.currentText() + ' - ' + self.endDateCombo.currentText() + ')')

            # axis labels
            self.MplWidget.canvas.axes.set_xlabel('Dates')
            self.MplWidget.canvas.axes.set_ylabel('Prices')

            # formate date on x-axis
            fmt_month = mdates.MonthLocator()
            
            self.MplWidget.canvas.axes.xaxis.set_minor_locator(fmt_month)
            self.MplWidget.canvas.axes.xaxis.set_major_formatter(mdates.DateFormatter('%m-%Y'))

            self.MplWidget.canvas.draw()

    # Parse csv and pass data into x data and y data and plot initiate graph
    def loadCsv(self):

        try:
            if self.fileNameInput.text():
                fileName = self.fileNameInput.text()
                df = pd.read_csv(fileName)
                y = df["Adj Close"]
                x = df["Date"]
                
                startDate = x.iloc[0]
                endDate = x.iloc[-1]
                
                self.dateRangeInput.setText(str(startDate) + ' to ' + str(endDate))
                
                self.startDateCombo.addItems(x)
                self.endDateCombo.addItems(x)
                self.endDateCombo.setCurrentIndex(len(x) - 1)

                # convert date string to datetime
                self.dateRange = [dt.datetime.strptime(date, '%Y-%m-%d').date() for date in x]
                
                self.y = y
                self.x = x

                # update chart if there is a valid file
                self.updateChart()
            else:
                self.errorMessage.setText("Please input a file path before clicking the 'Load CSV' button.")
        except:
            self.errorMessage.setText("Error loading the file. Please input the file path again.")
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.setWindowIcon(QIcon('icon.png'))
    main.setWindowTitle('Stock Chart & Moving Average Crossover')
    main.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("Closing Window...")
