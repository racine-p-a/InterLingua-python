# -*- coding:Utf-8 -*-

import pathlib
import os


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

        # Get folder list.
        root_directory = pathlib.Path(__file__).parent.parent.absolute()
        self.language_corpus_directory = os.path.join(root_directory, 'corpus/languages')
        # Get all languages sub-folders.
        self.get_list_language_directories()
        # For each language folder, analyze the corpus.
        self.analyze_languages()

    def analyze_languages(self):
        for language_folder in self.language_directories_list:
            # First get all files in the folder.
            onlyfiles = [f for f in os.listdir(language_folder) if os.path.isfile(os.path.join(language_folder, f))]
            print(language_folder)
            print(onlyfiles)


    def get_list_language_directories(self):
        # The first one is the parent directory, we ave to omit it.
        count = 0
        for language_directory in os.walk(self.language_corpus_directory):
            if count > 0:
                self.language_directories_list.append(language_directory[0])
            count += 1
