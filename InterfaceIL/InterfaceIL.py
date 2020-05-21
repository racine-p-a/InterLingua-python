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
        self.file_statistics = 0

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
        self.browse_button = Button(file_picker_frame, text="Browse", command=self.seek_file, width=10) \
            .grid(column=1, row=2)
        self.analyse_file_button = Button(file_picker_frame, text="Check !", command=self.analyse_file, width=10) \
            .grid(column=0, row=3)

        # Results frame
        self.results_frame = Notebook(self.root)

        #       FIRST TAB : Global results
        self.tab_global_results = Frame(self.results_frame)
        #                   Number of letters
        self.number_of_letters_entry = Label(self.tab_global_results, text='Number of letters :')
        self.number_of_letters_result = Spinbox(self.tab_global_results, from_=0, to=10, width=15)
        self.number_of_letters_entry.grid(column=0, row=1)
        self.number_of_letters_result.grid(column=1, row=1)
        #                   Number of lines
        self.number_of_lines_entry = Label(self.tab_global_results, text='Number of lines :')
        self.number_of_lines_result = Spinbox(self.tab_global_results, from_=0, to=10, width=15)
        self.number_of_lines_entry.grid(column=0, row=2)
        self.number_of_lines_result.grid(column=1, row=2)
        #                   Number of words
        self.number_of_words_entry = Label(self.tab_global_results, text='Number of words :')
        self.number_of_words_result = Spinbox(self.tab_global_results, from_=0, to=10, width=15)
        self.number_of_words_entry.grid(column=0, row=3)
        self.number_of_words_result.grid(column=1, row=3)
        #                   Number of letter monograms
        self.number_of_letters_monograms_entry = Label(self.tab_global_results, text='Number of monograms of letters :')
        self.number_of_letters_monograms_result = Treeview(self.tab_global_results,columns=('Message ID', 'Other Data'))
        self.number_of_letters_monograms_result.heading('#0', text='Monogram')
        self.number_of_letters_monograms_result.heading('#1', text='Count')
        self.number_of_letters_monograms_result.column('#0', stretch=YES)
        self.number_of_letters_monograms_result.column('#1', stretch=YES)


        self.number_of_letters_monograms_entry.grid(column=0, row=4)
        self.number_of_letters_monograms_result.grid(column=1, row=4)

        self.results_frame.add(self.tab_global_results, text='Global results')

        # Language results
        tab_language_results = Frame(self.results_frame)
        self.results_frame.add(tab_language_results, text='Language results')

        # Authors results
        tab_author_results = Frame(self.results_frame)
        self.results_frame.add(tab_author_results, text='Author results')

        self.results_frame.grid(column=0, row=4)

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
        self.update_entries()

    def update_entries(self):
        """
        Uodate all entries in the interface with the data in the variable self.file_statistics.
        :return:
        """
        self.number_of_letters_result.insert(INSERT, getattr(self.file_statistics, 'letter_count'))
        self.number_of_lines_result.insert(INSERT, getattr(self.file_statistics, 'line_count'))
        self.number_of_words_result.insert(INSERT, getattr(self.file_statistics, 'word_count'))
        self.update_letter_monograms_entry()

    def update_letter_monograms_entry(self):
        self.number_of_letters_monograms_result.insert("", 'end', values=('toto', 'titi'))
