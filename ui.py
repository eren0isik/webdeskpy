import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile

class MainWindow(QMainWindow):
    def __init__(self, title="PyGreap", locx=0, locy=0, w=800, h=600, uiloc="/"):
        super().__init__()

        # Pencere ayarları
        self.setWindowTitle(title)
        self.setGeometry(locx, locy, w, h)

        # Web görüntüleyiciyi oluştur
        self.browser = QWebEngineView()
        self.profile = QWebEngineProfile.defaultProfile()
        # URL belirle
        custom_user_agent = "WebDeskPy/1.0"
        self.profile.setHttpUserAgent(custom_user_agent)
        url = QUrl("http://127.0.0.1:6091" + uiloc)

        # HTML dosyasını yükle
        self.browser.load(url)

        # Pencere içine yerleştir
        self.setCentralWidget(self.browser)

def UiStart(titLE="WebDeskPy", locationx=100, locationy=100, width=800, height=600, uilocation=None):
    app = QApplication(sys.argv)
    window = MainWindow(title=titLE, locx=locationx, locy=locationy, w=width, h=height, uiloc=uilocation)
    window.show()
    app.exec_()
