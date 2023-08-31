import os

filename = 'alice.txt'
try:
    with open(filename, 'r') as f:
        txt = f.read()
        num_words = len(txt.split())
        print('The file ' + filename + ' contains ' + str(num_words) + ' words.')
except FileNotFoundError:
    print('The file ' + filename + ' does not exist.')

