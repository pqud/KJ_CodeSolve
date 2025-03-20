cards=[]


def card_select(temp, count, start):
    if count == 3:
        yield temp
        return
    
    for i in range(start, len(cards)):
        yield from card_select(temp + [cards[i]], count + 1, i + 1)

if __name__=="__main__":
    N, M = map(int,input().split())


    row= list(map(int, input().split()))

    for i in row:
        cards.append(i)


    answer=0
    for j in card_select([],0,0):
        print(j)
        hap=sum(j)
        if hap<=M and answer<hap:
            answer=hap
    print(answer)