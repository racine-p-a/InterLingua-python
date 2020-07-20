# -*- coding:Utf-8 -*-

from InterfaceIL.InterfaceIL import *


def display_manual():
    print('Use in console : ')
    print('python3 interlingua.py /absolute/File/Location.txt word_precision')
    print('Where :')
    print('- « /absolute/File/Location.txt » refers to the path to the file you want to analyse.')
    print('- « word_precision » refers to the number of most common words you want to compare to other languages. '
          '(choose 25 if you have no idea, it is a good middle-point.)')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        monInterface = InterfaceIL()
        monInterface.root.mainloop()
        exit()

    elif len(sys.argv) == 3:
        file_statistics = FileAnalysis(sys.argv[1])
        languages_scores = getattr(
            CorpusComparison(file_statistics, CorpusLanguageAnalysis(), int(sys.argv[2])),
            'languages_scores'
        )
        response = {}
        for language_result_file in languages_scores:
            response[os.path.basename(os.path.dirname(language_result_file))] = languages_scores[language_result_file]
        print(response)
        exit()

    else:
        display_manual()
        exit()
