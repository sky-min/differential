import numpy
import matplotlib.pylab as graph

def fx(x): #함수
    return x**3 + 2*x**2 - 4*x - 2

def differential(f, x):  #미분 함수
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

x = numpy.arange(-5, 5, 0.01)
y = fx(x)
graph.plot(x, y, 'b') #일반함수 그리기

y2 = differential(fx, x)
graph.plot(x, y2, 'g')

graph.axvline(x = 0, color = 'r')
graph.axhline(y = 0, color = 'r')
graph.show() #그래프 보내기
