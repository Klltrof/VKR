import math

from dim3_scheme import general_group_equation
from matplotlib import pyplot as plt
import numpy as np

u = 0.012277471
u_ = 1 - u
T = 17.0652165601579

d1 = lambda x, y: ((x + u) ** 2 + y ** 2) ** (3 / 2)
d2 = lambda x, y: ((x - u_) ** 2 + y ** 2) ** (3 / 2)


def norma2(vector):
    return sum(x ** 2 for x in vector) ** (1 / 2)


def test_equation(t, x, y, z, dx, dy, dz):
    return 0


def eq1(t, x, y, z, dx, dz):
    return y + 2 * dz - u_ * (y + u) / d1(y, z) - u * (y - u_) / d2(y, z)


def eq2(t, x, y, z, dx, dy):
    return z - 2 * dy - u_ * z / d1(y, z) - u * z / d2(y, z)


def eq3(t, x, y, z, dx, dy, dz):
    return x + 2 * dy - u_ * (x + u) / d1(x, y) - u * (x - u_) / d2(x, y)


def eq4(t, x, y, z, dx, dz):
    return y - 2 * dx - u_ * y / d1(x, y) - u * y / d2(x, y)


def eq5(t, x, y, z, dx, dy, dz):
    return x + 2 * dz - u_ * (x + u) / d1(x, z) - u * (x - u_) / d2(x, z)


def eq6(t, x, y, z, dx, dy):
    return z - 2 * dx - u_ * z / d1(x, z) - u * z / d2(x, z)


def eq11(t, x, y, dx, dy):
    return x + 2 * dy - u_ * (x + u) / d1(x, y) - u * (x - u_) / d2(x, y)


def eq12(t, x, y, dx, dy):
    return y - 2 * dx - u_ * y / d1(x, y) - u * y / d2(x, y)
