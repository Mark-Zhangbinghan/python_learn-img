# pandas库学习

> Pandas是基于Numpy的专业数据分析工具, 可以灵活高效的处理各种数据集

#### 一、 读取数据(**相对路径！！！**)

| 数据类型      | 说明                            | Pandas读取方式 |
| ------------- | ------------------------------- | -------------- |
| csv、tsv、txt | 用逗号分隔、tab分割的纯文本文件 | pd.read_csv    |
| excel         | 微软xls或者xlsx文件             | pd.read_excel  |
| myspl         | 关系型数据库表                  | pd.read_sql    |

```python
# 使用pd.read_csv()读取数据
datas = pd.read_csv("stu.txt")

# 查看前几行数据
datas.head()
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 不换行显示
pd.set_option('display.width', 1000)

# 查看数据的形状，返回（行数、列数）
datas.shape()
```

#### 二、 数据清洗

- 删除无用列

``` python
# 运用describe()函数展现统计信息
datas.describe()

# 运用drop()函数删除对应列
datas.drop(columns="XXX", inplace = True)

# 运用info()函数查看数据类型
datas.info()

# 运用isnull().sum()统计空值
datas.isnull().sum()

# 运用astype()函数将数据类型进行转换
datas['对应列'] = datas['对应列'].astype('想要的数据类型')
```

- 删除重复行

```python
# 运用duplicated()函数删除重复行
datas[datas.duplicated(keep=Fause)]  # 检查数据中是否存在重复值
datas[datas.drop_duplicated(keep="想要保留的行,如first",inplace=True)]
datas.reset_index(drop = True)  # 对数据索引进行重新排列
```

- 数据映射

```python
datas["XXX"].unique()  # 查看某一列的不同的数据种类
datas["XXX"] = datas["XXX"].map({
    "male":"male",
    "m":"male",
    "f":"female",
    "female":"female"
})
```

- 缺失值处理

```python
# 将特殊空值替换成NAN
datas["XXX"] = datas["XXX"].replace('-', np.NaN)

# 运用fillna()函数补充空值
datas["XXX"].fillna(datas["XXX"].median(),inplace = True)
```

- 字符串拆分

```python
# 取XXX数据的前10位
datas["XXX"] = datas["XXX"].apply(lambda x:str(x)[0:10])
```

#### 三、 数据提取

```python
# 统计XXX中的数据
datas["XXX"].value_counts()
```

##### 1. 分组聚合

```python
# 方法一
datas.pivot_table(index="索引值",values="想要比较的数据",aggfunc="数据比较的函数类型")

# 方法二
datas.groupby('索引值')['想要比较的数据'].count()
```

##### 2. 数据合并

```python
x = pd.merge(x,y,left_on=['以x的哪一列为合并值'],right_on=['以y的哪一列为合并值'])
```

