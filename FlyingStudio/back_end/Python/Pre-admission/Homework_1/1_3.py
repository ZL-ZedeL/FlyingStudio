#!/usr/bin/python3

year=input()
year=int(year)
B=bool(1)
if (year%4==0 or (year%4!=0 and year%400==0)):
    B=True
else:
    B=False
print(B)