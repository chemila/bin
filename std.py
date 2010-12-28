import sys, os, traceback
from Tkinter import *
from tkMessageBox import *

class Input:

    def __init__(self, message):
        self.message = message

    def read(self):
        showinfo(title='read', message=self.message)
        print self.message


class Output:

    def __init__(self):
        self.message = ''

    def write(self, message):
        self.message = self.message +  message
        showerror(title='write', message=self.message)



sys.stdin = Input('hello world')
sys.stdout = Output()

sys.stdin.read()

