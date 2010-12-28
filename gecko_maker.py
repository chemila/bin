#!/usr/bin/env python
"""
    GtkMozEmbed Websnap.

    @copyright: 2006 by Alan Snelson <Alan@Wave2.co.uk>
    @license: BSD License
"""
__version__ = "0.1"
import os
import getopt
import sys
import gtk
import gobject
import gtk.gdk as gdk
import gtkmozembed
 
class PyGtkMozWebsnap:
    __WIDTH = 0
    __HEIGHT = 0
    __OUTPUT = ''
    def __init__(self, URL = None, WIDTH = None, HEIGHT = None, OUTPUT = None, parent = None):
        if parent == None:
            self.parent = gtk.Window(gtk.WINDOW_TOPLEVEL)
            self.parent.set_border_width(0)
        else:
            self.parent = parent

        self.WIDTH = int(WIDTH)
        self.HEIGHT = int(HEIGHT)
        self.OUTPUT = OUTPUT
        # Initialize the widgets...
        self.widget = gtkmozembed.MozEmbed()
        self.widget.set_size_request(1024, 2000)
 
        # Connect signals
        self.widget.connect("net_stop", self.on_net_stop)
        self.widget.connect("progress", self.on_progress)
 
        self.parent.add(self.widget)
 
        if URL != None:
            self.widget.load_url(URL)

        self.parent.show_all()
        self.countdown = 3
 
    def on_progress(self, data, cur, max):
        print cur,"bytes loaded"

    def on_net_stop(self, data = None):
        gobject.timeout_add(1000,self.do_countdown,self)
        print "Taking screenshot in 3...",
        sys.stdout.flush()
 
    def do_countdown(self, data = None):
        self.countdown -= 1
        if(self.countdown > 0):
            print str(self.countdown)+"...",
            sys.stdout.flush()
            gobject.timeout_add(1000,self.do_countdown,self)
            return True
        else:
            print
            self.screenshot()
 
    def screenshot(self, data = None):
        window = self.widget.window
        (x,y,width,height,depth) = window.get_geometry()
        pixbuf = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,width,height)
        pixbuf.get_from_drawable(window,self.widget.get_colormap(),0,0,0,0,width,height)
        # pixbuf = pixbuf.scale_simple(self.WIDTH, self.HEIGHT, gdk.INTERP_HYPER)
        pixbuf.save(self.OUTPUT, "png", {"quality":"100"})
        print "Wrote " + self.OUTPUT
        gtk.main_quit()
        return True
 
def __windowExit(widget, data=None):
    gtk.main_quit()
    
def usage ():
    """ 
    Print Websnap usage information.
    """
    print "Usage: websnap [-ho] [-u url]\r\n"
    print "Options: --help -h                Displays this usage."
    print "         --url -u URL   The url to snap" 
    print "         --height HEIGHT   Snapshot height in pixels."
    print "         --width WIDTH   Snapshot width in pixels."
    print "         --output -o OUTPUT   Snapshot filename."
    sys.exit(0)
    
def main():
    """
    Entry point for GtkMozEmbed Websnap.
    """
    try:
        opts, args = getopt.getopt (sys.argv[1:], "ho:vu:", ["height=", "width=", "help", "output=", "url="])
    except getopt.GetoptError :
        # print help information and exit:
        usage()
        sys.exit(2)
    WIDTH = 90
    HEIGHT = 68
    URL = ''
    OUTPUT = 'websnap.png'
    for o, a in opts: 
        if o == "-v":
            verbose = True
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        if o in ("-o", "--output"): 
            OUTPUT = a
        if o in ("-u", "--url"):
            URL = a
        if o in ("--width"):
            WIDTH = a
        if o in ("--height"): 
            HEIGHT = a
    if URL == '': 
        # print help information and exit:
        usage()
        sys.exit(2)
    try:
        HomeDir = os.environ["HOME"]
    except KeyError:
        raise "No Home Directory, please set HOME environment variable."
 
    ProfileDir = HomeDir + "/.gtkmozwebsnap/"
    print "Note: a mozilla profile has been created in : " + ProfileDir
 
    gtkmozembed.set_profile_path(ProfileDir, "helpsys")
 
    window = PyGtkMozWebsnap(URL,WIDTH,HEIGHT,OUTPUT)
    window.parent.connect("destroy", __windowExit)
    gtk.main()
 
if __name__ == "__main__":
    main()
