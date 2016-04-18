from PyQt4 import QtCore

from PyQt4.QtCore import QObject
from PyQt4.QtWebKit import QWebView


class View(QWebView):
    def __init__(self):
        super(View, self).__init__()
        self.setupUi()
        self.load(QtCore.QUrl("http://faforever.com"))

    def setupUi(self):
        pass
