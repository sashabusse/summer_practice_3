#progon test
import numpy as np
from main import progon

a = np.array([0, -2, 0.1, -1])
b = np.array([10.0, 9, 4, 8])
c = np.array([1, 1, -1, 0])
d = np.array([5, -1, -5, 40])

print('answer:')
print('x = ', end='')
print(progon(a, b, c, d))
print()
print('right answer is:')
print('x = [0.5 0.  0.  5. ]')