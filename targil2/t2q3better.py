import re

file = open('shakespeare.txt', 'r')
content = file.read()
file.close()
words = content.replace('-', ' ')
words = words.replace('\n', ' ')
words = words.replace(':', ' ')
words = words.replace(',', ' ')
words = words.replace('"', ' ')
myL = words.split(' ')
d = {}
for i in range(len(myL)):
	word = myL[i]
	if str(word) in d:
		d[str(word)] += 1
	else:
		d[str(word)] = 1

print(d)