import numpy as np
import math
from sympy import *

a1 = 40
a2 = 22
b = 0
c1 = 79
c2 = 95
c3 = 152
# góc khớp đầu vào

q1, q2, q3, q4, q5, q6 = symbols("q1 q2 q3 q4 q5 q6")
# forward kinematics
psi3 = math.atan((a2/c3))
k = math.sqrt(a2**2 + c3**2)
cx1 = c2*sin(q2) + k*sin(q2+q3+psi3)+a1
cy1 = b
cz1 = c2*cos(q2) + k*cos(q2+q3+psi3)
cx0 = cx1*cos(q1) - cy1*sin(q1)
cy0 = cx1*sin(q1) + cy1*cos(q1)
cz0 = cz1 + c1
#####
s1 = sin(q1)
s2 = sin(q2)
s3 = sin(q3)
s4 = sin(q4)
s5 = sin(q5)
s6 = sin(q6)
c1 = cos(q1)
c2 = cos(q2)
c3 = cos(q3)
c4 = cos(q4)
c5 = cos(q5)
c6 = cos(q6)

R_0c = np.array(
    [[c1*c2*c3-c1*s2*s3, -s1, c1*c2*s3+c1*s2*c3], [s1*c2*c3-s1*s2*s3, c1, s1*c2*s3+s1*s2*c3], [-s2*c3-c2*s3, 0, -s2*s3+c2*c3]])
R_ce = np.array([[4*c5*c6-s4*s6, -c4*c5*s6-s4*c6, c4*s5],
                [s4*c5*c6+c4*s6, -s4*c5*s6+c4*c6, s4*s5], [-s5*c6, s5*s6, c5]])
R_0e = np.dot(R_0c, R_ce)
print("R_0c = ", R_0c)
print("R_ce = ", R_ce)
print("R_0e = ", R_0e)
# c4 = 415
# A = np.array([0, 0, 1])
# B = np.array([[1], [2], [3]])
# # B = np.array([1, 0, 0, 0])
# u = np.array([cx0, cy0, cz0]).T + np.dot((c4*R_0e), A.T)
