import numpy as np
from matplotlib import pyplot as plt
from main import solve_equation

#define functions
def k(x):
    return np.exp(x)


def dk_dx(x):
    return k(x)


def q(x):
    return np.exp(x)


def f(x):
    return np.sin(x)

#define N and eps
N = 100
eps = 1e-4
x = np.linspace(0, 1, N)

#boundary condition
#alpha[0]*u(0) + alpha[1]*u'(0) = alpha[2]
#betta[0]*u(1) + betta[1]*u'(1) = betta[2]
alpha = np.array([0, k(0), 0])
betta = np.array([1, k(1), 0])

#invoke function to solve eq.
y = solve_equation(0, 1, alpha, betta, k, dk_dx, q, f, N, eps)

#plot the function
plt.plot(x, y)
plt.grid(True)
plt.show()