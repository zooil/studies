import random
from pynput import keyboard


def on_release(key):
    print('Key %s released' %key)
    if key == keyboard.Key.space: 
        checkWord()
    if key == keyboard.Key.esc: #esc 키가 입력되면 종료
        return False

def checkWord():
	f	= open("japan_word.txt", 'r')
	lines	= f.readlines()
	lineLen	= len(lines)
	randNum	= random.randint(0,lineLen)
	wordList= lines[randNum].strip().split('\t')
	wordList[0].strip()
	print(wordList)
	f.close()

 # 리스너 등록방법1
with keyboard.Listener(
    on_release=on_release) as listener:
    listener.join()



