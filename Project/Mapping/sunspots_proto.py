from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import  renderPDF

data = [
    #Year moth Predicted High   Low
    (2007, 8,   113.2,    114.2, 112.2),
    (2007, 9,   112.8,    115.8, 109.8),
    (2007, 10,  111.0,    116.0, 106.0),
    (2007, 11,  109.8,    116.8, 102.8),
    (2007, 12,  107.3,    115.3, 99.3),
    (2008, 1,   105.2,    114.2, 96.2),
    (2008, 2,   113.2,    114.2, 112.2),
    (2008, 3,   112.8,    115.8, 109.8),
    (2008, 4,   111.0,    116.0, 106.0),
    (2008, 5,   109.8,    116.8, 102.8),
    (2008, 6,   107.3,    115.3, 99.3),
    (2008, 7,   105.2,    114.2, 96.2),
]

drawing = Drawing(400, 400)
pred = [row[2]-40 for row in data]
high = [row[3]-40 for row in data]
low = [row[4]-40 for row in data]
times = [400*((row[0]+row[1]/12.0)-2007)-220 for row in data]

drawing.add(PolyLine(list(zip(times, pred)), strokeColor=colors.blue))
drawing.add(PolyLine(list(zip(times, high)), strokeColor=colors.red))
drawing.add(PolyLine(list(zip(times, low)), strokeColor=colors.green))

drawing.add(String(130, 230, 'Sunsports', fontSize=18, fillColor=colors.red))
renderPDF.drawToFile(drawing, 'report1.pdf', 'Sunsports')
