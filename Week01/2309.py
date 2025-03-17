def find_nan(nan, target_value):
    for i in range(9):
        j=i+1
        
        while j<9:

            if nan[i]+nan[j]==target_value:
                #i가 무조건 j보다 작으니까 j삭제하고 i지우면 문제없을듯? 
                nan.remove(nan[j])
                nan.remove(nan[i])

                return 
                
            else:
                j+=1


if __name__=="__main__":

    nan=[]

    total=0

    for i in range(9):
        a=int(input())
        nan.append(a)
        total+=a

    target_value=total-100

    find_nan(nan, target_value)

    nan.sort()

    for nans in nan:
        print(nans)
    
