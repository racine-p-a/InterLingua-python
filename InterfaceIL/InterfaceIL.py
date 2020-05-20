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
        self.file_statistics = None

        self.root = Tk()
        self.root.title('InterLingua (using Python3)')

        # File picker frame
        file_picker_frame = LabelFrame(self.root, text="File")
        file_picker_frame.grid(column=0, row=1)
        # #   Please, choose the file to examinate using the « Browse » button.
        # #
        # #    _________________________________       __________
        # #   |_________________________________|     |__Browse__|
        # #
        # #                    _______________
        # #                   |___CHECK !_____|
        # #
        #
        self.file_label = Label(file_picker_frame, text="Choose the file you want to examine :").grid(column=0, row=1)
        self.file_entry = Entry(file_picker_frame, width='50')
        self.file_entry.grid(column=0, row=2)
        self.browse_button = Button(file_picker_frame, text="Browse", command=self.seek_file, width=10)\
            .grid(column=1, row=2)
        self.analyse_file_button = Button(file_picker_frame, text="Check !", command=self.analyse_file, width=10)\
            .grid(column=0, row=3)

        # Results frame
        results_frame = Notebook(self.root)

        # Global results
        tab_global_results = Frame(results_frame)
        number_of_letters_entry = Label(tab_global_results, text='Number of letters :')
        number_of_letters_entry.grid(column=0, row=1)
        results_frame.add(tab_global_results, text='Global results')

        # Language results
        tab_language_results = Frame(results_frame)
        results_frame.add(tab_language_results, text='Language results')

        # Authors results
        tab_author_results = Frame(results_frame)
        results_frame.add(tab_author_results, text='Author results')

        results_frame.grid(column=0, row=4)

        # Buttons frame
        end_button_frame = LabelFrame(self.root, text="Action")
        end_button_frame.grid(column=0, row=10)
        Button(end_button_frame, text='Export', command=self.root.quit).grid(row=8, column=4)
        Button(end_button_frame, text='Leave', command=self.root.quit).grid(row=8, column=5)



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
        self.file_statistics = FileAnalysis(self.file_entry.get())
