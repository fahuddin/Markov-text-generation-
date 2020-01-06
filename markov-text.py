#
# ps7pr2.py (Problem Set 7, Problem 3)
#
# 2-D Lists
#
# Computer Science 111
#
# If you worked with a partner, put his or her contact info below:
# partner's name: Gordon Ng
# partner's email: gng8@bu.edu
# 

# IMPORTANT: This file is for your solutions to Problem 3.
# Your solutions to problem 3 should go in ps7pr3.py instead.
import random
def word_frequencies(filename):
    """ uses the text file with the specified filename to create and return
        a dictionary of word frequencies for words in that text file.
        input: filename is a string specifying the name of a text file,
               which we assume is in the same folder as this Python file
    """
    file = open(filename, 'r')
    text = file.read()      # read it all in at once!
    file.close()

    words = text.split()

    d = {}

    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1

    return d
     
def create_dictionary(filename):
    """creates dictionary"""
    file = open(filename, 'r')
    text = file.read()
    words = text.split()
    file.close()
    d = {}
    current_word = '$'
    for next_word in words:
        if current_word not in d:
            d[current_word] = [next_word]
        else:
            d[current_word] += [next_word]
        if next_word[-1] in '.?!':
            current_word = '$'
        else:
            current_word = next_word
    return d

def generate_text(word_dict, num_words):
    """generates linked dictionaries"""
    current_word = '$'
    while num_words > 0:
        num_words -= 1
        wordlist = word_dict[current_word]
        next_word = random.choice(wordlist)
        print (next_word, end=' ')
        if next_word[-1] in '.?!':
            current_word = '$'
        else:
            current_word = next_word


