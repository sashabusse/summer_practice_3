import numpy as np



# метод прогонки
# вывод рекурентных соотношений читайте сами
def progon(a, b, c, d):
    n = len(a)
    U = np.zeros((n,))
    V = np.zeros((n,))

    U[0] = -c[0]/b[0]
    V[0] = d[0]/b[0]

    for i in range(1,n):
        U[i] = -c[i]/(a[i]*U[i-1]+b[i])
        V[i] = (d[i] - a[i]*V[i-1])/(a[i]*U[i-1] + b[i])

    x = np.zeros((n,))
    x[n-1] = V[n-1]

    for i in range(1, n):
        j = n - 1 - i
        x[j] = U[j]*x[j+1] + V[j]

    return x





#boundary condition
#alpha[0]*u(0) + alpha[1]*u'(0) = alpha[2]
#betta[0]*u(1) + betta[1]*u'(1) = betta[2]
#k, dk_dx, q, f. functions given in task
#this function solves equation with given x -> y
def concrete_approximation(x, alpha, betta, k, dk_dx, q, f):
    #deriving N and h from x
    N = len(x)
    h = (x[len(x)-1]-x[0])/N

    #preaparing data for progon
    a = np.zeros((N,))
    b = np.zeros((N,))
    c = np.zeros((N,))
    d = np.zeros((N,))

    #first and last element from boundary conditions
    a[0] = 0
    b[0] = alpha[0] - alpha[1]/h
    c[0] = alpha[1]/h
    d[0] = alpha[2]

    a[N-1] = -betta[1]/h
    b[N-1] = betta[0] + betta[1]/h
    c[N-1] = 0
    d[N-1] = betta[2]

    for i in range(1, N-1):
        xi = x[i]
        ki = k(xi)
        dki = dk_dx(xi)
        qi = q(xi)
        fi = f(xi)

        a[i] = ki/(h**2)-dki/(2*h)
        b[i] = -2*ki/(h**2) - qi
        c[i] = ki/(h**2)+dki/(2*h)
        d[i] = -fi

    y = progon(a, b, c, d)
    return y



#error control (scales N until error<eps)
def solve_equation(x_min, x_max, alpha, betta, k, dk_dx, q, f, N = 11, eps = 1e-4):
    N0 = N
    diff = 2*eps
    x = np.linspace(x_min, x_max, N)
    y = concrete_approximation(x, alpha, betta, k, dk_dx, q, f)
    while diff > eps:
        x2 = np.linspace(x_min, x_max, 2*N)
        y2 = concrete_approximation(x2, alpha, betta, k, dk_dx, q, f)

        diff = np.abs(y2[::2] - y).max()
        y = y2
        N *= 2

    j = N//N0
    j = j+j//N0+1
    N = j*(N0-1) + 1

    x = np.linspace(x_min, x_max, N)
    y = concrete_approximation(x, alpha, betta, k, dk_dx, q, f)
    return y[::j]

