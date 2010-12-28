#!/usr/bin/env python
from Tkinter import *
from tkMessageBox import *
import contextlib
import shelve

filedsname = ('name', 'age', 'sex')
shelve_file = '/home/ethan/data/gui_db'


def mkWidgets(db):
    window = Tk()
    window.title('test')

    form = Frame(window)
    labels = Frame(form)
    values = Frame(form)

    labels.pack(side=LEFT)
    values.pack(side=RIGHT)
    form.pack()

    entries = {}

    for label in filedsname:
        Label(labels, text=label).pack()
        ent = Entry(values)
        ent.pack()
        entries[label] = ent

    Button(window, text='Fetch', command=lambda: fetchRecord(entries)).pack(side=LEFT)
    Button(window, text='Update', command=lambda: updateRecord(db, entries)).pack(side=RIGHT)
    Button(window, text='Quit', command=window.quit).pack(side=RIGHT)

    return window


def fetchRecord(entries):
    key = entries['name'].get()

    try:
        record = db[key]
    except:
        showerror(title='Error', message='No such key ' + key)
    else:
        for field in filedsname:
            entries[field].delete(0, END)
            entries[field].insert(0, record[field])

    
def updateRecord(db, entries):
    key = entries['name'].get()

    if key in db.keys():
        record = db[key]
    else:
        record = {}

    for field in filedsname:
        record[field] = entries[field].get()

    db[key] = record
    debug('Update success')


def debug(message):
    showinfo(title='debug', message=message)


def init():
    db['ethan'] = {'name' : 'ethan', 'age' : 22, 'sex' : 1}


if __name__ == '__main__':
    with contextlib.closing(shelve.open(shelve_file)) as db:
        if not db:
            init()

        window = mkWidgets(db)
        window.mainloop()

