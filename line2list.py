import re

lineRegex = re.compile(r'''(
		(.{1,})
		(\n){1}
		)''', re.VERBOSE)

fo = open('dictionary.txt')
data = fo.read()
fo.close()

matches = []
for groups in lineRegex.findall(data):
	word = groups[1]
	matches.append(word)

fo = open('entryList.py', 'w')
data = 'wordList = ' + str(matches)
fo.write(data)
fo.close
