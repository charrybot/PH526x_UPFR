"""
Learn how to generate histograms using plt.hist()
Learn how to create subplots using plt.subplot()
"""
import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(size=1000)
#plt.hist(x, bins=np.linspace(-5, 5, 21))


x = np.random.gamma(2, 3, 100000)
plt.figure()
plt.subplot(2, 2, 1)
plt.hist(x, bins=30, cumulative=True)
plt.subplot(2, 2, 2)
plt.hist(x, bins=30, cumulative=True)
plt.subplot(2, 2, 3)
plt.hist(x, bins=30, cumulative=True, histtype="step")
plt.show()

