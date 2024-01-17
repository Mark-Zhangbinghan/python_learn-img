# Python

[TOC]



## 1/17学习

### 一、 基本语句：（缩进以四个空格为准）

##### 1. 输入输出

```python
# 在python中，用input( )使用户输入一个字符串，并放到一个变量中
string = input('Please input your string ')     # 在input里的字符串会随着语句一起输出

# 在python中，用print( )进行输出
print(string)
```



##### 2. 条件判断

```python
if 判断条件1：
    执行语句1...
elif 判断条件2：
    执行语句2...
else:
    执行语句3...
```



##### 3.  循环语句

######     	1）for循环

```python
string = 'Python'
for s in string:
    print(s)
    
"""
输出结果为
P
y
t
h
o
n
"""
```

######     	2）while循环

```python
sum = 0
m = 10
while m > 0:
    sum = sum + m
    m = m - 1
print(sum)

# 输出结果为55
```

######     	3）break退出循环

```python
string = 'Python'
for s in string:
    if s == 'o':
        break        # break用于for循环和while循环语句中，用于退出循环
    print(s)
    
"""
输出结果为
P
y
t
h
"""
```

######     	4）continue继续循环

```python
string = 'Python'
for s in string:
    if s == 'o':
        continue     # continue用于for循环和while循环语句中，用于跳过此次循环
    print(s)
    
"""
输出结果为
P
y
t
h
n
"""
```



##### 4. pass语句

```python
if Ture:
    pass            # pass作为空语句，用于补充语句结构完整性
```





### 二、 数字类型

##### 1. 数值类型

> 共有四种数值类型，分别是： 整形( int )、浮点型( float )、布尔类型( bool )、复数型( complex )

- **整形**：整型有四种进制表示，分别为：二进制、八进制、十进制、十六进制

  |   种类   |                     描述                     |  引导符  |
  | :------: | :------------------------------------------: | :------: |
  |  二进制  |                  由0和1组成                  | 0b 或 0B |
  |  八进制  |                  由0到7构成                  | 0o 或 0O |
  |  十进制  |                   默认情况                   |    无    |
  | 十六进制 | 由 0 到 9、a 到 f、A 到 F 组成，不区分大小写 |  0x或0X  |

- **浮点型**：由整数部分和小数部分组成
- **复数**：由实数部分和虚数部分组成
- **布尔类型**：由 True 和 Fault 组成



##### 2. 基本运算(import math)    

 仅列出与C语言中不同部分：

|        运算        |                    描述                    |
| :----------------: | :----------------------------------------: |
|       x / y        |               x 除以 y，取商               |
|       x // y       |              x 除以 y，取整除              |
|       x % y        |               x 除以 y，取模               |
|    complex(x,y)    | 一个带有实部 x 和虚部 y 的复数，y 默认为 0 |
| x ** y 或 pow(x,y) |                x 的 y 次幂                 |

![1705500688749](C:\Users\24468\Desktop\python\python_learn-img\Python笔记\1705500688749.png)



### 三、 数据结构

##### 1. 字符串

​    通常用单引号`'   '`、双引号`"   "`、三引号`'''   '''`来定义------>==必要条件==

> 格式化输出如下：





##### 2. 切片（左闭右开区间）

​    切片操作可以访问一定范围内的元素，语法如下所示：

```python
sname[start:end:step]
```

- sname：表示该序列的名字

- start：开始索引位置（包括该位置），默认为0

- end：结束索引位置（不包括该位置），默认为序列

- step：步长

  

##### 3. 字典`{x:y}`（字典的优势是快速存取,注意命名键的时候要见名知意,并且易于记忆）

######     	1）字典的定义：

```python
# 方法一
dict1 = {'name':'小明','age':'18'}

# 方法二
dict2 = dict(name='小明', age='18')
```

######     	2）字典的增加或更新：

- **增加**：字典变量[key] = 值  如果为新增,则key在原字典中不存在

```python
dict1['gender'] = '男'
print(dict1)  # {'name': '小明', 'age': '18', 'gender': '男'}
```

- **更新**：如果原字典中存在该key 则为更新原key所对应的值

```python
dict1['name'] = '小王'
print(dict1)  # {'name': '小王', 'age': '18', 'gender': '男'}
```

- **update(   )**

```python
dict1.update({'id': '001', 'color': 'yellow', 'name': 'rose'})
```

######     	3）字典的删除：

- **del** 查找到字典的键所对应的值进行删除

```python
del dict1['age']
```

- **clear( )** 清空字典所在数据空间中的多有键-值对

```python
dict1.clear()
```

- **pop( )** 删除指定键所对应的键-值对，会将删除的键-值对所对应的值**进行返回**

```python
dict1 = {'name': 'xiaoming', 'age': 18, 'gender': '男'}
print(dict1.pop('name'))    # 小明
print(dict1)                # {'age': 18, 'gender': '男'}
```

######     	4) 字典的查询

- **get( )** 查询

```python
dict1 = {'name': '小明', 'age': 18, 'gender': '男', 'id': '001'}
print(dict1.get('name'))     # 小明
print(dict1.get('apple'))    # None
```

- **keys** 获取当前字典中所有的键

```python
dict1.keys()
```

- **values** 获取当前字典中所有的值

```python
dict1.values()
```



##### 4. 列表`[]`（类似于数组，但是不用考虑类型）

######     	1）列表的创建

​    列表中所有元素都放在一个中括号 `[]` 中，相邻元素之间用逗号 `,` 分隔，如下所示：

```python
l = [1024, 0.5, 'Python']
```
######     	2）列表的访问

```python
print(l[1])    # 输出第二个元素，0.5
print(l[-1])   # 输出最后一个元素，Python
```
######     	3）列表的增删改查

- **增加**：

```python
# 方法一：用连接的方式
l + ['Hello World!']

# 方法二：append(追加一个元素到列表中
l.append('Hello World!')

# 方法三：extend(追加多个元素到列表中
l.extend(['Hello', 'World!'])

# 方法四：insert(在指定位置插入元素
l.insert(1,'Hello World!')
```

- **删除**：

```python
# 方法一：pop(弹出指定位置的元素
a = l.pop(0) #弹出第1个元素，并可以将其赋值

# 方法二：remove(指定删除对象的名字
l.remove('Python')

# 方法三：del(直接删除整个列表
del l
```

- **赋值**

```python
# 方法一：直接通过索引赋值
l[0] = 2024

# 方法二：通过切片赋值
l[:2] = [2024,3.14]
```

- **查看**

```python
# 方法一：count(查看某元素出现的次数
l.count('Python')
```



##### 5. 元组`()`（与列表类似，但元组是不可变的）

###### 	1）元组的创建

​	元组中所有元素都放在一个小括号 `()` 中，相邻元素之间用逗号 `,` 分隔，如下所示：

```python
t = (1024, 0.5, 'Python')
```

###### 	2）元组的访问

​    元组的访问与列表类似    

###### 	3）元组的修改

​	元组中元素不能被修改，我们要用重新赋值的方式操作，如下所示：

```python
t = (1024, 0.5, 'Python')
t = (1024, 0.5, 'Python', 'Hello')
```

==**Ps. 利用tuple()可将列表转换为元组**==



##### 6. 集合`{}`

###### 	1）集合的创建（Ps.集合中重复的元素会自动过滤掉）

​	集合使用花括号 `{}` 或者 `set()` 函数创建，如果**创建空集合**只能使用 `set()` 函数，如下所示：

```python
# 方法一：直接使用{}创建
s = {'a', 'b', 'c'}

# 方法二：利用set()函数创建
s = set(['a', 'b', 'c'])
```

###### 	2）集合的修改（添加后元素顺序随机）

- 增加

```python
# 方法一：add(将一个元素添加到集合中
set1 = {1,2,3,4}
set1.add(5)

# 方法二：update(将多个元素添加到集合中-->可以是列表、元组、字典等
set1.update(['hello', 'python'])
```

- 删除

```python
# 方法一：remove
set1.remove('hello')    #若元素不存在则报错

# 方法二：discard
set1.discard('python')  #若元素不存在不报错

# 方法三：pop
set1.pop()              #可返回并删除随机一个值

# 方法四：clear
set1.clear()            #清空集合中所有元素
```

###### 	3）集合的比较

通过运算符进行集合间的比较













