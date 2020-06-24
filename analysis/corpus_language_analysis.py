# -*- coding:Utf-8 -*-

import pathlib
import os

from analysis.file_analysis import FileAnalysis


class CorpusLanguageAnalysis(object):
    """
    Representation of a file and manages all computations ad operations required.
    """

    def __init__(self):
        """
        At class call, we have to follow these steps :
        - make a list of all folders in the language corpus
        - analyze the texts inside the folder and record the results
        """
        self.language_corpus_directory = ''
        self.language_directories_list = []
        self.languages_statistics = {}
        self.results_languages_comparison = {}

        # Get folder list.
        root_directory = pathlib.Path(__file__).parent.parent.absolute()
        self.language_corpus_directory = os.path.join(root_directory, 'corpus/languages')
        # Get all languages sub-folders.
        self.get_list_language_directories()
        # For each language folder, analyze the corpus.
        self.analyze_languages()


    def analyze_languages(self):
        for language_folder in self.language_directories_list:
            # Create the results file if they do not exist.
            if not os.path.exists(os.path.join(language_folder, 'results.txt')):
                self.build_result_file(language_folder)
            # Read and load the results.
            self.languages_statistics[os.path.join(language_folder, 'results.txt')] = self.load_result_file(
                os.path.join(language_folder, 'results.txt')
            )


    @staticmethod
    def load_result_file(result_file=''):
        letters = {}
        words = {}
        with open(result_file, 'r') as content_file:
            content = content_file.read()
        _, letter_block, word_block, _ = content.split('---')

        # Reading the letters
        letter_block = letter_block.split("\n")
        for letter_datum in letter_block:
            letter_data = letter_datum.split('\t')
            if len(letter_data) == 2:
                letters[letter_data[0]] = letter_data[1]
        # Reading the words
        word_block = word_block.split("\n")
        for word_datum in word_block:
            word_data = word_datum.split('\t')
            if len(word_data) == 2:
                words[word_data[0]] = word_data[1]
        return {'letters': letters, 'words': words}




    def build_result_file(self, new_corpus_directory):
        """
        The result file we have to create is made of a collection of letters (1,2,3-grams) and words (1,2,3-grams)
        and their proportion in this language.
        :param new_corpus_directory: The directory containing the corpus we have to consider as reference.
        :return:
        """
        files_analyzed = []
        text_files_in_current_folder = [f for f in os.listdir(new_corpus_directory)
                                        if os.path.isfile(os.path.join(new_corpus_directory, f))]
        for text_file in text_files_in_current_folder:
            absolute_path_to_file = os.path.join(new_corpus_directory, text_file)
            files_analyzed.append(FileAnalysis(absolute_path_to_file))

        complete_letter_sum = {}
        total_letter_sum = 0
        for analyse in files_analyzed:
            current_letters = getattr(analyse, 'letters')
            total_letter_sum += getattr(analyse, 'letter_count')
            for letter in current_letters:
                if letter[0] in complete_letter_sum:
                    complete_letter_sum[letter[0]] += letter[1]
                else:
                    complete_letter_sum[letter[0]] = letter[1]
        # We have now all informations about letter repartition in this sub-corpus.

        # Let's do the same with single words.
        complete_word_sum = {}
        total_word_sum = 0
        for analyse in files_analyzed:
            current_words = getattr(analyse, 'words')
            total_word_sum += getattr(analyse, 'word_count')
            for word in current_words:
                if word[0] in complete_word_sum:
                    complete_word_sum[word[0]] += word[1]
                else:
                    complete_word_sum[word[0]] = word[1]

        # Everything needed is done. We can write the file.
        self.write_result_file(
            new_corpus_directory,
            complete_letter_sum,
            total_letter_sum,
            complete_word_sum,
            total_word_sum
        )

    @staticmethod
    def write_result_file(new_corpus_directory='',
                          complete_letter_sum=None,
                          total_letter_sum=0,
                          complete_word_sum=None,
                          total_word_sum=0
                          ):
        file_result = open(os.path.join(new_corpus_directory, 'results.txt'), 'a')
        file_result.write('---' + "\n")
        # Inscription of letters repartition
        for letter in complete_letter_sum:
            file_result.write(str(letter) + "\t" + str(complete_letter_sum[letter]/total_letter_sum) + "\n")
        # Inscription of words repartition
        file_result.write('---' + "\n")
        for word in complete_word_sum:
            file_result.write(str(word) + "\t" + str(complete_word_sum[word]/total_word_sum) + "\n")
        file_result.write('---' + "\n")
        file_result.close()

    def get_list_language_directories(self):
        # The first one is the parent directory, we have to omit it.
        count = 0
        for language_directory in os.walk(self.language_corpus_directory):
            if count > 0:
                self.language_directories_list.append(language_directory[0])
            count += 1
