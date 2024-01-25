# Numpy函数学习

[TOC]

>  基于列表构建矩阵 特殊矩阵构建 矩阵乘法 矩阵广播机制 矩阵转置 矩阵的逆 矩阵存取

#### **相对于Python直接实现，优点：**

#### 	一、代码更简洁：粒度计算，并支持大量的数学函数

#### 	二、性能更高效：Numpy的数据存储与Python原生的List不同

##### 1. np.arange()创建数字序列

```python
def numpy_sum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    return a+b

numpy_sum(10)
>>>array([0,2,12,36,80,150,252,392,576,810])

np.shape()  # 用来确认矩阵的行列数
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
A = np.reshape(A, (2, 5))
A.shape = (2,5)
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
array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
array2 = np.array([[9,8,7],[6,5,4],[3,2,1]])
result = np.matmul(array1,array2)
```

###### 	3）np.dot()数组点积

```python
import numpy as np 
array1=np.array([[1,2,3],[4,5,6],[7,8,9]],ndmin=3) 
array2=np.array([[9,8,7],[6,5,4],[3,2,1]],ndmin=3) 
result=np.dot(array1,array2) 
```

##### 6. Numpy数组的广播机制

```python
# 当两个数组的shape相同时，两数组相乘的结果就是两数组对应位相乘
import numpy as np
a = np.array([1,3,5,7])
b = np.array([2,4,6,8])
c = a*b = [2,12,30,56]
```

> numpy广播的规则：

1、如果两个数的维度数不同，那么小维度数组的形状将会在最左边补1。
2、如果两个数组的形状在任何一个维度都不匹配，那么数组的形状会沿着维度为1的维度扩展以匹配另外一个数组的形状。
3、如果两个数组的形状在任何一个维度上都不匹配并且没有任何一个维度等于1，那么会引发异常。

```python
a = np.array([[1],
              [2],
              [3]])
b = np.array([1,2,3])
c = a+b = [[2,3,4]
           [3,4,5]
           [5,6,7]]
```

##### 7. 矩阵的转置

```python
import numpy as np
a = np.arange(10)
a = np.reshape(a, (2, 5))
a = a.T  # 通过用.T实现矩阵的转置
```

##### 8. 矩阵的逆

```python
import numpy as np
a = [[1, 2, 3, 4],
     [3, 4, 5, 6],
     [5, 6, 7, 8],
     [7, 8, 9, 0]]
print(np.linalg.inv(a))  # 通过用np.linalg.inv()实现矩阵求逆
```

##### 9. 矩阵的存取

> 通过savetxt存储矩阵，通过loadtxt读取矩阵：

|  函数   |               说明                |
| :-----: | :-------------------------------: |
| savetxt |    将np.ndarray存储在txt文件中    |
| loadtxt | txt文件中的矩阵读取到np.ndarray中 |

```python
import numpy as np
# np.savetxt(frame,array,fmt='%.18e',delimiter=None)
np.savetxt(X = array1, frame = "test.txt")
# np.loadtxt(frame,dtype=np.float,delimiter=None,unpack=False)
array2 = np.loadtxt("test.txt")
```

> 模型的保存和导入

```python
import numpy as np
#保存整个神经网络的结构和模型参数
torch.save(mymodel,'mymodel.pkl')
#只保存神经网络的模型参数
torch.save(mymodel.stae_dict(),'mymodel_prams.pkl')

mymodel = torch.load('mymodel.pkl')
```

##### 10. np.histogram直方图生成函数

```python
numpy.histogram(a, bins=10, range=None, normed=None, weights=None, density=None)

			1）a:  输入图像， 必选
			输入数据。直方图是在展平的数组上计算的。
            
			2）bin: int 或标量序列或 str
			如果 bins 是一个 int，它定义给定范围内的 equal-width bins 的数量(默认为 10)，主要是将灰度值空间分为多少分进行灰度值统计
            
			3）range：(浮点数，浮点数)，可选
			bin 的下限和上限范围，如果没有提供，范围很简单(a.min(), a.max()).超出范围的值将被忽略。范围的第一个元素必须小于或等于第二个元素。主要表明的是需要统计的灰度值取值范围。
                
			4）normed：布尔型，可选
			5）weights： 数组，可选
			6）density： 布尔型，可选
			如果False，结果将包含每个 bin 中的样本数。如果True, 结果就是概率的值密度在 bin 处的函数，归一化使得不可缺少的在范围内为 1
```



