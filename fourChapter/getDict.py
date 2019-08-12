#一个会用get的简单数据库

people = {
    'Alice': {
        'phone': 1234,
        'addr': 'Foo drive 23'
    },

    'Beth': {
        'phone': 1233,
        'addr': 'Bar drive 23'
    },
    'Cecli': {
        'phone': 1235,
        'addr': 'Bax drive 23'
    }
}
#电话号码和地址的描述性标签，供打印输出时使用

lables = {
    'phone': 'phone number',
    'addr': 'address'
}

name = input('Name:')

#查找电话还是地址
request = input('电话(p)或者地址(a)：')

#使用正确的键
key = request #如果request不是'p' 也不是'a'
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

#使用get 提供默认值
person = people.get(name, {})
lable = lables.get(key, key)
result = person.get(key, 'not available')
print("{}'s {} is {}.".format(name, lable, result))