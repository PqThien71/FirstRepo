import numpy as np
from numpy.lib.type_check import isreal, real
import sympy as sp
import math

x1, x2, x3 = sp.symbols("x1 x2 x3", positive=True, real=True)
nx1 = sp.symbols("nx1")
u = np.array([50, 50, 0])
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
cx0 = C[1][0]
cy0 = C[2][0]
cz0 = C[3][0]
print(cx0, cy0, cz0)
nx1 = sp.sqrt(cx0**2+cy0**2-b1**2)-a1
s12 = nx1**2+(cz0-c1)**2
s22 = (nx1+2*a1)*2+(cz0-c1)*2
k = sp.sqrt(a2**2+c3**2)
theta = np.ones((3, 4))*1j
print((s12+c2**2-k**2)/(2*(s12**0.5)*c2))
if isreal(nx1):
    if isreal(nx1+a1):
        theta[0][0] = theta[0][1] = math.atan2(cy0, cx0)-math.atan2(b1, nx1+a1)
        theta[0][2] = theta[0][3] = math.atan2(
            cy0, cx0)+math.atan2(b1, nx1+a1)-math.pi
    theta[1][0] = -math.acos((s12+c2**2-k**2) /
                             (2*(s12**0.5)*c2))+math.atan2(nx1, cz0-c1)
    theta[1][1] = -theta[1][0]

    if isreal(nx1+2*a1):
        theta[1][2] = -math.acos((s22+c2**2-k**2) /
                                 (2*(s22**0.5)*c2))-math.atan2(nx1+2*a1, cz0-c1)
        theta[1][3] = -theta[1][2]
    theta[2][0] = math.acos((s12-c2**2-k**2)/(2*c2*k))-math.atan2(a2, c3)
    theta[2][1] = -theta[2][0]
    theta[2][2] = math.acos((s22-c2**2-k**2)/(2*c2*k))-math.atan2(a2, c3)
    theta[2][3] = - theta[2][2]

print(theta)
