#!/usr/bin/python3

a,n=(input().split())
A=a
n=int(n)
S=int(0)
for i in range(n):
    S+=int(A)
    A += a
print(S)