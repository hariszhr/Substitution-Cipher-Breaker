try:
    import numpy
except ImportError:
    import subprocess
    subprocess.check_call(["python", '-m', 'pip', 'install', 'numpy']) # install pkg
    subprocess.check_call(["python", '-m', 'pip', 'install',"--upgrade", 'numpy']) # upgrade pkg
    import numpy

from string import ascii_lowercase
from string import ascii_uppercase
import os,inspect

numpy.set_printoptions (suppress=True)

def getFrequencyCounts(rawData):
    frequency_list = [0 for i in range(26)]
    for c in rawData:
        ord_idx=ord(c) - 65
        if(ord_idx >= 0 and ord_idx < 26):
            frequency_list[ord_idx] = frequency_list[ord_idx] + 1

    frequency_char_list = [0 for i in range(26)]

    for i in range(len(frequency_list)):
        frequency_char_list[i] = chr(i + 65)

    frequency_list, frequency_char_list = zip(*sorted(zip(frequency_list, frequency_char_list), reverse=True))

    for i in range(len(frequency_char_list)):
        print(i,":",frequency_char_list[i],"->", frequency_list[i], end="  ,  ")
    print(end="\n")

    return frequency_char_list,frequency_list

def getBigram(rawData, freq_char_list):
    bigram = numpy.zeros((26, 26))
    # create list of all 2-chars
    list_of_2_chars = [''] * (len(rawData) - 1)
    index = 0
    for c in rawData:
        if (index == 0):
            list_of_2_chars[index] = c
        elif index < len(rawData) - 1:
            list_of_2_chars[index - 1] = list_of_2_chars[index - 1] + c
            list_of_2_chars[index] = c
        elif index == (len(rawData) - 1):
            list_of_2_chars[index - 1] = list_of_2_chars[index - 1] + c
        else:
            print('something is wrong')
        index += 1

    # increment bigram counts using 2-chars list
    freq_char_list=list(freq_char_list)
    for entry in list_of_2_chars:
        char1_idx = freq_char_list.index(entry[0])
        char2_idx = freq_char_list.index(entry[1])
        bigram[char1_idx, char2_idx] = bigram[char1_idx, char2_idx] + 1

    # print(bigram)
    # print("total number of 2 chars:"+str(len(list_of_2_chars)))
    bigram = (bigram / len(list_of_2_chars)) * 100
    return bigram


def getTextFromBook():

    inputtxt = ''
    file = open(os.path.dirname(os.path.abspath(inspect.stack()[0][1]))+os.sep+'book.txt', 'r+', encoding='utf-8')
    while True:
        lines = file.readlines()
        if not lines:
            break
        for line in lines:
            inputtxt = inputtxt + line
    file.close()
    return inputtxt

def clean_up(inputtxt):
    # clean the input text
    clean_input=''
    for c in inputtxt:
        if (c in ascii_uppercase or c in ascii_lowercase):
            clean_input = clean_input + c.upper()
    # print('filtered input: ' + clean_input)
    return clean_input
