
import numpy as np
import matplotlib.pyplot as plt
import math
 

def draw(func,a,b):
    plt.rcParams['font.family'] = 'SimHei'
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(2)
    ax = plt.subplot(111)
    x = np.linspace(a, b, 100000)  # 在0到2pi之间，均匀产生200点的数组
    y,name = func(x)
    ax.plot(x,y)
    ax.set_title(name)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.ylim(ymin=-1000,ymax=1000000)
    plt.show()

def drawAndCompare(f1,f2,a,b):
    plt.rcParams['font.family'] = 'SimHei'
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(2)
    ax = plt.subplot(111)
    x = np.linspace(a, b, 100000)  # 在0到2pi之间，均匀产生200点的数组
    y1,name1 = f1(x)
    y2,name2 = f2(x)
    ax.plot(x,y1)
    ax.plot(x,y2)
    ax.set_title(" 蓝色："+name1+" 橘色："+name2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.ylim(ymin=-10000,ymax=1000000)
    plt.show()

def drawAndCompare2(f1,f2,f3,a,b):
    plt.rcParams['font.family'] = 'SimHei'
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(2)
    ax = plt.subplot(111)
    x = np.linspace(a, b, 10000000000000)  # 在0到2pi之间，均匀产生200点的数组
    y1,name1 = f1(x)
    y2,name2 = f2(x)
    y3,name3 = f3(x)
    ax.plot(x,y1)
    ax.plot(x,y2)
    ax.plot(x,y3)
    ax.set_title(" 蓝色："+name1+" 橘色："+name2+" 绿色："+name3)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.ylim(ymin=-0.5,ymax=5)
    plt.show()

# x的三次方-3x
def func1(x):
    y = np.power(x, 3) - 3 * x
    name = "np.power(x, 3) - 3 * x"
    return y,name

# x的三次方-3x
def func2(x):
    y = np.sin(x)
    name = "np.sin(x)"
    return y,name

# x-(3/2)*np.power(x,2/3)
def func3(x):
    #这里需要注意直接使用2/3次方的话，power函数无法正确处理。
    y = x-(3/2)*newPow(np.power(x,2),3)
    name = "x-(3/2)*np.power(x,2/3)"
    return y,name

# 2*np.power(x,1/2)
def func4(x):
    y = 2*np.power(x,1/2)
    name = "2*np.power(x,1/2)"
    return y,name

# 3-1/x
def func5(x):
    #这里需要注意直接使用2/3次方的话，power函数无法正确处理。
    y = 3-(1/x)
    name = "3-1/x"
    return y,name

# lnx
def func6(x):
    #这里需要注意直接使用2/3次方的话，power函数无法正确处理。
    y = np.log(x)
    name = "lnx"
    return y,name

# 1/x*sin(1/x)
def func8(x):
    y =1/x*np.sin(1/x)
    name = "1/x*sin(1/x)"
    return y,name

# 1/x 
def func9(x):
    y =1/x
    name = "1/x"
    return y,name
# power(x,-1/2)
def func10(x):
    y =np.power(x,-1/2)
    name = "power(x,-1/2)"
    return y,name

# 1/(x*x)
def func12(x):
    y =1/np.power(x,2)
    name = "1/np.power(x,2)"
    return y,name
# 1/(x*x)
def func13(x):
    y =1/np.power(x,1/2)
    name = "1/np.power(x,1/2)"
    return y,name

# 1/(x*(x-1)*(x+1)*(x-2))
def func11(x):
    y =1/(x*(x-1)*(x+1)*(x-2))
    name = "1/(x*(x-1)*(x+1)*(x-2))"
    return y,name

# np.power(x,5)+4*np.power(x,4) +1
def func14(x):
    y =0.8*np.power(x,5)+4*np.power(x,4) +1
    name = "np.power(x,5)+4*np.power(x,4) +1"
    return y,name

# np.power(x,5)
def func15(x):
    y =np.power(x,5)
    name = "np.power(x,5)"
    return y,name

# np.power(x,10)/np.exp(x)
def func16(x):
    y =np.power(x,10)/np.exp(x)
    name = "np.power(x,10)/np.exp(x)"
    return y,name

# y = np.power(x,1/3)
def newPow(x,n):
    y = []
    for i in list(x):
        if i < 0:
            y.append(-pow(-i,1/n))
        else:
            y.append(pow(i,1/n))
    y1 = np.array(y)
    return y1

# draw(func6,-2,3)
# draw(func2,-2,2)
# draw(func3,-2,2)
# drawAndCompare(func14,func15,-2,20000)

draw(func16,-10,150)