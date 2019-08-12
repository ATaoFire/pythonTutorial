#除了索引，还可以使用切片来访问元素
tag = 'qwertyuiopasdfghjkl'
print(tag[9:17])
print(tag[9:-4])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:6])
print(numbers[0:1])
print(numbers[7:10])
print(numbers[-3:-1])
print(numbers[-3:])
print(numbers[0:3])
print(numbers[:])

# url = input('请输入URL:')
# domain = url[12:-4]
# print(domain)

#步长，设置更大步长
print(numbers[0:10:1])
print(numbers[0:10:2])
print(numbers[10:0:-2])
print(numbers[::-2])
print(numbers[1:10:2])
