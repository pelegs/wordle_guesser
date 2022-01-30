# Regex for the win!
###### (not guaranteed)

Use the guesser to get candidates for a [wordle](https://www.powerlanguage.co.uk/wordle/) word (words containing 5 letters exactly).

You can use a list of words from any phonetic language: the list file must have all the words, each in its own line. example:

```
aback
abase
abate
abbey
abbot
abhor
abide
abled
abode
abort
...
```

Arguments:  
	- wordsList (-w): the file containing the list of words (default is English).  
	- forbidden (-f): list of greyed-out letters.  
	- otherPlace (-o): yellow letters separated by commas.  
	  Put `_` where no hint is given (e.g. `_,s,_,t,_` means that `s` is not in 2nd place and `t` is not in 4th place)  
	- known (-k): green letters separated by commas.  
	  (e.g. `r,_,_,_,t` means that `r` is in the 1st place and `t` in the last place)  

If no arguments are given, the script returns a random word.

Example of using the script:
![Example image English](https://github.com/pelegs/wordle_guesser/blob/master/example.png)
