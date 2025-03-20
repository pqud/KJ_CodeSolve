from collections import deque
from typing import Any

class Stack:
    def __init__(self, maxlen= 256):
        self.capacity=maxlen
        self.__stk=deque([], maxlen)

    def is_empty(self):
        return not self.__stk
    
    def push(self, value: Any):
        self.__stk.append(value)

    def pop(self):
        return self.__stk.pop()

def hanoi(n, start, end, sub):
    s=Stack(n)

    while True:

        
        if n>0:
            s.push([n,start,end,sub])
            n=n-1
            end,sub=sub,end
            continue

        if not s.is_empty():
            n, start, end, sub= s.pop()
            print(start, end)
            n=n-1
            start,sub=sub,start
            continue
        break

n = int(input())

# n >= 20일 때는 O(1) 연산만 수행하여 빠르게 처리
if n > 20:
    print(2**n - 1)
else:
    print(2**n - 1)
    hanoi(n, 1, 3, 2)
