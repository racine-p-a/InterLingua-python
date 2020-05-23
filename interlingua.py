# -*- coding:Utf-8 -*-

from InterfaceIL.InterfaceIL import *


def display_manual():
    print('Use in console : ')
    print('python3 interlingua.py /absolute/File/Location.txt')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        monInterface = InterfaceIL()
        monInterface.root.mainloop()

    elif len(sys.argv) == 2:
        # todo
        pass

    else:
        display_manual()
