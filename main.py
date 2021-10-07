import SMA
from datetime import datetime
import csv
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import matplotlib
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
        self.df = pd.read_csv("CSV files\PLTR.csv")  # placeholder
        self.closeData = self.df["Close"]  # placeholder
        self.datesData = self.df["Date"]   # placeholder
        self.y = self.closeData
        self.x = self.datesData
        # self.y = [random.randint(0, 300) for i in range(5)]  # placeholder
        # self.x = ["Jan", "Feb", "Mar", "April", "May"]  # placeholder

        self.show()

    # When the Update Window button is clicked
    def updateChart(self):

        # TODO: assign close data to self.closeData

        # df.rename(columns={'Adj Close': 'Adj_Close'}, inplace=True)

        sma1, sma2, crossBuy, crossSell = SMA.getSMAPlots(
            self.closeData, int(self.sma1Input.text()), int(self.sma2Input.text()))

        sma1, self.x = SMA.balanceLengths(
            sma1, self.x)

        sma2, self.x = SMA.balanceLengths(
            sma2, self.x)

        crossBuy, self.x = SMA.balanceLengths(
            crossBuy, self.x)

        crossSell, self.x = SMA.balanceLengths(
            crossSell, self.x)

        print("lengths", len(sma1), len(sma2), len(self.x), len(self.y))

        # crossBuy = [0]*(len(self.x) - len(crossBuy)) + crossBuy
        # crossSell = [0]*(len(self.x) - len(crossSell)) + crossSell

        # sma1 and sma2 are already the same size
        # crossBuy is an array of 0s and 1s, 1 is the point to buy
        # crossSell is an array of 0s and -1s, -1 is the point to sell
        # print(crossBuy, crossSell)

        # rolling_mean = df.Adj_Close.rolling(window=15).mean()
        # rolling_mean2 = df.Adj_Close.rolling(window=50).mean()

        # TODO: put sma1, sma2, crossBuy, crossSell into graph

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(self.x, self.y)

        if self.sma1CheckBox.isChecked():
            self.MplWidget.canvas.axes.plot(
                self.x, sma1, label='15 Day SMA', color='orange')  # placeholder

        if self.sma2CheckBox.isChecked():
            self.MplWidget.canvas.axes.plot(
                self.x, sma2, label='50 Day SMA', color='magenta')  # placeholder

        if self.sma1CheckBox.isChecked() and self.sma2CheckBox.isChecked():
            self.MplWidget.canvas.axes.plot(self.x, crossBuy)
            self.MplWidget.canvas.axes.plot(self.x, crossSell)
            buy_idx = [i for i, e in enumerate(crossBuy) if e == 1]
            for i in buy_idx:
                self.MplWidget.canvas.axes.plot(
                    self.x[i], sma1[i], 'go')

            sell_idx = [i for i, e in enumerate(crossSell) if e == -1]
            for i in sell_idx:
                self.MplWidget.canvas.axes.plot(
                    self.x[i], sma1[i], 'ro')

        self.MplWidget.canvas.axes.legend(('Close', self.sma1Input.text(
        ) + 'd', self.sma2Input.text() + 'd'), loc='upper right')
        print(self.sma2Input.text())
        self.MplWidget.canvas.axes.set_title('Placeholder')
        self.MplWidget.canvas.draw()

    # Parse csv and pass data into x data and y data and plot initiate graph
    def loadCsv(self):

        fileName = self.fileNameInput.text()
        y, x = [], []  # Data for y and x
        with open(fileName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue

                y.append(float(row[5]))
                x.append(row[0])

        if self.dateRangeInput.text():
            dateRange = self.dateRangeInput.text().split(' to ')
            if dateRange[0] in x:
                startIndex = x.index(dateRange[0])
            # else: do comparison
            if dateRange[1] in x:
                endIndex = x.index(dateRange[1])
                # else: do comparison
            x = x[startIndex:endIndex + 1]
            y = y[startIndex:endIndex + 1]

        self.y = y
        self.x = x
        print(x)
        print(y)

        # TODO: Set the start and end date of the CSV
        self.dateRangeInput.setText('insert date here')  # placeholder

        # TODO: Populate startDateCombo and endDateCombo
        self.startDateCombo.addItem('date')

        self.updateChart()


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
