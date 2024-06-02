import math
import numpy as np
from matplotlib import pyplot as plt
from other_methods import FehlbergRK67, FehlbergRK45, DoPriRK54, DoPriRK65
from calculation import Calc, Calc_1_1
from dim3_scheme import general_group_equation

from arenstorf_orbit import T, eq1, eq2, test_equation, norma2
from test_task import tt1, tt2

x_0 = (1, 0, 0, 1)
equations = (tt1, tt2)
interval = (0, 2 * math.pi)

result, steps = Calc_1_1(t_start=0,
                         t_end=interval[1],
                         h_start='auto',
                         tol=1e-3,
                         values=x_0,
                         f=equations,
                         method=DoPriRK54,
                         p=5,
                         s=6,
                         facmax=5.0,
                         facmin=0.2,
                         fac=0.8)

new_x_0 = result[interval[1]]

print(-math.log10(norma2([new_x_0[i] - x_0[i] for i in range(0, 4)])))
print(len(result) * 12, steps * 12)

stepsize1 = []
last_t = 0

alpha = 1
betta = 2

x = np.array([3, 0, -2, 0])

true_errors = dict()

for key, value in result.items():
    stepsize1.append((last_t, key - last_t))
    last_t = key

    true_result = (
    x[0] * np.cos(alpha * key) + x[1] * np.sin(alpha * key) + x[2] * np.cos(betta * key) + x[3] * np.sin(betta * key),
    x[0] * -np.sin(alpha * key) + x[1] * np.cos(alpha * key) + x[2] * -np.sin(betta * key) + x[3] * np.cos(betta * key),
    x[0] * -alpha * np.sin(alpha * key) + x[1] * alpha * np.cos(alpha * key) + x[2] * -betta * np.sin(betta * key) + x[
        3] * betta * np.cos(betta * key),
    x[0] * -alpha * np.cos(alpha * key) + x[1] * -alpha * np.sin(alpha * key) + x[2] * -betta * np.cos(betta * key) + x[
        3] * -betta * np.sin(betta * key))
    print(key, value)
    print(true_result)

    true_local_error = norma2((value[0] - true_result[0],
                               value[1] - true_result[2],
                               value[2] - true_result[1],
                               value[3] - true_result[3]))

    true_errors[key] = (true_local_error, value[4]) if key != 0 else (0, 1)

    a = np.array([[np.cos(alpha * key), np.sin(alpha * key), np.cos(betta * key), np.sin(betta * key)],
                  [-np.sin(alpha * key), np.cos(alpha * key), -np.sin(betta * key), np.cos(betta * key)],
                  [-alpha * np.sin(alpha * key), alpha * np.cos(alpha * key), -betta * np.sin(betta * key),
                   betta * np.cos(betta * key)],
                  [-alpha * np.cos(alpha * key), -alpha * np.sin(alpha * key), -betta * np.cos(betta * key),
                   -betta * np.sin(betta * key)]])
    b = np.array([value[0],
                  value[2],
                  value[1],
                  value[3]])
    x = np.linalg.solve(a, b)
    print(x)

#plt.plot([x[0] for x in stepsize], [x[1] for x in stepsize])
#plt.show()

#plt.plot(true_errors.keys(), [(true_errors[x][0]) for x in true_errors.keys()], color='blue')
#plt.plot(true_errors.keys(), [(true_errors[x][1]) for x in true_errors.keys()], color='red')

plt.plot(true_errors.keys(), [(true_errors[x][0] / (true_errors[x][1])) for x in true_errors.keys()], color='green')


result, steps = Calc_1_1(t_start=0,
                         t_end=interval[1],
                         h_start='auto',
                         tol=1e-5,
                         values=x_0,
                         f=equations,
                         method=DoPriRK54,
                         p=5,
                         s=6,
                         facmax=5.0,
                         facmin=0.2,
                         fac=0.8)

new_x_0 = result[interval[1]]



stepsize2 = []
last_t = 0

alpha = 1
betta = 2

x = np.array([3, 0, -2, 0])

true_errors = dict()

for key, value in result.items():
    stepsize2.append((last_t, key - last_t))
    last_t = key

    true_result = (
    x[0] * np.cos(alpha * key) + x[1] * np.sin(alpha * key) + x[2] * np.cos(betta * key) + x[3] * np.sin(betta * key),
    x[0] * -np.sin(alpha * key) + x[1] * np.cos(alpha * key) + x[2] * -np.sin(betta * key) + x[3] * np.cos(betta * key),
    x[0] * -alpha * np.sin(alpha * key) + x[1] * alpha * np.cos(alpha * key) + x[2] * -betta * np.sin(betta * key) + x[
        3] * betta * np.cos(betta * key),
    x[0] * -alpha * np.cos(alpha * key) + x[1] * -alpha * np.sin(alpha * key) + x[2] * -betta * np.cos(betta * key) + x[
        3] * -betta * np.sin(betta * key))
    print(key, value)
    print(true_result)

    true_local_error = norma2((value[0] - true_result[0],
                               value[1] - true_result[2],
                               value[2] - true_result[1],
                               value[3] - true_result[3]))

    true_errors[key] = (true_local_error, value[4]) if key != 0 else (0, 1)

    a = np.array([[np.cos(alpha * key), np.sin(alpha * key), np.cos(betta * key), np.sin(betta * key)],
                  [-np.sin(alpha * key), np.cos(alpha * key), -np.sin(betta * key), np.cos(betta * key)],
                  [-alpha * np.sin(alpha * key), alpha * np.cos(alpha * key), -betta * np.sin(betta * key),
                   betta * np.cos(betta * key)],
                  [-alpha * np.cos(alpha * key), -alpha * np.sin(alpha * key), -betta * np.cos(betta * key),
                   -betta * np.sin(betta * key)]])
    b = np.array([value[0],
                  value[2],
                  value[1],
                  value[3]])
    x = np.linalg.solve(a, b)

plt.plot(true_errors.keys(), [(true_errors[x][0] / (true_errors[x][1])) for x in true_errors.keys()], color='blue')

result, steps = Calc_1_1(t_start=0,
                         t_end=interval[1],
                         h_start='auto',
                         tol=1e-7,
                         values=x_0,
                         f=equations,
                         method=DoPriRK54,
                         p=5,
                         s=6,
                         facmax=5.0,
                         facmin=0.2,
                         fac=0.8)

new_x_0 = result[interval[1]]

stepsize3 = []
last_t = 0

alpha = 1
betta = 2

x = np.array([3, 0, -2, 0])

true_errors = dict()

for key, value in result.items():
    stepsize3.append((last_t, key - last_t))
    last_t = key

    true_result = (
        x[0] * np.cos(alpha * key) + x[1] * np.sin(alpha * key) + x[2] * np.cos(betta * key) + x[3] * np.sin(
            betta * key),
        x[0] * -np.sin(alpha * key) + x[1] * np.cos(alpha * key) + x[2] * -np.sin(betta * key) + x[3] * np.cos(
            betta * key),
        x[0] * -alpha * np.sin(alpha * key) + x[1] * alpha * np.cos(alpha * key) + x[2] * -betta * np.sin(betta * key) +
        x[
            3] * betta * np.cos(betta * key),
        x[0] * -alpha * np.cos(alpha * key) + x[1] * -alpha * np.sin(alpha * key) + x[2] * -betta * np.cos(
            betta * key) + x[
            3] * -betta * np.sin(betta * key))
    print(key, value)
    print(true_result)

    true_local_error = norma2((value[0] - true_result[0],
                               value[1] - true_result[2],
                               value[2] - true_result[1],
                               value[3] - true_result[3]))

    true_errors[key] = (true_local_error, value[4]) if key != 0 else (0, 1)

    a = np.array([[np.cos(alpha * key), np.sin(alpha * key), np.cos(betta * key), np.sin(betta * key)],
                  [-np.sin(alpha * key), np.cos(alpha * key), -np.sin(betta * key), np.cos(betta * key)],
                  [-alpha * np.sin(alpha * key), alpha * np.cos(alpha * key), -betta * np.sin(betta * key),
                   betta * np.cos(betta * key)],
                  [-alpha * np.cos(alpha * key), -alpha * np.sin(alpha * key), -betta * np.cos(betta * key),
                   -betta * np.sin(betta * key)]])
    b = np.array([value[0],
                  value[2],
                  value[1],
                  value[3]])
    x = np.linalg.solve(a, b)

plt.plot(true_errors.keys(), [(true_errors[x][0] / (true_errors[x][1])) for x in true_errors.keys()], color='black')

plt.title('DoPri54. true_local_error / error')
plt.legend(('1e-3', '1e-5', '1e-7'))
plt.show()


plt.title('DoPri54. step_size')
plt.legend(('1e-3', '1e-5', '1e-7'))
plt.plot([x[0] for x in stepsize1], [x[1] for x in stepsize1], color='green')
plt.plot([x[0] for x in stepsize2], [x[1] for x in stepsize2], color='blue')
plt.plot([x[0] for x in stepsize3], [x[1] for x in stepsize3], color='black')
plt.show()