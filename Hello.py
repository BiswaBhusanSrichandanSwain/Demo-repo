l1=[1,2,3,4,5]
l2=[1,2,3,3,4]
# l3=list(map(lambda x,y:x+y,l1,l2))
# print(l3)
# dic=dict(zip(l1,l2))
# print(dic)
# l3=[]
# for i in l2:
#     if i not in l3:
#         l3.append(i)
# l2=l3
# print(l2)
# s='aaaaaaabbbb'
# s1=[]
# for i in s:
#     if i not in s1:
#         s1.append(i)
# s=''.join(s1)
# print(s)
# s='jewel'
# i=len(s)-1
# print('The Reverse of {} Is:'.format(s))
# while i>=0:
#     print(s[i],end='')
#     i-=1
# name='Jewel Swain'
# count=0
# for i in name:
#     count+=1
#     print('{} occures {} times'.format(i,name.count(i)))
#     # print('{} present in {} index'.format(i,name.index(i)))
# print('The Numeber Of Occurence Is :',count)
# l3=[]
# for i in range(len(l1)):
#     add=l1[i]+l2[i]
#     l3.append(add)
# print(l3)
import re
data_string='06 apr 2021 15:28:30 5 ms 20 ms 600 ms'
s=data_string.split(' ')
print(s)
match=re.fullmatch('\d',s)
print(match)