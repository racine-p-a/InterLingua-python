# -*- coding:Utf-8 -*-


class CorpusLanguageAnalysis(object):
    """
    Representation of a file and manages all computations ad operations required.
    """
    def __init__(self):
        """
        At class call, we have to follow these steps :
        - make a list of all folders in the language corpus
        - check if a result file already exists :
            - it exists -> we keep it
            - it does not exist -> we analyse the texts inside the folder and create the file with the result
        """
        # Get folder list
        print('yo')
