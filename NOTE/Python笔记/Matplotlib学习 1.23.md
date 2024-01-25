# Matplotlib学习

[TOC]

```python
# 引用
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 设置正常显示符号
```

#### 一、 显示图片

```python
# retstep:是否断开各点之间的连线
x = np.linspace(start, stop, num, retstep=False)
y1 = 2*x+1
y2 = x**2

# num：编号
# figsize：图像展示的大小
# dpi：像素值
plt.figure(num=1,figsize=(10,10),dpi=100)   # 组一
plt.plot(x, y1)

# color：颜色
# linewidth：线的宽度
# linestyle：线的种类
plt.figure(num=2)   # 组二
plt.plot(x, y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')

plt.show()
```

##### 1. 多图分布

```python
# 多图布局
plt.subplot()
plt.subplots()
# 图形嵌套
plt.add_subplot()
plt.axes()
```

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize=(8, 3))

x = np.linspace(-np.pi, np.pi, 30)
y = np.sin(x)

# 子图1
ax1 = plt.subplot(2, 2, 1)  # 一行两列中的第一个图
ax1.plot(x, y)
ax1.set_title('子图1')  # 对图片进行注释

# 子图2
ax2 = plt.subplot(2, 2, 2)  # 一行两列中的第二个图
ax2.plot(x, y)
ax2.set_title('子图2')

# 子图3
ax3 = plt.subplot(2, 1, 2)  # 两行一列中的第二个图
ax3.plot(x, np.sin(x*x))
ax3.set_title('子图3')

# 自动调整布局
fig.tight_layout()

plt.show()
```

![](https://cdn.jsdelivr.net/gh/Mark-Zhangbinghan/python_learn-img@main/typora%E5%9B%BE%E5%BA%8A/202401232110426.png)

##### 2. 双轴显示

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 设置正常显示符号

fig = plt.figure(figsize=(10, 8))

x = np.linspace(0, 10, 100)

# 图1
ax1 = plt.gca()
ax1.plot(x, np.exp(x), color='r')
ax1.set_title('图1')  # 对图片进行注释
ax1.set_xlabel('time')
ax1.set_ylabel('exp', color='r')
ax1.tick_params(axis='y', labelcolor='r', labelsize='10')

# 图2
ax2 = ax1.twinx()  # 与图1共享x轴
ax2.plot(x, np.sin(x), color='b', linestyle='--')
ax2.tick_params(axis='y', labelcolor='b', labelsize='10')

plt.tight_layout()
plt.show()
```

![](https://cdn.jsdelivr.net/gh/Mark-Zhangbinghan/python_learn-img@main/typora%E5%9B%BE%E5%BA%8A/202401232151539.png)

##### 3. 坐标轴的设置

```python
fig = plt.figure(figsize=(6, 4))

x = np.linspace(0,10)
y = np.sin(x)
plt.plot(x,y)

# fonsize:字体大小
plt.xticks(ticks=np.arange(0,11,1), fontsize=10)
plt.yticks(ticks=[-1,0,1],  # 刻度值，刻度大小
           labels=['min','0','max'])  # 显示的刻度标签

# 坐标轴的范围
plt.xlim(-5,5)
plt.axis([1,2,3,4])  # [xmin, xmax, ymin, ymax]
```

| 绘图类型 | 绘图函数  |
| -------- | --------- |
| 散点图   | scatter() |
| 饼图     | pie()     |
|          |           |

#### 二、 绘制散点图

```python
# np.random.rand() rand函数根据给定维度生成[0,1)之间的数据，包含0，不包含1
# np.random.randn() randn函数返回一个或一组样本，具有标准正态分布
# np.random.randint() 返回随机整数，范围区间为[low,high）

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 设置正常显示符号

fig = plt.figure(figsize=(10, 8))
data = np.random.randn(100, 2)
s = np.random.randint(50, 200, size=100)
c = np.random.randn(100)

# 利用scatter建立散点图
plt.scatter(data[:, 0], data[:, 1], s=s, c=c, alpha=0.6)
plt.show()
```

![](https://cdn.jsdelivr.net/gh/Mark-Zhangbinghan/python_learn-img@main/typora%E5%9B%BE%E5%BA%8A/202401240942409.png)

#### 三、 绘制饼图

```python
# 利用pie建立饼图
plt.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=0, radius=1, counterclock=True, wedgeprops=None, textprops=None, center=0, 0, frame=False, rotatelabels=False, *, normalize=None, data=None)[source]
```



