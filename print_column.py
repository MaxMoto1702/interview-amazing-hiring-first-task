##########################################################################
# Данный код будет обрабатывать несколько файлов с разными разделителями #
# НО в данном коде минимальная защита для ошибочный вводов параметров    #
##########################################################################

import sys

##########################################################################

def manual():
    return """
   python <this_scpipt_name> "<file1> <file2> ... <fileN>" "<separate1><separate2>...<separateN>" number_column
    OR
   python <this_scpipt_name> <file1> <separate1> number_column

    EXAMPLE
   python <this_scpipt_name> text.txt " " 2
    """
##########################################################################

def print_column(file_name, separates, number_column):
    file = open(file_name)
    for line in file:
        if len(separates) > 1:
            for i in range(1, len(separates)):
                line.replace(separates[i], separates[0])
        words = line.split(separates[0])
        if len(words) >= 3:
            print(words[number_column - 1])
    file.close()
##########################################################################

if len(sys.argv) != 4:
    print(manual())
else:
    if not sys.argv[3].isdigit():
        print(manual())
    else:
        file_names = sys.argv[1].split(" ")
        separates = sys.argv[2]
        number_column = int(sys.argv[3])
        for file_name in file_names:
            print_column(file_name, separates, number_column)

##########################################################################
