from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar

        navbar = QToolBar()
        self.addToolBar(navbar)

        # back

        back_btn = QAction('<', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # forward

        forward_btn = QAction('>', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # reload

        reload_btn = QAction('^', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # home

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

app = QApplication(sys.argv)
QApplication.setApplicationName("My Browser")
window = MainWindow()
app.exec_()