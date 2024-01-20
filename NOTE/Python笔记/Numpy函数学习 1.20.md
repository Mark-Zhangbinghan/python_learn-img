# Numpy函数学习

[TOC]



>  基于列表构建矩阵 特殊矩阵构建 矩阵乘法 矩阵广播机制 矩阵转置 矩阵的逆 矩阵存取

#### **相对于Python直接实现，优点：**

- 代码更简洁：粒度计算，并支持大量的数学函数
- 性能更高效：Numpy的数据存储与Python原生的List不同

##### 1. np.arange()创建数字序列

```python
def numpy_sum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    return a+b

numpy_sum(10)
>>>array([0,2,12,36,80,150,252,392,576,810])
```

##### 2. np.zeros()创建全是0的数组

```python
np.zeros(10)
np.zeros((2,3))

"""
若用np.full(shape,fill)
即可创建一个全是fill的数组
"""
```

##### 3. np.arange(shape).reshape(shape)构建多维数组

```python
A = np.arange(20).reshape(2, 5)
```

##### 4. 布尔索引

```python
x = np.arange(10)

x[x>5]
# 或者
condition = x>5
x[condition]
```

##### 5. 矩阵乘法

###### 	1）np.multiply()逐元素矩阵乘法

```python
import numpy as np 
array1=np.array([[1,2,3],[4,5,6],[7,8,9]],ndmin=3) 
array2=np.array([[9,8,7],[6,5,4],[3,2,1]],ndmin=3) 
result=np.multiply(array1,array2) 
```

###### 	2）np.matmul()矩阵乘积

```python
inport numpy as np
array1 = np.array[[1,2,3],[4,5,6],[7,8,9]]
array2 = np.array[[9,8,7],[6,5,4],[3,2,1]]
result = np.matmul(array1,array2)
```



###### 	3）np.dot()数组点积

```python
import numpy as np 
array1=np.array([[1,2,3],[4,5,6],[7,8,9]],ndmin=3) 
array2=np.array([[9,8,7],[6,5,4],[3,2,1]],ndmin=3) 
result=np.dot(array1,array2) 
```

