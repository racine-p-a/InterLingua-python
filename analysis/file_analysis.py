# -*- coding:Utf-8 -*-

import re


class FileAnalysis(object):
    """
    Representation of a file and manages all computations ad operations required.
    """

    def __init__(self, file_location=""):
        """
        The constructor just open the file in file_location, reads it and analyse it on the go.
        Informations to extract :

        - number of letters         DONE
        - number of lines           DONE
        - number of words           DONE
        - list of letters frequency DONE
            - monograms             DONE
            - bigrams               DONE
            - trigrams              DONE
        - list of words frequency   DONE
            - monograms             DONE
            - bigrams               DONE
            - trigrams              DONE
        - mean size of words        DONE
        """
        self.letter_count = 0
        self.line_count = 0
        self.word_count = 0
        self.letters = {}
        self.bigrams = {}
        self.cumulated_sum_of_bigrams = 0
        self.trigrams = {}
        self.cumulated_sum_of_trigrams = 0
        self.words = {}
        self.word_bigrams = {}
        self.cumulated_sum_of_word_bigrams = 0
        self.word_trigrams = {}
        self.cumulated_sum_of_word_trigrams = 0
        self.mean_size_of_words = 0

        print(file_location)
        file_opener = open(file_location, 'r')
        file_content = file_opener.read().lower()

        # Letter count
        self.letter_count = len(file_content)

        # Line count
        self.line_count = len(file_content.split("\n"))

        # Word count
        word_list = re.findall(r"[\w']+", file_content)
        self.word_count = len(word_list)

        # Counting monograms, bigrams and trigrams of letters.
        penultimate_letter = ''
        last_letter = ''
        for letter in file_content:
            # Monograms
            if letter in self.letters:
                self.letters[letter] += 1
            else:
                self.letters[letter] = 1
            # Bigrams
            if last_letter != '':
                if (last_letter + letter) in self.bigrams:
                    self.bigrams[last_letter + letter] += 1
                else:
                    self.bigrams[last_letter + letter] = 1
                self.cumulated_sum_of_bigrams += 1
            # Trigrams
            if last_letter != '' and penultimate_letter != '':
                if (penultimate_letter + last_letter + letter) in self.trigrams:
                    self.trigrams[penultimate_letter + last_letter + letter] += 1
                else:
                    self.trigrams[penultimate_letter + last_letter + letter] = 1
                self.cumulated_sum_of_trigrams += 1

            penultimate_letter = last_letter
            last_letter = letter
        # Sorting the dictionnaries.
        self.letters = sorted(self.letters.items(), key=lambda x: x[1], reverse=True)
        self.bigrams = sorted(self.bigrams.items(), key=lambda x: x[1], reverse=True)
        self.trigrams = sorted(self.trigrams.items(), key=lambda x: x[1], reverse=True)

        # Counting monograms, bigrams and trigrams of words.
        cumulated_length_of_words = 0
        penultimate_word = ''
        last_word = ''
        for word in word_list:
            cumulated_length_of_words += len(word)
            # Monograms of words
            if word in self.words:
                self.words[word] += 1
            else:
                self.words[word] = 1

            # Bigrams of words
            if last_word != '':
                if(str(last_word), str(word)) in self.word_bigrams:
                    self.word_bigrams[(str(last_word), str(word))] += 1
                else:
                    self.word_bigrams[(str(last_word), str(word))] = 1
                self.cumulated_sum_of_word_bigrams += 1

            # Trigrams of words
            if last_word != '' and penultimate_word != '':
                if (str(penultimate_word), str(last_word), str(word)) in self.word_trigrams:
                    self.word_trigrams[(str(penultimate_word), str(last_word), str(word))] += 1
                else:
                    self.word_trigrams[(str(penultimate_word), str(last_word), str(word))] = 1
                self.cumulated_sum_of_word_trigrams += 1

            penultimate_word = last_word
            last_word = word
        # Sorting the dictionnaries.
        self.words = sorted(self.words.items(), key=lambda x: x[1], reverse=True)
        self.word_bigrams = sorted(self.word_bigrams.items(), key=lambda x: x[1], reverse=True)
        self.word_trigrams = sorted(self.word_trigrams.items(), key=lambda x: x[1], reverse=True)

        # print('cumulated size : ' + str(cumulated_length_of_words))
        # print('word quantity : ' + str(len(word_list)))
        self.mean_size_of_words = cumulated_length_of_words/len(word_list)
        # self.display_results()

    def display_results(self):
        print('letter count : ' + str(self.letter_count))
        print('line count : ' + str(self.line_count))
        print('word count : ' + str(self.word_count))
        print(self.letters)
        print(self.bigrams)
        print(self.trigrams)
        print(self.words)
        print(self.word_bigrams)
        print(self.word_trigrams)
        print('Mean size of words : ' + str(self.mean_size_of_words))
        print('done')
