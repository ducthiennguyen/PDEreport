import numpy as np
import matplotlib.pyplot as plt

#Investigate steady-state condition given boundary conditions (Dirichlet). Use poisson equation by assigning external forcing (e.g. g).
alpha = 5.
g = 9.8
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
T[20:30, 20:30] = 400

# for k in range(15001):
#     r = 1/4 * (T[2:n, 1:n-1] + T[0:n-2, 1:n-1] + T[1:n-1, 2:n] + T[1:n-1, 0:n-2] - (dx**2.)*g/alpha) - T[1:n-1, 1:n-1]
#     T[1:n-1, 1:n-1] += (1-w) * T[1:n-1, 1:n-1] + w*r
#     if k % 500 != 0: continue
#     plt.contourf(x, y, T, cmap = 'rainbow', vmin=-1400, vmax=400)
#     plt.colorbar()
#     plt.title('Iteration%d'%(k))
#     plt.savefig('GaussSeidel%d.png'%(k))
#     plt.clf()
#     plt.cla()

#Investigate various boundary conditions (non-steady state) by discussing its effects using animation

d = 0.1
alpha = 5.
len_x = 100
len_y = 100
nt = 500
dx = 1
dy = 1
dt = d * (dx**2) / alpha
grid_x = int(len_x/dx)
grid_y = int(len_y/dy)

x = np.linspace(0, len_x+dx, grid_x)
y = np.linspace(0, len_y+dy,grid_y)

T = np.zeros((grid_x, grid_y))
T[:, 0] = 30
T[:, -1] = 70.5
T[0, :] = 50
T[10:20, 20:30] = 237

def fdm(T):
#    Top row
    # T[grid_x-1, 1:grid_y-1] += d * (T[grid_x-2, 1:grid_y-1] + T[grid_x-2, 1:grid_y-1] + T[grid_x-1, 2:grid_y] + T[grid_x-1, 0:grid_y-2] - 4 * T[grid_x-1, 1:grid_y-1])
#    Right column
    # T[1:grid_x-1, grid_y-1] += d * (T[1:grid_x-1, grid_y-2] + T[1:grid_x-1, grid_y-2] + T[2:grid_x, grid_y-1] + T[0:grid_x-2, grid_y-1] - 4 * T[1:grid_x-1, grid_y-1])
#    Bottom row
    # T[0, 1:grid_y-1] += d * (T[1, 1:grid_y-1] + T[1, 1:grid_y-1] + T[0, 2:grid_y] + T[0, 0:grid_y-2] - 4 * T[0, 1:grid_y-1])
# #    Left column
    # T[1:grid_x-1, 0] += d * (T[1:grid_x-1, 1] + T[1:grid_x-1, 1] + T[2:grid_x, 0] + T[0:grid_x-2, 0] - 4 * T[1:grid_x-1, 0])

    T[1:grid_x-1, 1:grid_y-1] += d * (T[2:grid_x, 1:grid_y-1] + T[0:grid_x-2, 1:grid_y-1] + T[1:grid_x-1, 2:grid_y] + T[1:grid_x-1, 0:grid_y-2] - 4 * T[1:grid_x-1, 1:grid_y-1])

    return T

plt.contourf(x, y, T, cmap = 'rainbow')
plt.colorbar()
plt.title('Initial distribution')
plt.savefig('Initial.png')
plt.clf()
plt.cla()

for t in range(0, nt):
    T = fdm(T)
    # plt.contourf(x, y, T, cmap = 'rainbow')
    # plt.colorbar()
    # plt.title('Time %.5f'%(t*dt))
    # plt.savefig('GaussSeidel%d.png'%(t))
    # plt.clf()
    # plt.cla()

plt.contourf(x, y, T, cmap = 'rainbow')
plt.colorbar()
plt.title('Time %.3f distribution'%((nt-1)*dt))
plt.savefig('Dirichlet%d'%(nt-1))
plt.clf()
plt.cla()
