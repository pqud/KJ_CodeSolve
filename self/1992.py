

array=[]

def Split(graph, n):


    array.append("(")

    if n == 1:
        return [graph[0][0]]
    
    n = n // 2
    q1 = [[val for val in row[:n]] for row in graph[:n]] # 1사분면
    q2 = [[val for val in row[n:]] for row in graph[:n]] # 2사분면
    q3 = [[val for val in row[:n]] for row in graph[n:]] # 3사분면
    q4 = [[val for val in row[n:]] for row in graph[n:]] # 4사분면
    
    quad=[q1, q2, q3, q4]

    # print(f"quad는: {quad}")
    
    for q in quad:
        # 전부 0이라면 값 다 합쳤을때 0이고
        total=sum(sum(row) for row in q)
        if total ==0:
            array.append("0")
        # 전부 1이라면 값 다 합쳤을때 n*n과 같아야 하고
        elif total == n*n:
            array.append("1")
        # 그게 아니라면 스플릿
        else:
            Split(q, n)

    array.append(")")   
    
    return [q1, q2, q3, q4]


if __name__=="__main__":
    N=int(input())
    
    graph=[[0]*N for _ in range(N)]

    for i in range(N):
        row = input()
        for j in range(N):
            graph[i][j]=int(row[j])

    if N==1:
        print(graph[0][0])
    else:

        Split(graph, N)
        #array에 있는값이 1 ( ) 뿐이라면
        if "0" not in array:
            print("1")
        #array에 있는 값이 0 ( ) 뿐이라면
        elif "1" not in array:
            print("0")
        # 그게 아니라면 스플릿
        else:
            for item in array:
                print(item,end="")
 