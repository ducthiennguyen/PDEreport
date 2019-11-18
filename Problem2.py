import numpy as np
import matplotlib.pyplot as plt


#u[i][j] += (v / (dx**2.) * (u[i+1][j] + u[i-1][j] + u[i][j+1] + u[i][j-1]) - a / dx * (2*u[i][j] -u[i-1][j] - u[i][j-1])) * dt

a = 1
v = 0.1
L = 10
dx = 0.8
dy = dx
n = int(L/dx)
dt = 0.1
tend = 20
nt = int(tend/dt)
x = np.linspace(0, L, n)
y = np.linspace(0, L, n)

u = np.zeros((n, n))
u[:, 0] = 0.75
u[:, n-1] = 0.30
u[0, :] = 2.37
u[20:30, 20:30] = 10.0

for k in range(nt):
    for i in range(1, n-1):
        for j in range(1, n-1):
            u[i][j] += (v / (dx**2.) * (u[i+1][j] + u[i-1][j] + u[i][j+1] + u[i][j-1] - 4*u[i][j]) - (u[i][j] / dx) * (2*u[i][j] - u[i-1][j] - u[i][j-1])) * dt

    plt.contourf(x, y, u, cmap = 'rainbow')
    plt.colorbar()
    plt.title('%.3f'%(k*dt))
    plt.savefig('Thien_%03.3d.png'%(k))
    plt.clf()
    plt.cla()

