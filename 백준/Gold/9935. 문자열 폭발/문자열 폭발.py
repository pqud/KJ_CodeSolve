import sys



#string 에서 꺼낸 문자열이 bomb에 있는 문자열이라면 candidates 스택에 넣는다.
# candidates에 문자열 들어올 때 candidates의 상단 k개의 문자를 배교했을떄 bomb와 같으면 펑
# 꺼냈던문자열은 answers 스택에 그냥 넣는데 펑 하면 len(bomb)-1만큼 뺌뺌
# 터지면 candidates에서도도 뺌 

string=list(sys.stdin.readline().strip())
bomb=list(sys.stdin.readline().strip())
bomb.reverse()
answer=[]
candidates=[]


while string:
    s=string.pop()
    answer.append(s)
    if s in bomb:
        candidates.append(s)
        if len(candidates)>=len(bomb):
            if ''.join(candidates[-len(bomb):]) == ''.join(bomb):
                for i in range(len(bomb)):
                    candidates.pop()
                    answer.pop()
    else:
        candidates.append("")
        
if answer:
    answer.reverse()
    print(''.join(answer))
else:
    print("FRULA")