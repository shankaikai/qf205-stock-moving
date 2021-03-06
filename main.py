import SMA
from datetime import datetime
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import matplotlib.dates as mdates
import pandas as pd
matplotlib.use('Qt5Agg')

qtCreatorFile = "gui.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

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

            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(xDataToPlot, yDataToPlot)

            if self.sma1CheckBox.isChecked():
                self.MplWidget.canvas.axes.plot(
                    xDataToPlot, sma1, label= self.sma1Input.text() + ' Day SMA', color='orange') 

            if self.sma2CheckBox.isChecked():
                self.MplWidget.canvas.axes.plot(
                    xDataToPlot, sma2, label= self.sma2Input.text() + ' Day SMA', color='magenta')  
                
            if self.sma1CheckBox.isChecked() and self.sma2CheckBox.isChecked():
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
                self.dateRange = [datetime.strptime(date, '%Y-%m-%d').date() for date in x]
                
                self.y = y
                self.x = x

                # update chart if there is a valid file
                self.updateChart()

                # remove error message if any
                self.errorMessage.setText("")

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
