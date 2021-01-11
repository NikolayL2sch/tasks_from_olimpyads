import math
import sys

def rem(x):
    for elem in de:
        if elem == x:
            elem = -1
        elif math.gcd(elem,x)>1:
            elem-=1


n = int(input())
m = [i for i in range(1,2*n+1)]
de = [0]*(2*n)
for i in range (2*n):
    for j in range (2*n):
        if i!=j:
            if math.gcd(m[i],m[j])>1:
                de[i]+=1
print(de)
for i in range(n-1):
    x = int(input())
    rem(x)
    ans = m[de.index(max(de))]    
    print(ans)
    rem(ans)
    sys.stdout.flush()




'''x1,y1,x2,y2 = map(int,input().split())
if x1 == x2 or y1 == y2:
    print('oo')
else:
'''
