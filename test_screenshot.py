#!/usr/bin/python
import sys
import signal

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *


app = QApplication(sys.argv)

def onLoadFinished(result):
    if result:
        # Set the size of the (virtual) browser window
        webpage.setViewportSize(webpage.mainFrame().contentsSize())
        #webpage.setViewportSize(QSize(400, 400))
        # Paint this frame into an image
        imag = QImage(webpage.viewportSize(), QImage.Format_ARGB32)
        painter = QPainter(imag)
        webpage.mainFrame().render(painter)
        painter.end()
        print imag.save("output.png")
        # thumb = QImage(imag.scaled(678, 1024)
        #thumb.save("output.jpg")
    else:
        print "fail to get that page"

    sys.exit(0)

if __name__ == '__main__':
    #web = QWebView()
    #web.load(QUrl("www.sina.com.cn"))
    #webPage = web.page()
    #webPage.connect(webPage, SIGNAL("loadFinished(bool)"), storeImg)
    webpage = QWebPage()
    webpage.qWebSettings = {
        QWebSettings.JavascriptEnabled : True,
        QWebSettings.PluginsEnabled : True,
        QWebSettings.PrivateBrowsingEnabled : True,
        QWebSettings.JavascriptCanOpenWindows : False
    }

    webpage.connect(webpage, SIGNAL("loadFinished(bool)"), onLoadFinished)
    webpage.mainFrame().load(QUrl(sys.argv[1]))
    app.exec_()
