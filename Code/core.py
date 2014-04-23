#! /usr/bin/env python
# -*- coding: utf-8 -*
import gtk
import sys
import pango
import sentencer
import comparator
class Base:

    def compareinit(self, widget):
        if len(self.files) == 0:
            dialog = gtk.MessageDialog(self.window, 0, gtk.MESSAGE_ERROR, gtk.BUTTONS_OK, u"No file chosen")
            dialog.set_title("Error")
            dialog.run()
            dialog.destroy()
        elif self.files[0] == "":
            dialog = gtk.MessageDialog(self.window, 0, gtk.MESSAGE_ERROR, gtk.BUTTONS_OK, u"File 1 not chosen")
            dialog.set_title("Error")
            dialog.runt()
            dialog.destroy()
        elif self.files[1] == "":
            dialog = gtk.MessageDialog(self.window, 0, gtk.MESSAGE_ERROR, gtk.BUTTONS_OK, u"File 2 not chosen")
            dialog.set_title("Error")
            dialog.runt()
            dialog.destroy()
        else:
            ngramdict1 = sentencer.sentencer(self.files[0])
            ngramdict2 = sentencer.sentencer(self.files[1])
            result = comparator.comparator(ngramdict1, ngramdict2)
            dialog = gtk.MessageDialog(self.window, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, u"The percentage similarity is " + str(result) + "%")
            dialog.run()
            dialog.destroy()


        #dialog = gtk.MessageDialog(self.window, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, u"Not yet implemented")
        #dialog.set_title("Compare")
        #dialog.run()
        #dialog.destroy()

    def windowclick(self, widget):
        print "Here:"

    def changethreshold(self, widget, data):
        self.thresholdtext.set_text("")

    def filechoose(self, widget, *data):
        """Function to choose input files"""
        dialog = gtk.FileChooserDialog("Select File", None, gtk.FILE_CHOOSER_ACTION_OPEN, (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OK, gtk.RESPONSE_OK))
        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            inputfile = dialog.get_filenames()
            filetext = str(open(inputfile[0]).read())
            if len(self.files) == 2:
                if data[0] == "File1":
                    self.files[0] = inputfile[0]
                else:
                    self.files[1] = inputfile[0]
            else:
                self.files.append(inputfile[0])
            if data[0] == "File1":
                self.file1content.get_buffer().set_text(filetext)
            if data[0] == "File2":
                self.file2content.get_buffer().set_text(filetext)
        dialog.destroy()


    def closewindow(self, widget):
        """Function to terminate the program"""
        sys.exit()

    def helpfunction(self, widget):
        """Function to display Help dialog"""
        dialog = gtk.MessageDialog(self.window, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, "Open the two files using the File Choose Buttons. \n\nThe contents of the files will be displayed in the respective textboxes.\n\nSpecify the threshold value ,above which the similarity should mean data fraud, in the textbox provided at the bottom.\n\nClick the Compare button to get the result.")
        dialog.set_title("Help")
        dialog.run()
        dialog.destroy()

    def __init__(self):
        self.window = gtk.Window()
        pixbuf = gtk.gdk.pixbuf_new_from_file('assets/images/bg.jpg')
        pixmap, mask = pixbuf.render_pixmap_and_mask()
        self.window.set_app_paintable(gtk.TRUE)
        self.window.realize()
        self.window.window.set_back_pixmap(pixmap,gtk.FALSE)
        self.window.set_title("ND3S")
        self.window.set_size_request(300, 300)
        self.window.connect("destroy", self.closewindow)
        self.fixed = gtk.Fixed()
        self.file1button = gtk.Button("Choose File 1")
        self.file2button = gtk.Button("Choose File 2")
        self.file1button.connect("clicked", self.filechoose, "File1")
        self.file2button.connect("clicked", self.filechoose, "File2")
        self.scrollwindow1 = gtk.ScrolledWindow()
        self.scrollwindow2 = gtk.ScrolledWindow()
        self.file1content = gtk.TextView()
        self.file2content = gtk.TextView()
        self.file1content.set_property('editable', False)
        self.file2content.set_property('editable', False)
        self.file1content.set_wrap_mode(gtk.WRAP_WORD)
        self.file2content.set_wrap_mode(gtk.WRAP_WORD)
        self.label1 = gtk.Label()
        self.label1.modify_font(pango.FontDescription("GEronto Bis 37"))
        self.scrollwindow1.add(self.file1content)
        self.scrollwindow2.add(self.file2content)
        self.scrollwindow1.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
        self.scrollwindow2.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
        self.scrollwindow1.set_shadow_type(type=gtk.SHADOW_ETCHED_IN)
        self.scrollwindow2.set_shadow_type(type=gtk.SHADOW_ETCHED_IN)
        self.file1content.set_size_request(500, 500)
        self.fixed.put(self.scrollwindow1, 10, 120)
        self.file2content.set_size_request(500, 500)
        self.fixed.put(self.scrollwindow2, 600, 120)
        self.fixed.put(self.file1button, 10, 80)
        self.fixed.put(self.file2button, 600, 80)
        self.label1.set_markup(u"Near Duplicate Document Detection System for <span color='#ffffff'><b>മലയാളം</b></span>")
        self.fixed.put(self.label1, 10, 30)
        self.helpbox = gtk.VBox(spacing=30)
        self.thresholdtext = gtk.Entry()
        #self.thresholdtext.set_text("Threshold")
        #self.thresholdtext.connect("focus-in-event",self.changethreshold)
        self.exitbutton = gtk.Button("Exit")
        self.exitbutton.connect("clicked", self.closewindow)
        self.helpbutton = gtk.Button("Help")
        self.helpbutton.connect("clicked", self.helpfunction)
        self.comparebutton = gtk.Button("Compare!")
        self.comparebutton.connect("clicked",self.compareinit)
        self.helpbox.set_size_request(100, 300)
        #self.helpbox.pack_start(self.thresholdtext)
        self.helpbox.pack_start(self.comparebutton)
        self.helpbox.pack_start(self.exitbutton)
        self.helpbox.pack_start(self.helpbutton)
        self.fixed.put(self.helpbox, 1200, 120)
        self.window.add(self.fixed)
        self.window.show()
        self.window.show_all()
        self.window.maximize()
        self.files = []

    def main(self):
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()
