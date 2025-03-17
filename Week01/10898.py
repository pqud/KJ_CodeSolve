counter = [0] * 10000
                
if __name__ == "__main__":
    N = int(input())  

    for i in range(N):
        a= int(input())
        counter[a-1]+=1


    for i in range(10000):
        if counter[i]!=0:
            for _ in range(counter[i]):
                print(i+1)



# 입력은 N개이고 숫자는 기껏해야 만까지임.
# 그럼 동일한 입력에 대한 개수를 센다면?
# 10개씩 나온다고 쳤을 때 


# 일단 배열[10000]을 만들고
# 배열[i]가 나오면 배열[i]+=1을 함
# 그리고 배열을 순회하면서 배열[i]==0이면 스킵킵

