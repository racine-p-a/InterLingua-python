# -*- coding:Utf-8 -*-


class CorpusComparison(object):
    """
    The class attributes a score to each word of the unknown file using the frequency of its apparitions in all the
    different languages of the corpus.
    """

    def __init__(self, unknown_file_statistics, corpus_statistics, word_precision=25):

        self.unknown_file_statistics = unknown_file_statistics
        self.corpus_statistics = corpus_statistics
        self.word_precision = word_precision

        self.languages_scores = {}

        # First of all, we prepare the list of available languages.
        for language_result_file in getattr(self.corpus_statistics, 'languages_statistics'):
            self.languages_scores[language_result_file] = 0

        # Now, we browse each word of the unknown file and we compare its frequency in this file to its frequencies
        # in the corpus files.
        count = 0
        for word, word_occurencies in getattr(self.unknown_file_statistics, 'words'):
            if count >= self.word_precision:
                break
            current_word_frequency = int(word_occurencies)/getattr(self.unknown_file_statistics, 'word_count')
            # print(word, word_occurencies, current_word_frequency)
            for language_result_file in getattr(self.corpus_statistics, 'languages_statistics'):
                current_language_words = getattr(
                    self.corpus_statistics,
                    'languages_statistics'
                )[language_result_file]['words']
                if word in current_language_words:
                    # The word has been found in the current language. Let's add the difference of frequencies to the
                    # language variation.
                    self.languages_scores[language_result_file] += abs(
                        float(current_word_frequency) - float(current_language_words[word])
                    )
                else:
                    # The word does not exist in the current language. Let's add the complete score to the variation.
                    self.languages_scores[language_result_file] += current_word_frequency
            count += 1

    def display_scores(self):
        """
        Displays languages scores in console.
        :return:
        """
        for language in self.languages_scores:
            print(str(language) + " : " + str(self.languages_scores[language]))
