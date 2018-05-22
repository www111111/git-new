name_list=[]
while True:
    a=input('shuru')

#name_list=[a]
    name_list.append(a)
    if (a=='q'):
        break
print(name_list)
print('1 %s' % name_list[1])
print('3 %s' % name_list[3])
print('5 %s' % name_list[5])
print('8 %s' % name_list[8])

name_list.sort()
print(name_list)
name_list.sort(reverse=True)
print(name_list)
name_list.pop()
print(name_list)
del name_list[8]
print(name_list)
print('xxxxxxxxxxxxxxxxxxxxx')
a=[1,'小明','a','dd',2]
name_list.extend(a)
print(name_list)
name_list=name_list.index('cc')
print(name_list)
#print( 'aa %s' % name_list.index('cc'))
