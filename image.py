import matplotlib.pyplot as plt
import numpy as np
import random

a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)
inter=random.choice([None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
           'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
           'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos'])
print(inter)
plt.imshow(a, interpolation=inter, cmap='bone', origin='lower')

# 下面我们添加一个colorbar ，其中我们添加一个shrink参数，使colorbar的长度变短为原来的92%：
plt.colorbar(shrink=.92)
plt.xlabel(str(inter)+'-way to show')
plt.xticks(())
plt.yticks(())
plt.show()