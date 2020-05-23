# -*- coding:Utf-8 -*-

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *
from analysis.file_analysis import *
from analysis.corpus_language_analysis import *


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
        #                   Letters N-grams
        self.letters_n_grams_entry = Label(self.tab_global_results, text='Letter repartition :')
        self.letters_n_grams_result = Treeview(self.tab_global_results, columns=(
            "#0"
            'Monogram',
            'Monogram count',
            'Bigram',
            'Bigram count',
            'Trigram',
            'Trigram count',
        ))
        self.letters_n_grams_result.heading('#0', text='#')
        self.letters_n_grams_result.heading('#1', text='Monograms')
        self.letters_n_grams_result.heading('#2', text='Monograms count')
        self.letters_n_grams_result.heading('#3', text='Bigrams')
        self.letters_n_grams_result.heading('#4', text='Bigrams count')
        self.letters_n_grams_result.heading('#5', text='Trigrams')
        self.letters_n_grams_result.heading('#6', text='Trigrams count')
        self.letters_n_grams_result.column('#0', stretch=YES)
        self.letters_n_grams_result.column('#1', stretch=YES)
        self.letters_n_grams_result.column('#2', stretch=YES)
        self.letters_n_grams_result.column('#3', stretch=YES)
        self.letters_n_grams_result.column('#4', stretch=YES)
        self.letters_n_grams_result.column('#5', stretch=YES)
        self.letters_n_grams_result.column('#6', stretch=YES)

        self.letters_n_grams_entry.grid(column=0, row=4)
        self.letters_n_grams_result.grid(column=1, row=4)

        #                   Words N-grams
        self.words_n_grams_entry = Label(self.tab_global_results, text='Word repartition :')
        self.words_n_grams_result = Treeview(self.tab_global_results, columns=(
            "#0"
            'Monogram',
            'Monogram count',
            'Bigram',
            'Bigram count',
            'Trigram',
            'Trigram count',
        ))
        self.words_n_grams_result.heading('#0', text='#')
        self.words_n_grams_result.heading('#1', text='Monograms')
        self.words_n_grams_result.heading('#2', text='Monograms count')
        self.words_n_grams_result.heading('#3', text='Bigrams')
        self.words_n_grams_result.heading('#4', text='Bigrams count')
        self.words_n_grams_result.heading('#5', text='Trigrams')
        self.words_n_grams_result.heading('#6', text='Trigrams count')
        self.words_n_grams_result.column('#0', stretch=YES)
        self.words_n_grams_result.column('#1', stretch=YES)
        self.words_n_grams_result.column('#2', stretch=YES)
        self.words_n_grams_result.column('#3', stretch=YES)
        self.words_n_grams_result.column('#4', stretch=YES)
        self.words_n_grams_result.column('#5', stretch=YES)
        self.words_n_grams_result.column('#6', stretch=YES)

        self.words_n_grams_entry.grid(column=0, row=5)
        self.words_n_grams_result.grid(column=1, row=5)

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
        self.clean_entries()
        self.update_entries()
        corpus_language_analyses = CorpusLanguageAnalysis()

    def update_entries(self):
        """
        Uodate all entries in the interface with the data in the variable self.file_statistics.
        :return:
        """
        self.number_of_letters_result.insert(INSERT, getattr(self.file_statistics, 'letter_count'))
        self.number_of_lines_result.insert(INSERT, getattr(self.file_statistics, 'line_count'))
        self.number_of_words_result.insert(INSERT, getattr(self.file_statistics, 'word_count'))
        self.update_letter_stats_entry()
        self.update_word_stats_entry()

    def clean_entries(self):
        self.number_of_letters_result.delete(0, END)
        self.number_of_lines_result.delete(0, END)
        self.number_of_words_result.delete(0, END)
        self.letters_n_grams_result.delete(*self.letters_n_grams_result.get_children())
        self.words_n_grams_result.delete(*self.words_n_grams_result.get_children())

    def update_letter_stats_entry(self):
        maximal_length = len(getattr(self.file_statistics, 'letters'))
        if maximal_length < len(getattr(self.file_statistics, 'bigrams')):
            maximal_length = len(getattr(self.file_statistics, 'bigrams'))
        if maximal_length < len(getattr(self.file_statistics, 'trigrams')):
            maximal_length = len(getattr(self.file_statistics, 'trigrams'))

        for i in range(maximal_length):
            current_monogram = ''
            current_monogram_count = ''
            current_bigram = ''
            current_bigram_count = ''
            current_trigram = ''
            current_trigram_count = ''

            # Pick letter monograms.
            if i < len(getattr(self.file_statistics, 'letters')):
                current_monogram = getattr(self.file_statistics, 'letters')[i][0]
                current_monogram_count = str(getattr(self.file_statistics, 'letters')[i][1])
                percentage = getattr(self.file_statistics, 'letters')[i][1]
                percentage /= getattr(self.file_statistics, 'letter_count')
                current_monogram_count += ' (' + str(round(percentage * 100, 2)) + '%)'
            # Pick letter bigrams.
            if i < len(getattr(self.file_statistics, 'bigrams')):
                current_bigram = getattr(self.file_statistics, 'bigrams')[i][0]
                current_bigram_count = str(getattr(self.file_statistics, 'bigrams')[i][1])
                percentage = getattr(self.file_statistics, 'bigrams')[i][1]
                percentage /= getattr(self.file_statistics, 'cumulated_sum_of_bigrams')
                current_bigram_count += ' (' + str(round(percentage * 100, 2)) + '%)'
            # Pick letter trigrams.
            if i < len(getattr(self.file_statistics, 'trigrams')):
                current_trigram = getattr(self.file_statistics, 'trigrams')[i][0]
                current_trigram_count = str(getattr(self.file_statistics, 'trigrams')[i][1])
                percentage = getattr(self.file_statistics, 'trigrams')[i][1]
                percentage /= getattr(self.file_statistics, 'cumulated_sum_of_trigrams')
                current_trigram_count += ' (' + str(round(percentage * 100, 2)) + '%)'

            self.letters_n_grams_result.insert("", 'end', values=(
                self.make_characters_displayable(current_monogram),
                current_monogram_count,
                self.make_characters_displayable(current_bigram),
                current_bigram_count,
                self.make_characters_displayable(current_trigram),
                current_trigram_count
            ))

    def update_word_stats_entry(self):
        maximal_length = len(getattr(self.file_statistics, 'words'))
        if maximal_length < len(getattr(self.file_statistics, 'word_bigrams')):
            maximal_length = len(getattr(self.file_statistics, 'word_bigrams'))
        if maximal_length < len(getattr(self.file_statistics, 'word_trigrams')):
            maximal_length = len(getattr(self.file_statistics, 'word_trigrams'))

        for i in range(maximal_length):
            current_monogram = ''
            current_monogram_count = ''
            current_bigram = ''
            current_bigram_count = ''
            current_trigram = ''
            current_trigram_count = ''

            # Pick word monograms.
            if i < len(getattr(self.file_statistics, 'words'))\
                    and getattr(self.file_statistics, 'word_count') > 0:
                current_monogram = getattr(self.file_statistics, 'words')[i][0]
                current_monogram_count = str(getattr(self.file_statistics, 'words')[i][1])
                percentage = getattr(self.file_statistics, 'words')[i][1]
                percentage /= getattr(self.file_statistics, 'word_count')
                current_monogram_count += ' (' + str(round(percentage * 100, 2)) + '%)'
            # Pick letter bigrams.
            if i < len(getattr(self.file_statistics, 'word_bigrams'))\
                    and getattr(self.file_statistics, 'cumulated_sum_of_word_bigrams') > 0:
                current_bigram = getattr(self.file_statistics, 'word_bigrams')[i][0]
                current_bigram_count = str(getattr(self.file_statistics, 'word_bigrams')[i][1])
                percentage = getattr(self.file_statistics, 'word_bigrams')[i][1]
                percentage /= getattr(self.file_statistics, 'cumulated_sum_of_word_bigrams')
                current_bigram_count += ' (' + str(round(percentage * 100, 2)) + '%)'
            # Pick letter trigrams.
            if i < len(getattr(self.file_statistics, 'word_trigrams'))\
                    and getattr(self.file_statistics, 'cumulated_sum_of_word_trigrams') > 0:
                current_trigram = getattr(self.file_statistics, 'word_trigrams')[i][0]
                current_trigram_count = str(getattr(self.file_statistics, 'word_trigrams')[i][1])
                percentage = getattr(self.file_statistics, 'word_trigrams')[i][1]
                percentage /= getattr(self.file_statistics, 'cumulated_sum_of_word_trigrams')
                current_trigram_count += ' (' + str(round(percentage * 100, 2)) + '%)'

            self.words_n_grams_result.insert("", 'end', values=(
                current_monogram,
                current_monogram_count,
                current_bigram,
                current_bigram_count,
                current_trigram,
                current_trigram_count
            ))

    @staticmethod
    def make_characters_displayable(dirty_string=''):
        return '"' + dirty_string + '"'
