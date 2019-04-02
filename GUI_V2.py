import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
import time
class Second(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        self.setGeometry(150, 150, 1750, 700)
        self.title = 'Statistic Visualization'
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        helpMenu = mainMenu.addMenu('&Help')
        self.home()

    def home(self):
        self.main = QtWidgets.QWidget(self)
        self.setWindowTitle(self.title)
        self.createFormGroupBox1()
        self.createFormGroupBox2()
        self.layout = QtWidgets.QHBoxLayout(self.main)
        self.layout.addWidget(self.formGroupBox1)
        self.layout.addWidget(self.formGroupBox2)
        self.setCentralWidget(self.main)
        self.show()
        self.update()

    def createFormGroupBox1(self):
        self.formGroupBox1 = QtWidgets.QGroupBox("Description")
        self.reference = QtWidgets.QLabel()
        referencepic = QPixmap('Disscription.JPG')
        self.reference.setPixmap(referencepic)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.reference)
        self.formGroupBox1.setLayout(layout)

    def createFormGroupBox2(self):
        self.formGroupBox2 = QtWidgets.QGroupBox("Figure")
class Third(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Third, self).__init__(parent)
        self.setGeometry(150, 150, 1750, 700)
        self.title = 'Data quality'
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        helpMenu = mainMenu.addMenu('&Help')
        self.home()

    def home(self):
        self.main = QtWidgets.QWidget(self)
        self.setWindowTitle(self.title)
        self.createFormGroupBox1()
        self.createFormGroupBox2()
        self.layout = QtWidgets.QHBoxLayout(self.main)
        self.layout.addWidget(self.formGroupBox1)
        self.layout.addWidget(self.formGroupBox2)
        self.setCentralWidget(self.main)
        self.show()
        self.update()

    def createFormGroupBox1(self):
        self.formGroupBox1 = QtWidgets.QGroupBox("Description")
        self.reference = QtWidgets.QLabel()
        referencepic = QPixmap('Disscription.JPG')
        self.reference.setPixmap(referencepic)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.reference)
        self.formGroupBox1.setLayout(layout)

    def createFormGroupBox2(self):
        self.formGroupBox2 = QtWidgets.QGroupBox("Figure")
class SVMdialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SVMdialog, self).__init__(parent)
        self.setGeometry(150, 150, 1750, 700)
        self.title = 'Support vector Machine'
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        helpMenu = mainMenu.addMenu('&Help')
        self.home()

    def home(self):
        self.main = QtWidgets.QWidget(self)
        self.setWindowTitle(self.title)
        self.createFormGroupBox1()
        self.createFormGroupBox2()
        self.layout = QtWidgets.QHBoxLayout(self.main)
        self.layout.addWidget(self.formGroupBox1)
        self.layout.addWidget(self.formGroupBox2)
        self.setCentralWidget(self.main)
        self.show()
        self.update()

    def createFormGroupBox1(self):
        self.formGroupBox1 = QtWidgets.QGroupBox("Description")
        self.reference = QtWidgets.QLabel()
        referencepic = QPixmap('Disscription.JPG')
        self.reference.setPixmap(referencepic)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.reference)
        self.formGroupBox1.setLayout(layout)

    def createFormGroupBox2(self):
        self.formGroupBox2 = QtWidgets.QGroupBox("Figure")
class LRdialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LRdialog, self).__init__(parent)
        self.setGeometry(150, 150, 1750, 700)
        self.title = 'Logistic Regression'
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        helpMenu = mainMenu.addMenu('&Help')
        self.home()

    def home(self):
        self.main = QtWidgets.QWidget(self)
        self.setWindowTitle(self.title)
        self.createFormGroupBox1()
        self.createFormGroupBox2()
        self.layout = QtWidgets.QHBoxLayout(self.main)
        self.layout.addWidget(self.formGroupBox1)
        self.layout.addWidget(self.formGroupBox2)
        self.setCentralWidget(self.main)
        self.show()
        self.update()

    def createFormGroupBox1(self):
        self.formGroupBox1 = QtWidgets.QGroupBox("Description")
        self.reference = QtWidgets.QLabel()
        referencepic = QPixmap('Disscription.JPG')
        self.reference.setPixmap(referencepic)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.reference)
        self.formGroupBox1.setLayout(layout)

    def createFormGroupBox2(self):
        self.formGroupBox2 = QtWidgets.QGroupBox("Figure")
class KNNdialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(KNNdialog, self).__init__(parent)
        self.setGeometry(150, 150, 1750, 700)
        self.title = 'K nearest neighboring'
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        helpMenu = mainMenu.addMenu('&Help')
        self.home()

    def home(self):
        self.main = QtWidgets.QWidget(self)
        self.setWindowTitle(self.title)
        self.createFormGroupBox1()
        self.createFormGroupBox2()
        self.layout = QtWidgets.QHBoxLayout(self.main)
        self.layout.addWidget(self.formGroupBox1)
        self.layout.addWidget(self.formGroupBox2)
        self.setCentralWidget(self.main)
        self.show()
        self.update()

    def createFormGroupBox1(self):
        self.formGroupBox1 = QtWidgets.QGroupBox("Description")
        self.reference = QtWidgets.QLabel()
        referencepic = QPixmap('Disscription.JPG')
        self.reference.setPixmap(referencepic)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.reference)
        self.formGroupBox1.setLayout(layout)

    def createFormGroupBox2(self):
        self.formGroupBox2 = QtWidgets.QGroupBox("Figure")
class DTdialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(DTdialog, self).__init__(parent)
        self.setGeometry(150, 150, 1750, 700)
        self.title = 'Decision Tree'
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        helpMenu = mainMenu.addMenu('&Help')
        self.home()

    def home(self):
        self.main = QtWidgets.QWidget(self)
        self.setWindowTitle(self.title)
        self.createFormGroupBox1()
        self.createFormGroupBox2()
        self.layout = QtWidgets.QHBoxLayout(self.main)
        self.layout.addWidget(self.formGroupBox1)
        self.layout.addWidget(self.formGroupBox2)
        self.setCentralWidget(self.main)
        self.show()
        self.update()

    def createFormGroupBox1(self):
        self.formGroupBox1 = QtWidgets.QGroupBox("Description")
        self.reference = QtWidgets.QLabel()
        referencepic = QPixmap('Disscription.JPG')
        self.reference.setPixmap(referencepic)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.reference)
        self.formGroupBox1.setLayout(layout)

    def createFormGroupBox2(self):
        self.formGroupBox2 = QtWidgets.QGroupBox("Figure")
class NBdialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(NBdialog, self).__init__(parent)
        self.setGeometry(150, 150, 1750, 700)
        self.title = 'Naive bayes'
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        helpMenu = mainMenu.addMenu('&Help')
        self.home()

    def home(self):
        self.main = QtWidgets.QWidget(self)
        self.setWindowTitle(self.title)
        self.createFormGroupBox1()
        self.createFormGroupBox2()
        self.layout = QtWidgets.QHBoxLayout(self.main)
        self.layout.addWidget(self.formGroupBox1)
        self.layout.addWidget(self.formGroupBox2)
        self.setCentralWidget(self.main)
        self.show()
        self.update()

    def createFormGroupBox1(self):
        self.formGroupBox1 = QtWidgets.QGroupBox("Description")
        self.reference = QtWidgets.QLabel()
        referencepic = QPixmap('Disscription.JPG')
        self.reference.setPixmap(referencepic)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.reference)
        self.formGroupBox1.setLayout(layout)

    def createFormGroupBox2(self):
        self.formGroupBox2 = QtWidgets.QGroupBox("Figure")
class HSLdialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(HSLdialog, self).__init__(parent)
        self.setGeometry(150, 150, 1750, 700)
        self.title = 'Hybrid supervised learning'
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        helpMenu = mainMenu.addMenu('&Help')
        self.home()

    def home(self):
        self.main = QtWidgets.QWidget(self)
        self.setWindowTitle(self.title)
        self.createFormGroupBox1()
        self.createFormGroupBox2()
        self.layout = QtWidgets.QHBoxLayout(self.main)
        self.layout.addWidget(self.formGroupBox1)
        self.layout.addWidget(self.formGroupBox2)
        self.setCentralWidget(self.main)
        self.show()
        self.update()

    def createFormGroupBox1(self):
        self.formGroupBox1 = QtWidgets.QGroupBox("Description")
        self.reference = QtWidgets.QLabel()
        referencepic = QPixmap('Disscription.JPG')
        self.reference.setPixmap(referencepic)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.reference)
        self.formGroupBox1.setLayout(layout)

    def createFormGroupBox2(self):
        self.formGroupBox2 = QtWidgets.QGroupBox("Figure")
class CPDdialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CPDdialog, self).__init__(parent)
        self.setGeometry(150, 150, 1750, 700)
        self.title = 'Change point detection'
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        helpMenu = mainMenu.addMenu('&Help')
        self.home()

    def home(self):
        self.main = QtWidgets.QWidget(self)
        self.setWindowTitle(self.title)
        self.createFormGroupBox1()
        self.createFormGroupBox2()
        self.layout = QtWidgets.QHBoxLayout(self.main)
        self.layout.addWidget(self.formGroupBox1)
        self.layout.addWidget(self.formGroupBox2)
        self.setCentralWidget(self.main)
        self.show()
        self.update()

    def createFormGroupBox1(self):
        self.formGroupBox1 = QtWidgets.QGroupBox("Description")
        self.reference = QtWidgets.QLabel()
        referencepic = QPixmap('Disscription.JPG')
        self.reference.setPixmap(referencepic)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.reference)
        self.formGroupBox1.setLayout(layout)

    def createFormGroupBox2(self):
        self.formGroupBox2 = QtWidgets.QGroupBox("Figure")
class PCAdialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(PCAdialog, self).__init__(parent)
        self.setGeometry(150, 150, 1750, 700)
        self.title = 'PCA (visualization'
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        helpMenu = mainMenu.addMenu('&Help')
        self.home()

    def home(self):
        self.main = QtWidgets.QWidget(self)
        self.setWindowTitle(self.title)
        self.createFormGroupBox1()
        self.createFormGroupBox2()
        self.layout = QtWidgets.QHBoxLayout(self.main)
        self.layout.addWidget(self.formGroupBox1)
        self.layout.addWidget(self.formGroupBox2)
        self.setCentralWidget(self.main)
        self.show()
        self.update()

    def createFormGroupBox1(self):
        self.formGroupBox1 = QtWidgets.QGroupBox("Description")
        self.reference = QtWidgets.QLabel()
        referencepic = QPixmap('Disscription.JPG')
        self.reference.setPixmap(referencepic)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.reference)
        self.formGroupBox1.setLayout(layout)

    def createFormGroupBox2(self):
        self.formGroupBox2 = QtWidgets.QGroupBox("Figure")
class CETdialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CETdialog, self).__init__(parent)
        self.setGeometry(150, 150, 1750, 700)
        self.title = 'Clustering for event type'
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        helpMenu = mainMenu.addMenu('&Help')
        self.home()

    def home(self):
        self.main = QtWidgets.QWidget(self)
        self.setWindowTitle(self.title)
        self.createFormGroupBox1()
        self.createFormGroupBox2()
        self.layout = QtWidgets.QHBoxLayout(self.main)
        self.layout.addWidget(self.formGroupBox1)
        self.layout.addWidget(self.formGroupBox2)
        self.setCentralWidget(self.main)
        self.show()
        self.update()

    def createFormGroupBox1(self):
        self.formGroupBox1 = QtWidgets.QGroupBox("Description")
        self.reference = QtWidgets.QLabel()
        referencepic = QPixmap('Disscription.JPG')
        self.reference.setPixmap(referencepic)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.reference)
        self.formGroupBox1.setLayout(layout)

    def createFormGroupBox2(self):
        self.formGroupBox2 = QtWidgets.QGroupBox("Figure")
class CELdialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CELdialog, self).__init__(parent)
        self.setGeometry(150, 150, 1750, 700)
        self.title = 'Clustering for event location'
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        helpMenu = mainMenu.addMenu('&Help')
        self.home()

    def home(self):
        self.main = QtWidgets.QWidget(self)
        self.setWindowTitle(self.title)
        self.createFormGroupBox1()
        self.createFormGroupBox2()
        self.layout = QtWidgets.QHBoxLayout(self.main)
        self.layout.addWidget(self.formGroupBox1)
        self.layout.addWidget(self.formGroupBox2)
        self.setCentralWidget(self.main)
        self.show()
        self.update()

    def createFormGroupBox1(self):
        self.formGroupBox1 = QtWidgets.QGroupBox("Description")
        self.reference = QtWidgets.QLabel()
        referencepic = QPixmap('Disscription.JPG')
        self.reference.setPixmap(referencepic)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.reference)
        self.formGroupBox1.setLayout(layout)

    def createFormGroupBox2(self):
        self.formGroupBox2 = QtWidgets.QGroupBox("Figure")

class Window(QtWidgets.QMainWindow):

    def __init__(self,parent=None):
        super(Window, self).__init__(parent)
        self.setGeometry(150, 150, 1550, 1200)
        self.title='Synchrophase Fault Identification'
        self.dialogs = list()
        extracAction = QtWidgets.QAction("&exit", self)
        extracAction.triggered.connect(self.close_application)
        helpAction = QtWidgets.QAction("help", self)
        helpAction.triggered.connect(self.help_info)



        loadfile = QtWidgets.QAction("&Load data", self)
        loadfile.setShortcut("Ctrl+O")
        loadfile.setStatusTip('Load data')
        # openFile.triggered.connect(self.file_open)
        savedata = QtWidgets.QAction("&Save data", self)
        savedata.setShortcut("Ctrl+S")
        savedata.setStatusTip('Load data')
        vendorlist = QtWidgets.QAction("&Vendor List", self)
        savedata.setStatusTip('Load data')

        Contact = QtWidgets.QAction("&Contact", self)
        Contact.setShortcut("Ctrl+C")
        Contact.setStatusTip('Contact Information')
        # Contact.triggered.connect(self.help_info())

        search=QtWidgets.QAction("&Search", self)
        search.setStatusTip('Search data')

        Clear =QtWidgets.QAction("&Clear", self)
        Clear.setStatusTip('Clear all data')

        Statistics =QtWidgets.QAction("&Statistics", self)
        Statistics.setStatusTip('Load data')
        Statistics.triggered.connect(self.statisticstri)

        Dataquality =QtWidgets.QAction("&Data Quality", self)
        Dataquality.setStatusTip('data quality')
        Dataquality.triggered.connect(self.dataqualitytri)

        SVMlearning = QtWidgets.QAction("&Support vector machine", self)
        SVMlearning.triggered.connect(self.SVMlearningtri)
        Llearning = QtWidgets.QAction("&Logistic regression", self)
        Llearning.triggered.connect(self.Llearningtri)
        KNNlearning = QtWidgets.QAction("&K nearest neighboring", self)
        KNNlearning.triggered.connect(self.KNNlearningtri)
        DTlearning = QtWidgets.QAction("&Decision tree", self)
        DTlearning .triggered.connect(self.DTlearningtri)
        NBlearning = QtWidgets.QAction("&Naïve bayes", self)
        NBlearning.triggered.connect(self.NBlearningtri)
        HSLlearning = QtWidgets.QAction("&Hybrid supervised learning", self)
        HSLlearning.triggered.connect(self.HSLlearningtri)

        CPDlearning = QtWidgets.QAction("&Change point detection", self)
        CPDlearning.triggered.connect(self.CPDlearningtri)
        PCAlearning = QtWidgets.QAction("&PCA (visualization)", self)
        PCAlearning.triggered.connect(self.PCAlearningtri)
        CETlearning = QtWidgets.QAction("&Clustering for event type", self)
        CETlearning.triggered.connect(self.CETlearningtri)
        CELlearning = QtWidgets.QAction("&Clustering for event location", self)
        CELlearning.triggered.connect(self.CELlearningtri)

        loadnetwork = QtWidgets.QAction("&Load network", self)
        visualization = QtWidgets.QAction("&Visualization", self)
        addfault = QtWidgets.QAction("&Add fault flag", self)

        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        Toolbox = mainMenu.addMenu('&Toolbox')
        ViewMenu = mainMenu.addMenu('&Machine learning model')
        VisualMenu = mainMenu.addMenu('Network visualiztion')
        helpMenu = mainMenu.addMenu('&Help')

        fileMenu.addAction(loadfile)
        fileMenu.addAction(savedata)
        fileMenu.addAction(vendorlist)
        fileMenu.addAction(Contact)

        Toolbox.addAction(search)
        Toolbox.addAction(Clear)
        Toolbox.addAction(Statistics)
        Toolbox.addAction(Dataquality)

        Slearning1=ViewMenu.addMenu("&Supervised learning")
        Ulearning=ViewMenu.addMenu("&Unsupervised learning")
        ViewMenu.addMenu("&Semi-Supervised learning")
        ViewMenu.addMenu("&Active learning")

        Slearning1.addAction(SVMlearning)
        Slearning1.addAction(Llearning)
        Slearning1.addAction(KNNlearning)
        Slearning1.addAction(DTlearning)
        Slearning1.addAction(NBlearning)
        Slearning1.addAction(HSLlearning)

        Ulearning.addAction(CPDlearning)
        Ulearning.addAction(PCAlearning)
        Ulearning.addAction(CETlearning)
        Ulearning.addAction(CELlearning)

        VisualMenu.addAction(loadnetwork)
        VisualMenu.addAction(visualization)
        VisualMenu.addAction(addfault)

        helpMenu.addAction(helpAction)

        self.home()

    def home(self):
        self.main = QtWidgets.QWidget(self)
        self.setWindowTitle(self.title)

        self.createFormGroupBox1()
        self.createFormGroupBox2()

        self.layout = QtWidgets.QHBoxLayout(self.main)
        self.layout.addWidget(self.formGroupBox1)
        self.layout.addWidget(self.formGroupBox)

        self.setCentralWidget(self.main)

        self.show()
        self.update()

    def createFormGroupBox1(self):
        self.formGroupBox1 = QtWidgets.QGroupBox("Function Module")
        self.createFormGroupBox3()
        self.name = []

        self.label2 = QtWidgets.QLabel()
        functionmap = QPixmap('function.JPG')
        self.label2.setPixmap(functionmap)

        self.label = QtWidgets.QLabel()
        pixmap = QPixmap('EPRI.JPG')
        self.label.setPixmap(pixmap)

        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)
        self.btn = QtWidgets.QPushButton('Download', self)
        self.btn.clicked.connect(self.download)



        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.formGroupBox3)
        layout.addWidget(self.label2)
        layout.addWidget(self.progress)
        layout.addWidget(self.btn)
        layout.addWidget(self.label)
        self.formGroupBox1.setLayout(layout)

    def createFormGroupBox3(self):
        self.formGroupBox3 = QtWidgets.QGroupBox("Data Spliting")

        self.s1 = QtWidgets.QSlider(Qt.Horizontal)
        self.s1.setMinimum(1)
        self.s1.setMaximum(99)
        self.s1.setValue(25)
        self.s1.setTickInterval(10)
        self.s1.setTickPosition(QtWidgets.QSlider.TicksBothSides)

        self.spliter = QtWidgets.QPushButton("Confirm data splitting")
        layoutt = QtWidgets.QHBoxLayout()
        layoutt.addWidget(self.s1)
        layoutt.addWidget(self.spliter)

        self.formGroupBox3.setLayout(layoutt)


    def createFormGroupBox2(self):
        self.formGroupBox = QtWidgets.QGroupBox("Search Result:")
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(5)
        layoutt = QtWidgets.QVBoxLayout()
        layoutt.addWidget(self.tableWidget)
        self.formGroupBox.setLayout(layoutt)


    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self, 'Extract',"confirm to quit?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass
    def help_info(self):
        choice = QtWidgets.QMessageBox.question(self, 'help imformation', "please contact mike ", QtWidgets.QMessageBox.Yes)

        if choice == QtWidgets.QMessageBox.Yes:
            pass

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)
    def statisticstri(self):
        dialog = Second(self)
        self.dialogs.append(dialog)
        dialog.show()
    def dataqualitytri(self):
        dialog = Third(self)
        self.dialogs.append(dialog)
        dialog.show()
    def SVMlearningtri(self):
        dialog = SVMdialog(self)
        self.dialogs.append(dialog)
        dialog.show()
    def Llearningtri(self):
        dialog = LRdialog(self)
        self.dialogs.append(dialog)
        dialog.show()
    def KNNlearningtri(self):
        dialog = KNNdialog(self)
        self.dialogs.append(dialog)
        dialog.show()
    def DTlearningtri(self):
        dialog = DTdialog(self)
        self.dialogs.append(dialog)
        dialog.show()
    def NBlearningtri(self):
        dialog = NBdialog(self)
        self.dialogs.append(dialog)
        dialog.show()
    def HSLlearningtri(self):
        dialog = HSLdialog(self)
        self.dialogs.append(dialog)
        dialog.show()
    def CPDlearningtri(self):
        dialog = CPDdialog(self)
        self.dialogs.append(dialog)
        dialog.show()

    def PCAlearningtri(self):
        dialog = PCAdialog(self)
        self.dialogs.append(dialog)
        dialog.show()

    def CETlearningtri(self):
        dialog = CETdialog(self)
        self.dialogs.append(dialog)
        dialog.show()

    def CELlearningtri(self):
        dialog = CELdialog(self)
        self.dialogs.append(dialog)
        dialog.show()

def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    GUI.show()
    sys.exit(app.exec_())

run()