# -*- coding:Utf-8 -*-

import pathlib
import os

from analysis.file_analysis import FileAnalysis


class CorpusComparison(object):
    """
    The class attributes a score to each word of the unknown file using the frequency of its apparitions in all the
    different languages of the corpus.
    """

    def __init__(self, unknown_file_statistics, corpus_statistics):

        self.unknown_file_statistics = unknown_file_statistics
        self.corpus_statistics = corpus_statistics

        for word in getattr(self.unknown_file_statistics, 'words'):
            #print(word)
            pass

        for results_file in getattr(self.corpus_statistics, 'languages_statistics'):
            print(results_file)

        def compare_to_corpus(self):
            # We have computed all results. Now, we have to match the language corpus with our unknown text
            for language_result_file in self.languages_statistics:
                print(language_result_file)
                # print(len(self.languages_statistics[language_result_file]['words']))
                print(self.languages_statistics[language_result_file]['words']['le'])

                # print(self.languages_statistics[language_result_file]['words'])
