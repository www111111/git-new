
'''
list1=[{'beingjing':{'mainji':'1000ping','renkou':'200w'},'sahnghai':{'mainji':'600ping','renkou':'150w'}}]

for i in list1:
    print(i)
    for a in i:
        if(a=='beingjing'):
            wrint(a)
            print('mainji 1000ping')
            print('renkou 200w')
'''
'''
dic={'name':'www','age':22,'pho':120,'好吃点':'你就多吃点'}
a=dic.keys()
print(dic.keys())
print(a)
b=dic.values()
print(dic.values())
print(b)
c=dic.items()
print(dic.items())
for i in dic.items():
    for a in i:
        print(a)
#print(dic.get('name'))
'''
#for i in c:
#    print(i)
'''
lis=[{'上海':{'面积':'100平','人口':'200w'},'北京':{'面积':'200平','人口':'150w'},'成都':{'面积':'50平','人口':'130w'}}]

for i in lis:
    for a,b in i.items():
        for c,d in b.items():
                print(a,c,d)

'''

'''
str='人生苦短，我用pyrYthon，life is short'
print(len(str))
print(str.count('p'))
print(str.count('l'))
a=str.rfind('s',0,len(str))
print(a)
'''
'''
print(str.upper())#转换 string 中的小写字母为大写
print(str.title())#把字符串的每个单词首字母大写
str1=str[:]#把字符串的每个单词首字母大写
print(str1)

names=['二豆','华仔','狗仔','三毛']
for i in names:
    print('hello friend %s' %i)


bus=['保时捷','劳斯莱斯','宾利','林肯']
for a in bus:

    print('i like %s ' % a)
'''

lis=['xiaom','xiaohua','xiaoming']
print(lis)
Z=input('shuru wufacanjia renyuan')
J=input('shuru xinlaideren ')
for i in lis:

    if i == Z:
        print('%s wufacanjia' %i)
        lis.remove(Z)
        lis.append(J)
        print(lis)
for b in lis:
    print('hello %s'%b)
    #print(lis.append('xiaog'))
print(lis)
x=input('1')
y=input('2')
z=input('3')
lis.insert(0,x)
print(lis)
lis.insert(2,y)
print(lis)
lis.append(z)
print(lis)
for n in lis:
    print(n)
i=0
while(i<=len(lis)):
    lis.pop()
    print(lis)
    i+=1
    if(i<=len(lis)):
        print('baoqian')
    else:
        print('haunyin')

print(lis)
del lis[0]
del lis[0]
print(lis)


'''
a=[1,3,5]
print(a)
print(a.reverse())
a.sort()
'''


