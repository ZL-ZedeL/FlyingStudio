#因为输入格式很恶心，我又暂时不会正则表达式，
#因此此处关于正则表达式的代码并非由自己完成(由室友帮忙完成)
#相关代码由##标记并由空一行结束

#!/usr/bin/python3
import datetime
##
import re

d1=datetime.datetime(2000,1,1)
y_m_d=input()
##
year=re.search('(\d*).',y_m_d).group(1)
month=re.search('(\d*).(\d*).(\d*)',y_m_d).group(2)
day=re.search('(\d*).(\d*).(\d*)',y_m_d).group(3)
#print(year,month,day)

year=int(year);month=int(month);day=int(day)
d2=datetime.datetime(year,month,day)
##
temp=str(d2-d1)
ans=re.search('(\d*) day',temp).group(1)
ans=int(ans)+1
print(ans)