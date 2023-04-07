import matplotlib.pyplot as plt
import numpy as np
import math as m
#np.arange() tạo 3d list, tác dụng giống range nhưng mà khác type
#delta và đỉnh phương trình (parabol)
def dt():
    return b*b - 4*a*c
def dinh_x():
    return -b/2*a #hoàn độ đỉnh
def dinh_y():
    return a*dinh_x()**2 + b*dinh_x() + c

#vẽ trục tung và trục hoành
def axis_x():
    xline_x = np.arange(dinh_x() -10,dinh_x() + 10, 0.1)
    xline_y = np.zeros_like(xline_x)
    plt.plot(xline_x, xline_y, color = 'k')
def axis_y(): 
    if a > 0:
        yline_y = np.arange(dinh_y() - 4, a*10**2 + b*10 + c, 0.1)
    else:
        yline_y = np.arange(a*10**2 + b*10 + c, dinh_y() + 4, 0.1)
    yline_x = np.zeros_like(yline_y)
    plt.plot(yline_x, yline_y, color = 'k')

#title function (unfinished)
def title():
    if a != 0 and b != 0 and c != 0:
        title = 'y = {}x^2 + {}x + {}'.format(a, b, c)
        return title
    if a != 0 and b != 0 and c == 0:
        title = 'y = {}x^2 + {}x'.format(a, b)
        return title
    elif a != 0 and b == 0 and c == 0:
        title = 'y = {}x^2 '.format(a)
        return title
    elif a == 0 and b == 0 and c == 0:
        title = "y = 0"
        return title

#parabol 
def parabol():
    x = np.arange(dinh_x()-10 , dinh_y()+10 , 0.1) 
    y = a*(x**2) + (b*x) + c
    return x, y

# giao diện
#plt.axes().set_facecolor('xkcd:mint green')

""" plotting """
#nhap a,b,c ax^2 + bx +c
a = int(input("Nhập a:"))
b = int(input("Nhập b:"))
c = int(input("Nhập c:"))
#title
print(title())
plt.title(title())
bottom, top = plt.ylim()
print(bottom,top)

plt.ylim(dinh_y() - 4, dinh_y() + 7) 
#calculate value for x and y

plt.plot(parabol()[0], parabol()[1], color = 'r')
#hàm vẽ trục tung và trục hoành
axis_x()
axis_y()

# Display the plot
plt.show()

#chức năng còn thiếu: zoom, scroll, user-friendly, title improvement
