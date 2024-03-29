# coding=UTF-8
#文本块处理程序
class Handler:
    """
    处理程序父类
    """
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method): return method(*args)

    def start(self, name):
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)

    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None: match.group(0)
            return result
        return substitution

class HTMLRenderer(Handler):
    """
    HTML处理程序,给文本块加相应的HTML标记
    """
    def start_document(self):
        print('<html><head><title>Python文本解析</title></head><body>')
        print('<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>')
    def end_document(self):
        print('</body></html>')

    def start_paragraph(self):
        print('<p style=\"color: #444; text-indent:2em;\" >')

    def end_paragraph(self):
        print('</p>')

    def start_heading(self):
        print('<h2 style=\"color: #68BE5D;\" align=\"right\">')

    def end_heading(self):
        print('</h2>')

    def start_list(self):
        print('<ul style=\"color: #363736;\">')

    def end_list(self):
        print('</ul>')

    def start_listitem(self):
        print('<li>')

    def end_listitem(self):
        print('</li>')

    def start_title(self):
        print('<h1 style=\"color: #1ABC9C;\" align=\"center\">')

    def end_title(self):
        print('</h1>')

    def sub_emphasis(self, match):
        return '<em>{}</em>'.format(match.group(1))

    def sub_url(self, match):
        return '<a target=\"_blank\" style=\"text-decoration: none;color: #BC1A4B;\" href={}>{}</a>'.format(match.group(1),match.group(1))

    def sub_mail(self, match):
        return '<a style=\"text-decoration: none;color: #BC1A4B;\" href=\"mailto:{}\">{}</a>'.format(match.group(1), match.group(1))

    def feed(self, data):
        print(data)