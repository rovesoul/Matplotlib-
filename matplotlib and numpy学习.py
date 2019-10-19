import matplotlib.pyplot as plt
import numpy as np
x= np.linspace(-3,3,50)
y1= 2*x+1
y2= np.sin(x)
#------------------------------------------------------------------1
# plt.figure()
# # 用plt展示出来
# plt.plot(x,y1)
# plt.show()
#------------------------------------------------------------------2
# plt.figure(num='hahaha' , figsize=(8,5))
# # 用plt展示出来
# plt.plot(x,y2)
# plt.plot(x,y1,color='red',linewidth=1,linestyle='--')
# plt.show()
#------------------------------------------------------------------3
plt.figure(num='带坐标轴' , figsize=(5,5))
# 用plt展示出来
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=0.5,linestyle='--')
# 加横纵坐标轴范围
plt.xlim((-1,2))
plt.ylim((-2,3))
#加坐标轴解释
plt.xlabel('i am x')
plt.ylabel('i am y')

#换角标，原始x轴7个点，换成5个
new_ticks=np.linspace(-1,2,5)
# print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,1,3],['really bad','nomal','really good'])
plt.show()
#------------------------------------------------------------------
