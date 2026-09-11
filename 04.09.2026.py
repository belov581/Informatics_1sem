import numpy
import matplotlib
import pandas
import scipy
#1

'''a=list(map(int,input().split()))
h=a[0]
a=a[1:]
b=(1+h)//2*(len(a)+1)
print(b-sum(a))'''

#2
'''a=input()
r=int(a[0])
d=a[1:]
e1=''
while d!='':
    e=d[:r]
    e1=e1+e[::-1]
    d=d[r:]
print(e1)'''

#3
s=input()
if s==s[::-1]:
    print('s is a regular palindrome')

