import numpy as np
from matplotlib import pyplot as plt
from main import concrete_approximation

def k(x):
    return np.sqrt(np.e)


def dk_dx(x):
    return 0


def q(x):
    return np.sqrt(np.e)


def f(x):
    return np.sin(0.5)



N = 1000
x = np.linspace(0, 1, N)

#граничные условия в виде
#alpha[0]*u(0) + alpha[1]*u'(0) = alpha[2]
#betta[0]*u(0) + betta[1]*u'(0) = betta[2]
alpha = np.array([0, k(0), 0])
betta = np.array([1, k(1), 0])

y = concrete_approximation(x, alpha, betta, k, dk_dx, q, f)

plt.plot(x, y)
plt.grid(True)
#plt.show()

C = -f(0)/(q(0)*(np.e*(k(0)+1)+1/np.e*(1-k(0))))

y_proof = C*np.exp(x)+C*np.exp(-x)+f(0)/q(0)
print(f(0)/q(0))

print('result:')
print(y)
print('Check:')
print(y_proof)

plt.plot(x, y_proof)
plt.show()