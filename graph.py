import numpy
import matplotlib.pylab as graph

def fx(x): #함수
    return x**3 + 2*x**2 - 4*x - 2

def differential(f, x):  #미분 함수
    h = 0.0000000001 #0의 극한
    return (f(x+h) - f(x-h)) / (2*h) #중앙차분
    #return (f(x+h) - f(x)) / h  도함수

def line(f, x): 미분함수의 접선함수
    d = differential(f, x)
    y = f(x) - d*x
    return lambda t: d*t + y

xx = float(input('접선의 x좌표를 입력해주세요: '))
lim_x1, lim_x2 = map(float, input('x의 최솟값과 최대값을 입력해주세요(띄어쓰기로 구별): ').split())
lim_y1, lim_y2 = map(float, input('y의 최솟값과 최대값을 입력해주세요(띄어쓰기로 구별): ').split())


graph.axvline(x = 0, color = 'r')
graph.axhline(y = 0, color = 'r')

x = numpy.arange(lim_x1, lim_x2, 0.01)
y = fx(x)
graph.plot(x, y, 'b') #일반함수 그리기

y2 = differential(fx, x)
graph.plot(x, y2, 'g') #미분한 함수 그리기

tf = line(fx, xx)
y3 = tf(x)
graph.plot(x, y3, 'm') #미분함수 접선 그리기

graph.ylim(lim_y1, lim_y2)
graph.show() #그래프 보내기
