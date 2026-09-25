import numpy as np
import matplotlib.pyplot as plt

kt = np.linspace(0, 10, 1000)
P = (1/(1+np.exp(-kt)))**4
E = np.cumsum(P)*(kt[1]-kt[0])
plt.plot(kt,E)
plt.show()