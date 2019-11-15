import numpy as np
import matplotlib.pyplot as plt

alpha = 5.
g = alpha
L = 100
dx = 1
dy = dx
n = int(L/dx)
T = np.zeros((n, n))
x = np.linspace(0, 100, n)
y = np.linspace(0, 100, n)
w = 1 #Gauss Seidel

#2D Poisson
T[:, 0] = 75
T[:, n-1] = 30
T[0, :] = 237
T[20:30, 20:30] = 100

for i in range(10000):
    r = 1/4 * (T[2:n, 1:n-1] + T[0:n-2, 1:n-1] + T[1:n-1, 2:n] + T[1:n-1, 0:n-2] - (dx**2.)*g/alpha) - T[1:n-1, 1:n-1]
    T[1:n-1, 1:n-1] += (1-w) * T[1:n-1, 1:n-1] + w*r

plt.contourf(x, y, T, cmap = 'rainbow')
plt.colorbar()
plt.show()

#1D poisson
#f = [0] * n
#for k in range(100000):
#    for i in range(1, n-1):
#        r = 1/2 * (f[i-1] + f[i+1] - g/alpha*(dx**2.)) - f[i]
#        f[i] += (1-w)*f[i] + w*r


#plt.plot(x, f)
#plt.title('1D Poisson')
#plt.show()
