import random
from pynput import keyboard


def on_release(key):
    if key == keyboard.Key.space: 
        checkWord()
    if key == keyboard.Key.esc: #esc 키가 입력되면 종료
        return False

def checkWord():
	f	= open("jword.txt", 'r')
	lines	= f.readlines()
	lineLen	= len(lines)
	randNum	= random.randint(0,lineLen)
	str = lines[randNum]
	cnt = 1
	if lineLen == randNum:
		cnt = -1
	while True:
		if '예)' in str:
			break
		else:
			randNum += cnt
			str = lines[randNum]
	print(lines[randNum-1])
	print(lines[randNum])
	print(lines[randNum+1])
	f.close()

 # 리스너 등록방법1
with keyboard.Listener(
    on_release=on_release) as listener:
    listener.join()



