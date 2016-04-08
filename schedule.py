def function(word):
	list = []
	A = word.find("LEC")
	if (A>=0):
		list.append(A)
	A = word.find("LAB")
	if (A>=0):
		list.append(A)
	A = word.find("T/D")
	if (A>=0):
		list.append(A)
	print list
	word = word[min(list):]
	print word
	return word

fr = open('fr', 'r')
fw = open('fw', 'w')
for line in fr:
	fw.write(function(line))
