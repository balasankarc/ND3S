#! /usr/bin/env python
# -*- coding: utf-8 -*
import gtk
import sys


class Base:

    def file1choose(self,widget):
        dialog = gtk.FileChooserDialog("Select File",None,gtk.FILE_CHOOSER_ACTION_OPEN,(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OK,gtk.RESPONSE_OK))
        dialog.run()
        file1 = dialog.get_filenames()
        file1text = str(open(file1[0]).read())
        self.file1content.get_buffer().set_text(file1text)
        
        dialog.destroy()
    def closewindow(self, widget):
        sys.exit()

    def __init__(self):
        self.window = gtk.Window()
        self.window.set_title("ND3S")
        self.window.set_size_request(300, 300)
        self.window.connect("destroy", self.closewindow)
        self.fixed = gtk.Fixed()
        self.file1button = gtk.Button("Choose File 1")
        self.file1button.connect("clicked", self.file1choose)
        self.scrollwindow1 = gtk.ScrolledWindow()
        self.file1content = gtk.TextView()
        self.scrollwindow1.add(self.file1content)
        self.file1content.set_size_request(500, 500)
        self.fixed.put(self.scrollwindow1, 10, 80)
        self.fixed.put(self.file1button, 10, 10)
        self.window.add(self.fixed)
        self.window.show()
        self.window.show_all()
        self.window.maximize()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()
