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
        - list of words frequency
            - monograms
            - bigrams
            - trigrams
        - mean size of words
        """
        self.letter_count = 0
        self.line_count = 0
        self.word_count = 0
        self.letters = {}
        self.bigrams = {}
        self.trigrams = {}
        print('file location : ' + file_location)
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
        current_trigram = ''
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
            # Trigrams
            if last_letter != '' and penultimate_letter != '':
                if (penultimate_letter + last_letter + letter) in self.trigrams:
                    self.trigrams[penultimate_letter + last_letter + letter] += 1
                else:
                    self.trigrams[penultimate_letter + last_letter + letter] = 1

            penultimate_letter = last_letter
            last_letter = letter

        print('letter count : ' + str(self.letter_count))
        print('line count : ' + str(self.line_count))
        print('word count : ' + str(self.word_count))
        print(self.letters)
        print(self.bigrams)
        print(self.trigrams)



