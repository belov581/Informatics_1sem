import numpy
import matplotlib
import pandas
import scipy

#1
'''a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)

#2
a=input()
print(a[-1])'''

#3
'''a=list(map(int,input().split()))
t=1
for y in a:
    t=t*y
print(t**(1/len(a)))'''

#4
'''a=open('input.txt').readlines()
m=[]
n=[]
for r in a:
    r=r.split()
    for el in r:
        if str(el) in '0123456789':
            m.append(el)
        else:
            n.append(el)
print(m)
s=''
while len(m)>1:
    s=s+str(m[0])+str(n[0])
    m=m[1:]
    print(m)
s=s+m[0]
print(s)
d=eval(s)
print(d)
f=open('output.txt', 'w')
f.write(str(d)+'\n')
f.close()'''

#5
'''a=list(map(int, input().split()))
N=a[0]
b=a[1]
c=a[2]
s=int(str(N), b)
g=0
m=''
while s!=0:
    g=s%c
    m=str(g)+m
    s=s//c
print(int(m))'''

#6
a=open('input.txt').readlines()
m=[]
m1=[]
for r in a:
    r=r.split()
    for el in r:
        if el in '+-*':
            m1.append(el)
        elif 1<=int(el)<=10:
            m.append(el)
print(m1)
h=m[-1]  # система счисления
m=m[:-1]  # массив с числами в сч h
s=[]
for el1 in m:
    f=int(str(el1), int(h))
    s.append(f)  # массив числами в сч 10
t=''
while len(s)>1:
    t=t+str(s[0])+str(m1[0])
    s=s[1:]
t=t+str(s[-1])
d=eval(t)
g1=0
m5=''
while d!=0:
    g1=d%int(h)
    m5=str(g1)+m5
    d=d//int(h)
f=open('output.txt', 'w')
f.write(str(m5)+'\n')
f.close()






