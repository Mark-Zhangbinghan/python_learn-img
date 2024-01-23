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

