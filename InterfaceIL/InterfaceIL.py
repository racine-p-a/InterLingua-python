# -*- coding:Utf-8 -*-

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *
from analysis.file_analysis import *


class InterfaceIL(object):
    """
    Create InterLingua interface.
    """

    def __init__(self):
        """
        """
        self.root = Tk()
        self.root.title('InterLingua (using Python3)')

        # File picker frame
        file_picker_frame = LabelFrame(self.root, text="File")
        file_picker_frame.grid(column=0, row=1)
        #
        #   Please, choose the file to examinate using the « Browse » button.
        #
        #    _________________________________       __________
        #   |_________________________________|     |__Browse__|
        #
        #                    _______________
        #                   |___CHECK !_____|
        #

        self.file_label = Label(file_picker_frame, text="Choose the file you want to examine :").grid(column=0, row=1)
        self.file_entry = Entry(file_picker_frame, width='50')
        self.file_entry.grid(column=0, row=2)
        self.browse_button = Button(file_picker_frame, text="Browse", command=self.seek_file, width=10)\
            .grid(column=1, row=2)
        self.analyse_file_button = Button(file_picker_frame, text="Check !", command=self.analyse_file, width=10)\
            .grid(column=0, row=3)

        # Results frame
        results_frame = LabelFrame(self.root, text="Results")
        results_frame.grid(column=0, row=2)

        left = Label(results_frame, text="Results")
        left.grid(column=0, row=0)

        # End buttons frame
        end_button_frame = LabelFrame(self.root, text="Action")
        end_button_frame.grid(column=0, row=3)
        Button(end_button_frame, text='Export', command=self.root.quit).grid(row=8, column=4)
        Button(end_button_frame, text='Leave', command=self.root.quit).grid(row=8, column=5)

        # self.root = Tk()
        #
        #
        #
        # self.entreeFichier = Entry(self.root, width='50')
        # self.entreeFichier.grid(row=2, column=0)
        #
        # self.boutonParcourir = Button(self.root, text="Browse", command=self.chercherFichier, width=10)
        # self.boutonParcourir.grid(row=2, column=1, )
        #
        # Button(self.root, text='Confirmer', command=self.lancerProgrammePrincipal).grid(row=8, column=0)
        #
        # file_block = Labelframe(self.root, text='test').pack(fill="both", expand="yes")
        # Label(self.root, text='test 1').grid(column=0, row=0)
        # Label(file_block, text='test 2').grid(column=0, row=1)

    def seek_file(self):
        """
        The browse button for the user. It
        """
        fname = askopenfilename(filetypes=(
            ("All files", "*.*"),
            ))
        self.file_entry.delete(0, END)
        self.file_entry.insert(0, fname)

    def analyse_file(self):
        data = FileAnalysis(self.file_entry.get())
