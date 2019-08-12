#一个简单的字典

#一个将人名作为键的字典，每个人都用一个字典表示
#字典包含phone和addr,他们分别与电话号码和地址相关联

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

if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

#仅当名字是字典里的，打印
if name in people:print("{}'s {} is {}.".format(name, lables[key], people[name][key]))


