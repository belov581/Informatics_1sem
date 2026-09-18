import numpy
import matplotlib
import pandas
import scipy
#1
'''n=int(input())
a=1
b=1
p=0
for i in range(3, n+1):
    p=a+b
    a=b
    b=p
print(p)'''
#2
n=int(input())
def f(x):
    for i in range(2, x):
        if x%i==0:
            b=[e for e in range (2, i) if i%e==0]
        if len(b)==0:
            return i
        else:
            return []

print(f(n))

