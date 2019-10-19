import matplotlib.pyplot as plt
import numpy as np

n = 1024    # data size
X = np.random.normal(0, 1, n) # 每一个点的X值
Y = np.random.normal(0, 1, n) # 每一个点的Y值
T = np.arctan2(Y,X) # for color value


# 输入X和Y作为location，size=75，颜色为T，color map用默认值，透明度alpha 为 50%。 
# x轴显示范围定位(-1.5，1.5)，并用xtick()函数来隐藏x坐标轴，y轴同理：

plt.scatter(X, Y, s=55, c=T, alpha=.5)

plt.xlim(-1.5,1.5)
plt.xticks(())  # ignore xticks
plt.ylim(-1.5,1.5)
plt.yticks(())  # ignore yticks

plt.show()