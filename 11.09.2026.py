import numpy
import matplotlib
import pandas
import scipy
#3
'''a=input()
t=0



if a[len(a)//2] in 'AHIMOTUVWXY18' and a[::-1]==a and '*' not in a and '&'not in a and '!' not in a and '%' not in a:
    print("a is a mirrored palindrome.")
    t=t+1

if t==0 and a[::-1]==a and a[len(a)//2] not in 'AHIMOTUVWXY18' and '*' not in a and '&'not in a and '!' not in a and '%' not in a:
    print("a is a regular palindrome.")
    t=t+1
for el in range (0, len(a)//2+1):
    if t==0 and ((a[el]=='E' and a[-1*el-1]=='3') or (a[el]=='3' and a[-1*el-1]=='E') or (a[el]=='J' and a[-1*el-1]=='L') or (a[el]=='L' and a[-1*el-1]=='J') or (a[el]=='Z' and a[-1*el-1]=='5') or (a[el]=='5' and a[-1*el-1]=='Z') or (a[el]=='S' and a[-1*el-1]=='2') or (a[el]=='2' and a[-1*el-1]=='S')):
        a=a.replace('E', '*')
        a=a.replace('3', '*')
        a=a.replace('J', '*')
        a=a.replace('L', '*')
        a=a.replace('S', '*')
        a=a.replace('2', '*')
        a=a.replace('Z', '*')
        a=a.replace('5', '*')
        if a==a[::-1]:
            print('a is a mirrored string.')
            t=t+1
if t==0:
    print('a is not palindrome')'''

#4
'''a=list(map(int,input().split()))
b=[[a[i], a[i-1]] for i in range(1, len(a), 2)]
print(*b,[a[-1] for el in range(1) if len(a)%2!=0])'''

#5
'''a=list(map(int,input().split()))
print(a[-1:] + a[:-1])'''

#6
'''a=list(map(int,input().split()))
print([x for x in a if a.count(x)==1])'''

#7
'''a=list(map(int,input().split()))
t=0
m=0
for el in a:
    if a.count(el)>t:
        t=a.count(el)
        m=el
print(el)'''

#8
'''n=int(input())
a=list(map(int,input().split()))
for el in a:
    k=0
    p=0
    for el1 in a:
        if el>el1:
            k=k+1
        if el<el1:
            p=p+1
    if k==p:
        print(el)
        break'''


#9
'''with open('input.txt', 'r') as f1:
    s=0
    L=f1.readlines()
    for el in L:
        el=el.replace('...', '*')
        el=el.replace('?!', '&')
        s=s+el.count('*')+el.count('&')+el.count('!')+el.count('?')
print(s)'''

'''#10
with open('input.txt') as f1:
    L=f1.readlines()'''



