#字符串是不可变得

width = int(input('请输入宽度：'))

price_width = 10
item_width = width - price_width
header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)

fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)

print('=' * width)
print(header_fmt.format('Item', 'Price'))

print('-' * width)

print(fmt.format('Apple', 0.4))
print(fmt.format('Pears', 0.5))
print(fmt.format('Cantaloupes', 1.92))
print(fmt.format('Apple', 0.4))
print(fmt.format('Apple', 0.4))

print('=' * width)