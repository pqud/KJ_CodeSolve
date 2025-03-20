

Hap_ways=[0]*11

Hap_ways[1]=1
Hap_ways[2]=2
Hap_ways[3]=4

for i in range(4, 11):
    Hap_ways[i]=sum(Hap_ways[i-3:i])

T = int(input())
for i in range(T):
    n=int(input())

    print(Hap_ways[n])
