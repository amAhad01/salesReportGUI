from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QHBoxLayout, QComboBox, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from connector import connector
from errorm import errorfunc, errorfunc2, errorfunc3
from situation import sit1, sit2, sit3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #setting a title for window
        self.setWindowTitle('Sell Management Dashboard')
        #setting an icon for window
        self.setWindowIcon(QIcon('icons/management.svg'))
        #setting x and y coordinates, length and width of the window
        self.setGeometry(300, 100, 1000, 700)
        graphFrame = QFrame(self)
        graphFrame.setFrameShape(QFrame.Shape.StyledPanel)
        graphFrame.setGeometry(300, 1, 1240, 800)
        layout = QHBoxLayout(graphFrame)
        MyFigure = plt.figure()
        MyCanvas = FigureCanvas(MyFigure)
        layout.addWidget(MyCanvas)
        #creating combobox
        BeginMonth = QComboBox(self)
        EndMonth = QComboBox(self)
        BeginYear = QComboBox(self)
        EndYear = QComboBox(self)
        ChartKind = QComboBox(self)
        BarKind = QComboBox(self)
        Timing = QComboBox(self)
        #Goal = QComboBox(self)
        #setting comboboxes lenght, width and x-y-coordinates
        BeginYear.setGeometry(40, 50, 100, 30)
        EndYear.setGeometry(40, 150, 100, 30)
        BeginMonth.setGeometry(200, 50, 100, 30)
        EndMonth.setGeometry(200, 150, 100, 30)
        ChartKind.setGeometry(100, 200, 150, 30)
        BarKind.setGeometry(100, 250, 150, 30)
        Timing.setGeometry(100, 300, 150, 30)
        #Goal.setGeometry(100, 350, 150, 30)
        years = ['2023', '2024']
        months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        chartkinds = ['Bar', 'Line', 'Pie']
        barkinds = ['Vertical', 'Horizontal']
        evos = ['Monthly', 'Yearly']
        #goals = ['Sells', 'Products', 'Costumers']
        #adding the created lists to the comboboxes list items
        BeginYear.addItems(years)
        EndYear.addItems(years)
        BeginMonth.addItems(months)
        EndMonth.addItems(months)
        ChartKind.addItems(chartkinds)
        BarKind.addItems(barkinds)
        Timing.addItems(evos)
        #Goal.addItems(goals)
        #creating a button
        btn1 = QPushButton('Submit', self)
        #setting an icon for the created button
        btn1.setIcon(QIcon('icons/checkmark.svg'))
        btn1.setGeometry(100, 500, 100, 30)
        #creating labels
        label1 = QLabel('From', self)
        label2 = QLabel('Until', self)
        label3 = QLabel('Month', self)
        label4 = QLabel('Month', self)
        label5 = QLabel('Year', self)
        label6 = QLabel('Year', self)
        label7 = QLabel('Kind of Chart', self)
        label8 = QLabel("Bar's Direction", self)
        label9 = QLabel('Timing', self)
        #label10 = QLabel('Goal', self)
        label1.setGeometry(1, 1, 100, 30)
        #setting a font to 'sanserif' style and the size
        label1.setFont(QFont('Sanserif', 20))
        label3.setGeometry(160, 50, 100, 30)
        label2.setGeometry(1, 100, 100, 30)
        label2.setFont(QFont('Sanserif', 20))
        label4.setGeometry(160, 150, 100, 30)
        label5.setGeometry(1, 50, 100, 30)
        label6.setGeometry(1, 150, 100, 30)
        label7.setGeometry(1, 200, 100, 30)
        label8.setGeometry(1, 250, 100, 30)
        label9.setGeometry(1, 300, 100, 30)
        #label10.setGeometry(1, 350, 150, 30)

        #creating a function for checking if its a problem in the inputs
        #and calling a proper function according to the inputs 
        def handler():
            #getting the current text of the comboboxes and converting them to integer
            y1 = int(BeginYear.currentText())
            y2 = int(EndYear.currentText())
            m1 = int(BeginMonth.currentText())
            m2 = int(EndMonth.currentText())
            #calling the connector function for accessing the database
            curs = connector()
            kob = BarKind.currentText()
            koc = ChartKind.currentText()
            #g = Goal.currentText()
            t = Timing.currentText()
            #clearing the current chart then making space for the new chart
            MyFigure.clear()
            #partitioning the chart means that only one chart can be shown
            ax = MyFigure.add_subplot(111)
            if t == 'Monthly':
                if y1 > y2:
                    errorfunc()
                elif y1 == y2:
                    if m1 > m2:
                        errorfunc2()
                    elif m1 < m2:
                        sit1(y1, m1, m2, curs, kob, MyFigure, ax, koc)
                    else:
                        errorfunc3()
                else:
                    sit2(y1, y2, m1, m2, curs, kob, MyFigure, ax, koc)
            else:
                if y1 > y2:
                    errorfunc()
                else:
                    sit3(y1, y2, curs, kob, MyFigure, ax, koc)
        #when the button is clicked, the handler() is being called
        btn1.clicked.connect(handler)
        #ChartKind.currentTextChanged.connect(comboshandler1)
        #Timing.currentTextChanged.connect(comboshandler2)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
