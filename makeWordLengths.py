#!/usr/bin/python
# -*- coding: <utf-8> -*-

import pprint

def main():
	allLengths = {}

	fo = open('dictionary.txt')
	wordList = fo.read().split('\n')
	fo.close()

	for word in wordList:
		# Get the pattern for each string in wordList.
		length = len(word)
		
		if length not in allLengths:
			allLengths[length] = [word]
		else:
			allLengths[length].append(word)

	# This is code that writes code. The wordPatterns.py file contains
	# one very, very large assignment statement.
	fo = open('wordLengths.py', 'w')
	fo.write('allLengths = ')
	fo.write(pprint.pformat(allLengths))
	fo.close


if __name__ == '__main__':
	main()