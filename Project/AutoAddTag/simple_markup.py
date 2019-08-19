# encoding: utf-8
import sys, re
from util import *

print('<html><head><title>文本自动添加标签</title><body>')
print("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">")

title = True

for block in  blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*', r'<em>\1<em>', block)
    if title:
        print('<h1>')
        print(block)
        print('</h>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')


print('</body></html>')

