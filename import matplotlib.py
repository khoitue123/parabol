import matplotlib.pyplot as plt
import numpy as np
import math as m

#delta và đỉnh phương trình (parabol)
def dt():
    return b*b - 4*a*c
def dinh_x():
    return -b/2*a #hoàn độ đỉnh
def dinh_y():
    return a*dinh_x()**2 + b*dinh_x() + c

#vẽ trục tung và trục hoành
def truc_hoanh():
    xline_x = np.arange(dinh_x() -10,dinh_x() + 10, 0.1)
    xline_y = np.zeros_like(xline_x)
    plt.plot(xline_x, xline_y, color = 'k')
def truc_tung(): 
    if a > 0:
        yline_y = np.arange(dinh_y() - 4, a*10**2 + b*10 + c, 0.1)
    else:
        yline_y = np.arange(a*10**2 + b*10 + c, dinh_y() + 4, 0.1)
    yline_x = np.zeros_like(yline_y)
    plt.plot(yline_x, yline_y, color = 'k')


#vẽ parabol (hàm chính dùng để vẽ đồ thị)
def parabol():
    x = np.arange(dinh_x()-10 , dinh_x()+10 , 0.01) 
    y = a*(x**2) + (b*x) + c
    return x, y

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

# giao diện (background color)
#plt.axes().set_facecolor('xkcd:mint green')

""" plotting """
#nhap a,b,c ax^2 + bx +c
a = int(input("Nhập a:"))
b = int(input("Nhập b:"))
c = int(input("Nhập c:"))

#title
print(title())
plt.title(title())
#trademark =))
plt.text(dinh_x()+2, dinh_y() - 5.5, "made by anh khôi, xuân đức", color = "g")

#giới hạn cho cái khung
plt.ylim(dinh_y() - 4, dinh_y() + 10) 
plt.ylim(dinh_x() - 6, dinh_x()+6)
#vẽ hàm chính
plt.plot(parabol()[0], parabol()[1], color = 'r')
#hàm vẽ trục tung và trục hoành
truc_hoanh()
truc_tung()

# Display the plot
plt.grid() #hiện thị khung grid 
plt.show()

