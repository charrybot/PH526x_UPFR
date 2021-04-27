"""
Plotting Using Logarithmic Axes
-semilogx() plots the x-axes on a log scale and the y in the original scale;
-semilogy() plots the y-axes on the log scale and the x in the original scale;
-loglog() plots both x and y on logarithmic scales.
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.logspace(np.log10(0.1), np.log10(10), 20)
y1 = x**2
y2 = x**1.5

plt.loglog(x, y1, "bo-", linewidth=1, markersize=2, label="first")
plt.loglog(x, y2, "ro-", linewidth=2, markersize=4, label="second")
plt.xlabel("$X$")
plt.ylabel("$Y$")
# plt.axis([xmin, xmax, ymin, ymax])
plt.axis([-0.5, 10.5, -5, 105])

plt.legend(loc="upper left")
plt.show()


