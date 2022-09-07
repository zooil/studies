import random, keyboard

f	= open("japan_word.txt", 'r')
lines	= f.readlines()
lineLen	= len(lines)

while True:
	if keyboard.read_key() == 'space':
		randNum	= random.randint(0,lineLen-1)
		wordList= lines[randNum].strip().split('\t')
		print(wordList)
		break

f.close()

