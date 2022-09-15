import random
from pynput import keyboard


def on_release(key):
#    print('Key %s released' %key)
    if key == keyboard.Key.space: 
        checkWord()
    if key == keyboard.Key.esc: #esc 키가 입력되면 종료
        return False

def checkWord():
	f	= open("cherry01.txt", 'r')
	lines	= f.readlines()
	lineLen	= len(lines)
	randNum	= random.randint(0,lineLen-1)
	wordList= lines[randNum].strip().split(',')
	wordList[0] = wordList[0].strip()
	wordList[1] = wordList[1].strip()
	print(wordList,'\n')
	f.close()

 # 리스너 등록방법1
with keyboard.Listener(
    on_release=on_release) as listener:
    listener.join()



