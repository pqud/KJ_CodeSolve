import sys
import heapq


N=int(sys.stdin.readline())

cards=[]
for i in range(N):
    card=int(sys.stdin.readline())
    cards.append(card)

cards.sort()
answer=0

while len(cards)>1:
    card_1=heapq.heappop(cards)
    card_2=heapq.heappop(cards)

    card_3=card_1+card_2
    answer+=card_3
    heapq.heappush(cards, card_3)


print(answer)