#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Regex for the win! (not guaranteed)
Use the guess function to get candidates for a wordle word: words containing
N letters. The number and language of the letters are determined by a provided
list of possible words.

Arguments:
	- wordsList (-w): the file containing the list of words.
	- forbidden (-f): list of greyed-out letters.
	- otherPlace (-o): yellow letters separated by '|'.
	  put '?' where no hint is given
	  (e.g. '?|s|?|t|?' means that 's' is not in 2nd place
	   and 't' is not in 4th place)
	- known (-k): green letters separated by '|'.
	  (e.g. 'r|?|?|?|t' means that there is an 'r' in the 1st place
	   and a 't' in the last place)

If no arguments are given, the script returns a random word.
"""


import re
import argparse
import random


def only_uses_letters_from(s1, s2):
    """
    Check if all letters in s1 are also in s2.
    Taken from: https://stackoverflow.com/questions/28997056/
    return-true-if-all-characters-in-a-string-are-in-another-string/28997088
    """
    return set(s1) <= set(s2)


def guess(words='', letters='', forbidden=[],
          known=[], otherPlace=[], num_letters=5):
    """
    Returns possible words per given specifications from given words list'
    """
    known = known.split('|')
    otherPlace = otherPlace.split('|')
    allowed = ''.join(sorted([c for c in letters if c not in forbidden]))
    rules = [''.join([c for c in allowed if c not in set(o)])
             if a == '?' else a for a, o in zip(known, otherPlace)]
#    regex = f'{[rules[0]]}{[rules[1]]}{[rules[2]]}{[rules[3]]}{[rules[4]]}'
    regex = ''.join(f'[{rule}]' for rule in rules)
    found = re.findall(regex, words)
    exist = ''.join(set([x for x in otherPlace if x != '?']))

    if args.verbose:
        print('forbidden:', forbidden)
        print('known:', known)
        print('otherPlace:', otherPlace)
        print('allowed:', allowed)
        print('rules:', rules)

    return [f for f in found if only_uses_letters_from(exist, f)]


# Arguments
parser = argparse.ArgumentParser()
parser.add_argument('-w', '--wordsList', type=str,
                    default='en.txt', help='words list file')
parser.add_argument('-f', '--forbidden', type=str,
                    default='', help='forbidden letters')
parser.add_argument('-o', '--otherPlace', type=str,
                    default='', help='letters that are in the word, '\
                    'but in a different place')
parser.add_argument('-k', '--known', type=str,
                    default='', help='known letters')
parser.add_argument('--verbose', dest='verbose', action='store_true',
                    help='show all data')
args = parser.parse_args()

# Words file
with open(args.wordsList, 'r') as f:
    wordsList = [line.rstrip('\n') for line in f]
wordsStr = ' '.join([f'"{w}"' for w in wordsList])

# Set number of letters vis words file
num_letters = len(wordsList[0])

# Set default values for known and other
otherPlaceEmpty, knownEmpty = [False, False]
if args.otherPlace == '':
    args.otherPlace = '|'.join(['?']*num_letters)
    otherPlaceEmpty = True
if args.known == '':
    args.known = '|'.join(['?']*num_letters)
    knownEmpty = True

# Set letters via words file
all_letters = ''.join(list(set(''.join(wordsList))))


if __name__ == '__main__':
    if args.forbidden == '' and otherPlaceEmpty and knownEmpty:
        print('Random word: {}.'.format(random.choice(wordsList)))
    else:
        found = guess(
                    words=wordsStr,
                    letters=all_letters,
                    forbidden=args.forbidden,
                    otherPlace=args.otherPlace,
                    known=args.known,
                    num_letters=num_letters,
                )
        print('Possible words: {}.'.format(', '.join(found)))
