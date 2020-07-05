import numpy as np
from matplotlib import pyplot as plt
from main import solve_equation


def k(x):
    return np.sqrt(np.e)


def dk_dx(x):
    return 0


def q(x):
    return np.sqrt(np.e)


def f(x):
    return np.sin(0.5)

N = 10
eps = 1e-4
x = np.linspace(0, 1, N)

#граничные условия в виде
#alpha[0]*u(0) + alpha[1]*u'(0) = alpha[2]
#betta[0]*u(0) + betta[1]*u'(0) = betta[2]
alpha = np.array([0, k(0), 0])
betta = np.array([1, k(1), 0])

y = solve_equation(0, 1, alpha, betta, k, dk_dx, q, f, N, eps)


plt.plot(x, y)
plt.grid(True)


C = -f(0)/(q(0)*(np.e*(k(0)+1)+1/np.e*(1-k(0))))
y_proof = C*np.exp(x)+C*np.exp(-x)+f(0)/q(0)

plt.plot(x, y_proof)
plt.show()