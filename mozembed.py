#!/usr/bin/python
# see a mini youtube video on resizable window
# this script could be better
 
import sys
import gtk
import gtkmozembed
import re
 
if (len(sys.argv)==1) :
        print "~$ script url_video"
            sys.exit() # exit if not url
        URL = sys.argv[1]
        m = re.search('(?&lt;=v=).{11}',URL)
        id = m.group(0)
     
# html code to render on the small web browser
    data ='<object width="100%" height="100%" data="http://www.youtube.com/swf/l.swf?video_id='+id+'&amp;rel=1&amp;iurl=null&amp;color1=0x2b405b&amp;color2=0x6b8ab6&amp;autoplay=1" type="application/x-shockwave-flash">
    <param name="allowFullScreen" value="true" />
    <param name="src" value="http://www.youtube.com/swf/l.swf?video_id='+id+'&amp;rel=1&amp;iurl=null&amp;color1=0x2b405b&amp;color2=0x6b8ab6&amp;autoplay=1" />
    <param name="allowfullscreen" value="true" /></object>'
     
    def CloseWindow(caller_widget):
            """Close the window and exit the app"""
                   gtk.main_quit()
                
               win = gtk.Window()
    win.set_title("Small Web Browser")
    win.set_position(gtk.WIN_POS_NONE) # general put the window on the top left corner
    win.set_resizable(True) # resizable window
    win.connect("destroy", CloseWindow)
     
    gtkmozembed.set_profile_path("/tmp", "simple_browser_user")
    mozbrowser = gtkmozembed.MozEmbed() # gtkmozembed
     
    win.add(mozbrowser)
    win.show_all()
     
    mozbrowser.set_size_request(272,223) #size of the window
# show the video on the small web browser
    mozbrowser.render_data(data, long(len(data)), 'file:///', 'text/html')
     
    gtk.main()
