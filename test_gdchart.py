#!/usr/bin/env python
import cgitb; cgitb.enable()
import gdchart
import sys

data1 = (0.5, 0.09, 0.3, 0.75, 0.0, 0.90)
data2 = (1.9, 1.3, 1.2, 0.75, 0.1, 2.0)
data3 = (62, 71, 71, 52, 55, 48)
data4 = (42, 62, 52, 37, 52, 50)
cities = ('Chicago', 'New York', 'L.A.', 'Atlanta', 'Paris, MD\n(USA)', 'London')
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

dates = ('Jan 1', 'Jan 8', 'Jan 15', 'Jan 22', 'Jan 29', 'Feb 5')
h1=(28,30,32,33,36,35)
l1=(24,27,28,30,31,24)
c1=(27,29,30,31,33,26)

h2=map(lambda x:0.8*x, h1); h2.reverse()
l2=map(lambda x:0.6*x, l1); l2.reverse()
c2=map(lambda x:0.7*x, c1); c2.reverse()

gd = gdchart.HLC3D()
gd.title = 'Hi-Lo-Close Chart'
gd.yaxis = 1
gd.ylabel_fmt = '$%.0f '
gd.set_color = (0x80ff80, 0x8080ff, 0xff8080, 0x80c080, 0x8080c0, 0xc08080)
gd.hlc_style = ("I_CAP", "CONNECTING")
gd.setLabels(dates)
gd.width = 550
gd.height = 550
gd.setData((h1,l1,c1))
gd.draw('chart.png')
