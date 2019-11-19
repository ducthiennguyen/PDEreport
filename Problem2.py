import numpy as np
import matplotlib.pyplot as plt


#u[i][j] += (v / (dx**2.) * (u[i+1][j] + u[i-1][j] + u[i][j+1] + u[i][j-1]) - a / dx * (2*u[i][j] -u[i-1][j] - u[i][j-1])) * dt

a = 0.1
v = 0.005
L = 10
dx = 0.5
dy = dx
n = int(L/dx)
dt = 0.1
tend = 25
nt = int(tend/dt)
x = np.linspace(0, L, n)
y = np.linspace(0, L, n)

u = np.zeros((n, n))
u[:, 0] = 0.1
u[:, n-1] = 0.2
u[0, :] = 0.3
u[15:18, 15:18] = 2.37

for k in range(nt):

    plt.contourf(x, y, u, cmap = 'rainbow')
    plt.colorbar()
    plt.title('%.3f'%(k*dt))
    plt.savefig('variable_a%03.3d.png'%(k))
    plt.clf()
    plt.cla()

    # for i in range(1, n-1):
    #     for j in range(1, n-1):
    #         u[i][j] += (v / (dx**2.) * (u[i+1][j] + u[i-1][j] + u[i][j+1] + u[i][j-1] - 4*u[i][j]) - (u[i][j] / dx) * (2*u[i][j] - u[i-1][j] - u[i][j-1])) * dt

    u = u + (v / (dx**2.) * (np.roll(u, -1, axis = 0) + np.roll(u, 1, axis = 0) + np.roll(u, -1, axis = 1) + np.roll(u, 1, axis = 1) - 4*u) - \
    (u / dx) * (2*u - np.roll(u, 1, axis = 0) - np.roll(u, 1, axis = 1))) * dt
