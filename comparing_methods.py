import math

from calculation import Calc_1_1, Calc, Calc_23_method_by_tol_interval, Calc_other_method_by_tol_interval
from dim3_scheme import general_group_equation, combination_1_1
from other_methods import FehlbergRK67, DoPriRK54, FehlbergRK45, DoPriRK65
from arenstorf_orbit import T, eq11, eq12, norma2, eq1, eq2
from matplotlib import pyplot as plt
from test_task import tt1, tt2

tasks = {
    1: 'Задача Аренсторфа',
    2: 'Модельная задача'
}

methods = {
    1: 'Dim3scheme',
    2: 'Fehlberg',
    3: 'DoPri'
}

method = (1, 2, 3)
task = 1
tol_start, tol_end, tol_start_Fehlberg, tol_end_Fehlberg = 1e-7, 1e-10, 1e-7, 1e-11
tol_start_DoPri65, tol_end_DoPri65 = 1e-7, 1e-11

if task == 1:
    x_0_11 = x_0_Fehlberg = x_0_DoPri = (0.994, 0, 0, -2.00158510637908252240537862224)
    x_0_23 = (0, 0, 0.994, 0, 0, -2.00158510637908252240537862224)
    equations23 = (lambda t, x, y, z, dx, dy, dz: 0, eq1, eq2)
    equations = (eq11, eq12)
    interval = (0, T)
else:
    x_0_11 = x_0_Fehlberg = x_0_DoPri = (1, 0, 0, 1)
    x_0_23 = (0, 0, 1, 0, 0, 1)
    equations23 = (lambda t, x, y, z, dx, dy, dz: 0,
                   lambda t, x, y, z, dx, dz: 3 * dz + 2 * y,
                   lambda t, x, y, z, dx, dy: -3 * dy + 2 * z)
    equations = (tt1, tt2)
    interval = (0, 2 * math.pi)

tols = [10 ** (-i) for i in [-math.log10(tol_start) + x * 0.25 for x in range(0, 1 + 4 * int(-math.log10(tol_end) +
                                                                                             math.log10(tol_start)))]]

tols_Fehlberg = [10 ** (-i) for i in [-math.log10(tol_start_Fehlberg) + x * 0.25 for x in range(0,
                                                                                                1 + 4 * int(-math.log10(
                                                                                                    tol_end_Fehlberg) + math.log10(
                                                                                                    tol_start_Fehlberg)))]]

tols_DoPri = [10 ** (-i) for i in [-math.log10(tol_start_DoPri65) + x * 0.25 for x in range(0,
                                                                                             1 + 4 * int(-math.log10(
                                                                                                 tol_end_DoPri65) + math.log10(
                                                                                                 tol_start_DoPri65)))]]

result_23_64 = Calc_23_method_by_tol_interval(tol_start, tol_end, x_0_23, equations23, interval, fac=0.8)

result_Fehlberg67 = Calc_other_method_by_tol_interval(tol_start_Fehlberg, tol_end_Fehlberg, x_0_Fehlberg, equations,
                                                      interval,
                                                      FehlbergRK67, 6, 10, fac=0.8)
result_DoPri54 = Calc_other_method_by_tol_interval(tol_start, tol_end, x_0_DoPri, equations, interval,
                                                   DoPriRK54, 5, 6, fac=0.8)

global_errors_23_64, steps_23_64 = result_23_64['global_errors'], result_23_64['steps']
global_errors_Fehlberg67, steps_Fehlberg67 = result_Fehlberg67['global_errors'], result_Fehlberg67['steps']
global_errors_DoPri54, steps_DoPri54 = result_DoPri54['global_errors'], result_DoPri54['steps']

plt.plot([-math.log10(x) for x in tols_Fehlberg], [math.log10(x[0]) for x in steps_Fehlberg67], color='blue')
plt.plot([-math.log10(x) for x in tols], [math.log10(x[0]) for x in steps_DoPri54], color='red')
plt.plot([-math.log10(x) for x in tols], [math.log10(x[0]) for x in steps_23_64], color='black')
plt.legend(('Fehlberg67', 'DoPri54', '23_64'))
plt.title(f'{tasks[task]}\n log10(fc) / -log10(tol)')
plt.show()

plt.plot([-math.log10(x) for x in tols_Fehlberg], [-math.log10(x) for x in global_errors_Fehlberg67], color='blue')
plt.plot([-math.log10(x) for x in tols], [-math.log10(x) for x in global_errors_DoPri54], color='red')
plt.plot([-math.log10(x) for x in tols], [-math.log10(x) for x in global_errors_23_64], color='black')
plt.legend(('Fehlberg67', 'DoPri54', '23_64'))
plt.title(f'{tasks[task]}\n global_error / -log10(tol)')
plt.show()

temp = {
    'Fehlberg67': (steps_Fehlberg67, global_errors_Fehlberg67, 20),
    'DoPri54': (steps_DoPri54, global_errors_DoPri54, 12),
    '23_64': (steps_23_64, global_errors_23_64, 12)
}

error_start = 1e-5
error_end = 1e-10

for method in temp.keys():
    for i, info in enumerate(temp[method][1]):
        if error_end < info < error_start:
            print(f"{method}: {temp[method][0][i][0]} шагов, {info} глобальная погрешность. (При tol = {tols[i]})")
            print(
                f"{method} затраты: {temp[method][0][i][0]} * {temp[method][2]} = {temp[method][0][i][0] * temp[method][2]}")
            break

plt.plot([math.log10(x[0] * 20) for x in steps_Fehlberg67], [-math.log10(x) for x in global_errors_Fehlberg67],
         color='blue')
plt.plot([math.log10(x[0] * 12) for x in steps_DoPri54], [-math.log10(x) for x in global_errors_DoPri54], color='red')
plt.plot([math.log10(x[0] * 12) for x in steps_23_64], [-math.log10(x) for x in global_errors_23_64], color='black')
plt.legend(('Fehlberg67', 'DoPri54', '23_64'))
plt.title(f'{tasks[task]}\n -log10(global_error) / log10(steps)')
plt.show()
