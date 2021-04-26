import matplotlib.pyplot as plt
import numpy as np
#　plt.plot([0, 1, 4, 9, 16]);
#　plt.show()

x = np.linspace(0, 10, 20)
y1 = x**2
#　plt.plot(x, y1)
#　plt.show()

# linewidth, markersize
y2 = x**1.5
plt.plot(x, y1, "bo-", linewidth=1, markersize=2)
plt.plot(x, y2, "ro-", linewidth=2, markersize=4)
plt.show()

