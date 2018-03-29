#!/usr/bin/python
# -*- coding: <utf-8> -*-

import re

fileNameInput = input('Please input file name (without .txt)\n> ')
fileName = fileNameInput + '.txt'

fo = open(fileName,'r')
data = fo.read()
fo.close()

dictRegex = re.compile(r'''(
	([^\t\n]{1,})
	(\t)
	([^\t\n]{1,})
	)''', re.VERBOSE)


matches = []
for groups in dictRegex.findall(data):
	newDictEntry = '\'' + groups[1] + '\': \'' + groups[3] + '\''
	matches.append(newDictEntry)


data = ', '.join(matches)

fileName_dict = fileNameInput + '_dict.txt'
fo = open(fileName_dict, 'w')
fo.write(data)
fo.close()

print('Done!')