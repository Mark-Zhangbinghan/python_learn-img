import numpy as np


# 构建线性回归函数的类封装
class Linear:
    def __init__(self, alpha, times, lz):
        """初始化方法
        参数解释：
        alpha:学习率（权重调整的幅度）
        times:循环迭代的次数，达到一定次数终止迭代
        lz:正则化参数
        """
        self.alpha = alpha
        self.times = times
        self.lz = lz

    # 求解损失函数MSE
    def CostFunction(self, x, y, theta):
        inner = np.power((x@theta-y), 2)
        return np.sum(inner)/(2*len(x))

    # 梯度下降函数
    def Gradient(self, x, y):
        loss = []
        theta = np.zeros((2, 1))
        for i in range(self.times):
            theta = theta - self.alpha*(x.T@theta - y)/len(x)
            if i % 100 == 0:
                loss.append(theta)
        return theta, loss


alpha = 0.001
times = 10000
lz = 0
x_train = np.zeros((2, 2))
y_train = np.zeros((2, 2))
LINE = Linear(alpha, times, lz)
thetas, loss_ = LINE.Gradient(x_train, y_train)
MSE = LINE.CostFunction(x_train, y_train, thetas)
