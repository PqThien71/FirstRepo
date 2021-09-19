import numpy as np
from sympy import *

x1, x2, x3 = symbols("x1 x2 x3")
u = np.array([x1, x2, x3])
# Thong so hinh hoc robot
a1 = 40
a2 = 22
b1 = 0
c1 = 79
c2 = 95
c3 = 152
c4 = 41.5

# Huong khau thao tac
d = np.array([0, 0, -1])
print(d[2])
# Ma tran dinh huong toa do khau thao tac
EE = np.array([[1, 0, 0, 0], [u[0], d[2], 0, 0], [
              u[1], 0, 1, 0], [u[2], 0, 0, d[2]]])

# print(EE[1][0]-EE[1][3]*c4)
# print(EE[1, 1:4])
# Toa do dinh huong diem C

C = np.array([[1, 0, 0, 0], [EE[1][0]-EE[1][3]*c4, EE[1][1],
             0, 0], [EE[2][0]-EE[2][3]*c4, 0, 1, 0], [EE[3][0]-EE[3][3]*c4, 0, 0, EE[3][3]]])
