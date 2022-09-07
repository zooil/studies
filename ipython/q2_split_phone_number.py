''' 
3-1. 변수 pn 에 전화번호가 문자열로 “010-1234-5678”와 같이 저장되어 있다고 
가정하자. 변수 a에 두 번째 번호를 변수 b에 세 번째 번호를 각각 저장하라.
'''

pn = '010-1234-5678'
pList = pn.split('-')
print(pList)
a = pList[1]
print(f'a is {a}')
b = pList[2]
print(f'b is {b}')
