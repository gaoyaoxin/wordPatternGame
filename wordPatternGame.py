#!/usr/bin/python
# -*- coding: <utf-8> -*-

import random
import wordPatterns, wordLengths

def getWordPattern(word):
	# Returns a string of the pattern form of the given word.
	# e.g. '0.1.2.3.4.1.2.3.5.6' for 'DUSTBUSTER'
	word = word.upper()
	nextNum = 0
	letterNums = {}
	wordPattern = []

	for letter in word:
		if letter not in letterNums:
			letterNums[letter] = str(nextNum)
			nextNum += 1
		wordPattern.append(letterNums[letter])
	return '.'.join(wordPattern)



def generateWord(wordLength):
	global wordGenerated
	wordGenerated = wordLengths.allLengths[wordLength][random.randint(0, len(wordLengths.allLengths[wordLength]) - 1)]
	global wordGeneratedPattern
	wordGeneratedPattern = getWordPattern(wordGenerated)
	print(wordGenerated.lower())
	return wordGenerated

while 1:
	wordLengthInput = input('Please input word length (3-22, 28):\n> ')
	wordLengthInput = int(wordLengthInput)

	generateWord(wordLengthInput)

	userAnswerWord = input('Please input a word with the same pattern or 0 if no word meets the requirement.\n> ')

	userAnswerWordPattern = getWordPattern(userAnswerWord)

	if userAnswerWordPattern == wordGeneratedPattern:
		print('You win!')
	elif userAnswerWord == '0':
		allOtherPossibleWordsInThisPattern = (wordPatterns.allPatterns[wordGeneratedPattern])
		allOtherPossibleWordsInThisPattern.remove(wordGenerated)
#		print(allOtherPossibleWordsInThisPattern)
		if allOtherPossibleWordsInThisPattern == None:
			print('You win!')
		if allOtherPossibleWordsInThisPattern != None:
			print('You lose! There are other words in this pattern:')
			print(allOtherPossibleWordsInThisPattern)