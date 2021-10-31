#!/usr/bin/python3

for i in range(100,999):
    Huns=i/100;Tens=(i%100)/10;Digits=i%10
    Huns=int(Huns);Tens=int(Tens)
    num=(Huns*Huns*Huns)+(Tens*Tens*Tens)+(Digits*Digits*Digits)
    if(num==i):
        print(i,end=" ")
    i+=1