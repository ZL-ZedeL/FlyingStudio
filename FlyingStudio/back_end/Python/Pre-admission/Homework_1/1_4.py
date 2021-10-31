#!/usr/bin/python3

n=input()
n=num=int(n)
isPrime=bool(1)
for div in range(2,n):
    if (num%div==0):
        isPrime=False
    else:
        isPrime=True
    div+=1
print(isPrime)