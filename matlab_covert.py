import numpy as np
import math

# q = np.array([q1, q2, q3])

H_01 = np.zeros([4, 4])
H_02 = np.zeros([4, 4])
H_03 = np.zeros([4, 4])
H_12 = np.zeros([4, 4])
H_23 = np.zeros([4, 4])

H_test = np.array([["a", 2, 3], ["b", 5, 6], ["b", 5, 6]])
H_test2 = np.dot(H_test, H_test)
print(H_test2)

N = np.matrix([a, b], [1, 2])


M = np.array([[q1, "d1", 0, math.pi/2], ["q2", "a1", 0,
             math.pi/2], [-math.pi/2, "d3", "a3", 0]])
print(M)
for i in range(1, 4):
    fi = M[i, 1]
    d = M[i, 2]
    a = M[i, 3]
    anpha = M[i, 4]
    H = np.array([[math.cos(fi), -math.sin(fi) *
                  math.cos(anpha), math.sin(fi)*math.sin(anpha), a*math.cos(fi)], [math.sin(fi), math.cos(fi)*math.cos(anpha), -math.cos(fi)*math.sin(anpha), a*math.sin(fi)], [0, math.sin(anpha), math.cos(anpha), d], [0, 0, 0, 1]])
    if i == 1:
        H_01 = H
    elif i == 2:
        H_12 = H
    elif i == 3:
        H_23 = H

H_02 = np.dot(H_01, H_12)
H_03 = np.dot(H_12, H_23)

X_E = H_03[0, 3]
Y_E = H_03[1, 3]
Z_E = H_03[2, 3]
