#!/usr/bin/python

import sys
import signal

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import QWebPage

def onLoadFinished(result):
    if not result:
        print "Request failed"
        sys.exit(1)

    #screen = QtGui.QDesktopWidget().screenGeometry()
    size = webpage.mainFrame().contentsSize()
    # Set the size of the (virtual) browser window
    webpage.setViewportSize(webpage.mainFrame().contentsSize())

    # Paint this frame into an image
    image = QImage(webpage.viewportSize(), QImage.Format_ARGB32)
    painter = QPainter(image)
    webpage.mainFrame().render(painter)
    painter.end()

    image.save("/tmp/output.png")
    sys.exit(0)

qtargs = [sys.argv[0]]
qtargs.append("-display")
qtargs.append(":0")

app = QApplication(qtargs,True)
#app = QApplication(sys.argv)
signal.signal(signal.SIGINT, signal.SIG_DFL)

webpage = QWebPage()
webpage.mainFrame().setScrollBarPolicy(Qt.Horizontal, Qt.ScrollBarAlwaysOff)
webpage.mainFrame().setScrollBarPolicy(Qt.Vertical, Qt.ScrollBarAlwaysOff)
webpage.connect(webpage, SIGNAL("loadFinished(bool)"), onLoadFinished)
webpage.mainFrame().load(QUrl(sys.argv[1]))

sys.exit(app.exec_())
