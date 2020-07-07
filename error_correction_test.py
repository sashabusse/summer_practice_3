import numpy as np
from matplotlib import pyplot as plt
from main import solve_equation

#model task functions are constants
def k(x):
    return np.sqrt(np.e)


def dk_dx(x):
    return 0


def q(x):
    return np.sqrt(np.e)


def f(x):
    return np.sin(0.5)

#setting up N and eps
N = 11
eps = 1e-4

x = np.linspace(0, 1, N)

#boundary condition
#alpha[0]*u(0) + alpha[1]*u'(0) = alpha[2]
#betta[0]*u(1) + betta[1]*u'(1) = betta[2]
alpha = np.array([0, k(0), 0])
betta = np.array([1, k(1), 0])

#invoke solve_equation to calculate answer
y = solve_equation(0, 1, alpha, betta, k, dk_dx, q, f, N, eps)

#plot result
plt.plot(x, y)
plt.grid(True)


#plot analytical solution for model task to chek if algorithm works right
C = -f(0)/(q(0)*(np.e*(k(0)+1)+1/np.e*(1-k(0))))
y_proof = C*np.exp(x)+C*np.exp(-x)+f(0)/q(0)

plt.plot(x, y_proof)
plt.show()