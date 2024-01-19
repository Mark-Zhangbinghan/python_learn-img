# Python

[TOC]



## 1/17学习

### 一、 基本语句：（缩进以四个空格为准）

##### 1. 输入输出

```python
# 在python中，用input( )使用户输入一个字符串，并放到一个变量中
string = input('Please input your string ')     # 在input里的字符串会随着语句一起输出

# 在python中，用print( )进行输出
print(string, end=' ')                          # 若在print内加入end=，此次输出后将不会换行
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

#可利用zip()对多个序列并行迭代
for (name,age,job) in zip(names,ages,jobs):
    print("{0}-{1}-{2}".format(name,age,job))
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





### 三、 数据结构

##### 1. 字符串

​    通常用单引号`'   '`、双引号`"   "`、三引号`'''   '''`来定义------>==必要条件==

> 格式化输出如下：

![](https://cdn.jsdelivr.net/gh/Mark-Zhangbinghan/python_learn-img@main/typora%E5%9B%BE%E5%BA%8A/202401192137451.png)



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

# 使用list()函数可将表达式转化为列表
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





## 1/18学习

### 四、 推导式

######     1）列表推导式：

```python
a = [x*2 for x in range(1,5) if x%2==0]   #将符合条件的元素生成入列表a中
# a = [2, 4, 6, 8]
```

######     2）字典推导式：

```python
my_text = 'i love you,i love mark,i love zidain'
text_count = {c:my_text.count(c) for c in my_text}
# 将my_text中的每一个字符统计数量并构成一个字典
```

###### 	3）集合推导式：（与列表推导式类似）

```python
a = {x*2 for x in range(1,5) if x%2==0}   #将符合条件的元素生成入列表a中
# a = {6, 8, 2, 4}                        #集合是无序的
```

###### 	4）生成器推导式：(不直接生成元组)

```python
a = (x for x in range(1,10) if x%2==0)
# <generator object <genexpr> at 0x000001EB9EC0D700>  --->生成器的表达式
for x in a:
    print(x， end=' ')
```





### 五、 错误和异常捕获

##### 	try/except：

```python
while True:
    try:
        user_weight = float(input("请输入您的体重(单位：kg):"))
    except ValueError:
        print("输入为不合理数字，请重新输入")
        continue
    else:
        print("您的体重为%.2fkg" % user_weight)
        exit()
```





### 六、 基本函数的使用

|         函数名         |                        用法                         |
| :--------------------: | :-------------------------------------------------: |
|   map(函数名，列表)    |  将列表中的所有元素代入到函数中加工，并返回生成器   |
| lambda 参数:操作(参数) | 匿名函数(lambda它只是一个表达式，而def则是一个语句) |
|  filter(函数名，参数)  | 过滤函数，与map作用类似，函数名的函数返回值要是T/F  |





### 七、 面向对象（从宏观上把握，从整体上分析）

##### 1. 类与实例化（用class定义类，类似与结构体）

```python
class Cat:  # 这是一只猫
    name = "Amy"
    age = "age"

    """
    在__init__方法内部使用self.属性名 = 属性的初始值就可以定义属性
    在定义属性之后，再使用Cat类创建对象，都会拥有该属性。
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    """
    如果在开发中使用print输出变量时，希望打印自定义内容
    就可以利用 __str__这个内置方法
    """
    def __str__(self):
        return "我是小猫[%s]" % self.name

    def eat(self):
        print("%s岁的%s爱吃饭" % (self.age, self.name))

    def sleep(self):
        print("%s爱睡觉" % self.name)

tom = Cat("Tom", "2")                        # 实例--->类属性与实例属性相同时，实例属性优先
tom.name = "Tom"                             # 赋予实例属性--->理解为字典
tom.eat()
tom.sleep()
print(tom)                                   #输出函数__str__内的内容
print(Cat.name)
print(Cat.age)


输出结果：
>>>2岁的Tom爱吃饭
>>>Tom爱睡觉
>>>我是小猫[Tom]
>>>Amy
>>>age
```

##### 2. 私有属性和私有方法

​	在实际开发中，对象的某些属性或方法可能只希望在对象的内部被使用，而不希望在外部访问到

1. ###### **私有属性**就是对象不希望公开属性

2. ###### **私有方法**就是对象不希望公开方法

> **定义方法**： 在定义属性或方法时，在属性名或方法名前增加两个下划线，定义就是私有属性或方法

##### 3. 面向对象的三大特性（封装、继承、多态）

- **封装：**根据职责将属性和方法封装到一个抽象的类中（私有化）

- **继承：**实现代码的重用 相同的代码不需要重复的编写

###### 1）继承的概念：子类拥有父类的全部方法和属性

###### 2）继承的语法：

```python
class 类名(父类名)：
	pass
```

1. 子类继承父类，可以**直接享受**父类封装好的方法，不需要再次开发
2. 子类中应该根据职责，封装子类**特有的**属性和方法
3. 子类对象不能在自己的方法内部直接访问父类的**私有属性或方法**

- **多态：**不同的对象调用相同的方法，产生不同的执行结果，增加代码的灵活度

1. 多态可以**增加**代码的**灵活度**
2. 以**继承**和**重写**父类方法为前提
3. 是调用方法的技巧，**不会影响**到类的内部设计









