import sys
sys.setrecursionlimit(10 ** 4)


#find 연산(나중에 u와 v가 같은 트리에 속하는지 찾기 위해서. 같은 트리면 부모가 같다.)
def Find_Set(parent, x):
    if parent[x]!=x: #x의 부모가 x가 아니라면 (즉 x에게 부모가 있다면 )
        parent[x] = Find_Set(parent, parent[x]) #x의 부모의 부모를 찾음 
    return parent[x] 

def Union(parent, a, b):
    a=Find_Set(parent, a)
    b=Find_Set(parent, b)
    #부모가 더 큰 쪽을 새 부모 삼아서 합친다.
    if a<b:
        parent[b]=a
    else:
        parent[a]=b


if __name__=="__main__":

    read = sys.stdin.readline
    v, e = map(int, read().split())

    parent=[x for x in range(v+1)] #부모 테이블 초기화

    edges=[]
    total_cost=0

    for i in range(e):
        u, v, cost=map(int, read().split())
        edges.append((cost,u,v))

    edges.sort()

    for i in range(e):
        cost, u, v= edges[i]
        if Find_Set(parent, u) != Find_Set(parent,v):
            total_cost+=cost
            Union(parent, u, v)

    print(total_cost)