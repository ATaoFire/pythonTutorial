from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

d = Drawing(200, 200)
s = String(100, 100, 'Hello, world', textAnchor='middle')
d.add(s)
renderPDF.drawToFile(d, 'hello.pdf', 'A simple PDF file')



