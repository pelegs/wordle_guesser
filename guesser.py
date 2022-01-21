#!/usr/bin/env python3
# -*- coding: iso-8859-15 -*-

"""
Regex for the win! (not guaranteed)
Use the guess function to get candidates for a
wordle word (English words containing 5 letter).

Arguments:
    - forbiden: list of greyed-out letters.
    - otherplace: yellow letters separated by commas.
      put '_' where no hint is given
      (e.g. '_,s,_,t,_' means that 's' is not in 2nd place
       and 't' is not in 4th place)
    - known: green letters separated by commas.
      (e.g. 'r,_,_,_,t' means that 'r' is in the 1st place
       and 't' in the last place)
"""


from string import ascii_lowercase as letters
import re


empty_known = [None]*5


def only_uses_letters_from(s1, s2):
    """
    Check if all letters in s1 are also in s2.
    Taken from: https://stackoverflow.com/questions/28997056/return-true-if-all-characters-in-a-string-are-in-another-string/28997088
    """
    return set(s1) <= set(s2)


def guess(forbiden=[], known=empty_known, otherplace=[]):
    """
    Returns possible words per given specifications.
    """
    known = [c if c != '_' else None for c in known.split(',')]
    otherplace = [c if c != '_' else ' ' for c in otherplace.split(',')]
    allowed = ''.join([c for c in letters if c not in forbiden])
    rules = [c if c is not None else '[{}]'.format(allowed.replace(x, ''))
             for c, x in zip(known, otherplace)]
    regex = f'{rules[0]}{rules[1]}{rules[2]}{rules[3]}{rules[4]}'
    found = re.findall(regex, words)
    exist = ''.join(set([x for x in otherplace if x != ' ']))

    return [f for f in found if only_uses_letters_from(exist, f)]


with open('5_letters.txt', 'r') as f:
    words = [line.rstrip('\n') for line in f]
words = ' '.join([f'"{w}"' for w in words])


if __name__ == '__main__':
    found = guess(
                forbiden='heatdnbs',
                otherplace='_,_,_,_,_',
                known='_,r,i,_,k',
            )
    print('Possible words: {}.'.format(', '.join(found)))
