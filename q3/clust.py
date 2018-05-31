from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

data = pd.read_csv('nafta.csv')
print(data.shape)
data.head()

f1 = data['Description'].values
f2 = data['Title'].values
X = np.array(list(zip(f1, f2)))
plt.scatter(f1, f2, c='black', s=7)

k=2
colors = ['r', 'g', 'b', 'y', 'c', 'm']
fig, ax = plt.subplots()
ax.scatter(C[:, 0], C[:, 1], marker='*', s=200, c='#050505')

plt.show()
