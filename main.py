import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout
from PyQt5 import uic
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import random

qtCreatorFile = "gui.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

'''
Object names:
fileNameInput
dateRangeInput
loadCsvButton
startDateInput
endDateInput
sma1CheckBox
sma2CheckBox
sma1Input
sma2Input
updateButton

Grab text e.g. self.fileNameInput.text()
Grab checkbox e.g. self.sma1CheckBox.isChecked()
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
        self.y = [random.randint(0, 300) for i in range(5)] # placeholder
        self.x = ["Jan", "Feb", "Mar", "April", "May"] # placeholder
        
    
    # When the Update Window button is clicked
    def updateChart(self):
        sma1 = [random.randint(0, 300) for i in range(5)] # placeholder
        sma2 = [random.randint(0, 300) for i in range(5)] # placeholder
        
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(self.x, self.y)

        if self.sma1CheckBox.isChecked():
            self.MplWidget.canvas.axes.plot(self.x, sma1) # placeholder
        
        if self.sma2CheckBox.isChecked():
            self.MplWidget.canvas.axes.plot(self.x, sma2) # placeholder

        self.MplWidget.canvas.axes.legend(('Close', self.sma1Input.text() + 'd', self.sma2Input.text() + 'd'), loc = 'upper right')
        print(self.sma2Input.text())
        self.MplWidget.canvas.axes.set_title('Placeholder')
        self.MplWidget.canvas.draw()
    
    # Parse csv and pass data into x data and y data and plot initiate graph
    def loadCsv(self):
        self.updateChart()
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    try: 
        sys.exit(app.exec_())
    except SystemExit:
        print("Closing Window...")

