croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
    # replace : 문자열을 변경하는 함수. replace(old,new)
    # croatia alphabet 문자가 입력받은 word에 존재한다면 그 문자를 /로 교체한다.
print(len(word))