# 알고리즘 책 보고 해결함




def set(i,N) :
    global count
    for j in range(N): 
        if (not flag_a[j] and  # j행에 퀸이 없고
            not flag_b[i+j] and # 좌하단/우상단에 퀸이 없고
            not flag_c[i-j+N-1]): #우하단/좌상단에 퀸이 없다면
            pos[i]=j
            if i ==N-1:
                count+=1
            else:
                flag_a[j]=flag_b[i+j]=flag_c[i-j+N-1]=True
                set(i+1,N)
                flag_a[j]=flag_b[i+j]=flag_c[i-j+N-1]=False

        
N=int(input())
pos=[0]*N
flag_a=[False]*N # 각 행에 퀸을 두었는가?
flag_b=[False]*((N*2)-1) # 좌하단/우상단에 퀸이 있는가?
flag_c=[False]*((N*2)-1) # 우하단/좌상단에 퀸이 있는가?

count=0

set(0,N)
print(count)