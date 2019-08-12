print(list('Hello'))



co = [1, 1, 1]
co[1] = 2
print(co)
#删除元素
names = ['A', 'B', 'C', 'D', 'E']
del names[2]
print(names)
#给切片赋值
name = list('Perl')
name[2:] = list('aa')
print(name)
#插入
name[1:1] = list('Python')
print(name)
#列表方法 append  clear copy

#append
lst = [1, 2, 3]
lst.append(4)
print(lst)

#clear
lst.clear()
print(lst)
#copy
a = [1, 2, 3]
b = a
print(b)
print(a)
#copy副本
b = a.copy()
b[1] = 4
print(b)
print(a)
#count
counta = ['to', 'br', 'to']
print(counta.count('to'))

#extend 切片也可以达到同样效果
sa = [1, 2, 3]
sb = [4, 5, 6]
sa.extend(sb)
print(sa)

#index
print(sa.index(4))

#insert
sa.insert(2, 10)
print(sa)
#pop
sa.pop()
print(sa)
#remove
sa.remove(10)
print(sa)
#reverse
sa.reverse()
print(sa)
