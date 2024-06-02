import math

from dim3_scheme import general_group_equation, combination_1_1
from arenstorf_orbit import norma2


def Calc(t_start, t_end, h_start, tol, values, f, p, s, facmax=5.0, facmin=0.2, fac=0.8):
    x_prev, dx_prev, y_prev, dy_prev, z_prev, dz_prev = (x for x in values)
    error = 0
    result = {t_start: (x_prev, dx_prev, y_prev, dy_prev, z_prev, dz_prev, error)}
    current_t = t_start
    steps = 1

    delta = (1 / max(abs(t_start), abs(t_end))) ** (p + 1) + norma2((f[0](t_start,
                                                                          x_prev,
                                                                          y_prev,
                                                                          z_prev,
                                                                          dx_prev,
                                                                          dy_prev,
                                                                          dz_prev),
                                                                     f[1](t_start,
                                                                          x_prev,
                                                                          y_prev,
                                                                          z_prev,
                                                                          dx_prev,
                                                                          dz_prev),
                                                                     f[2](t_start,
                                                                          x_prev,
                                                                          y_prev,
                                                                          z_prev,
                                                                          dx_prev,
                                                                          dy_prev))) ** (p + 1)
    h = (tol / delta) ** (1 / (p + 1)) if h_start == 'auto' else h_start

    while t_end - current_t > 0:
        temp = general_group_equation(current_t, x_prev, y_prev, z_prev, dx_prev, dy_prev, dz_prev, h, f[0], f[1], f[2])
        error = temp[6]
        steps += 1

        if error < tol:
            current_t += h
            result[current_t] = temp
            x_prev, dx_prev, y_prev, dy_prev, z_prev, dz_prev = (temp[i] for i in range(0, 6))
        h = h * min(facmax, max(facmin, fac * ((tol / error) ** (1 / (p + 1)))))

        if t_end - current_t - h < 0:
            h = t_end - current_t
            temp = general_group_equation(current_t, x_prev, y_prev, z_prev, dx_prev, dy_prev, dz_prev, h, f[0], f[1],
                                          f[2])
            error = temp[6]
            steps += 1

            if error < tol:
                current_t += h
                result[current_t] = temp
                break
            else:
                h = h / 2

    return result, steps


def Calc_1_1(t_start, t_end, h_start, tol, values, f, method, p, s, facmax=5.0, facmin=0.2, fac=0.8):
    x_prev, dx_prev, y_prev, dy_prev = (x for x in values)
    error = 0
    result = {t_start: (x_prev, dx_prev, y_prev, dy_prev, error)}
    current_t = t_start
    steps = 1

    delta = (1 / max(abs(t_start), abs(t_end))) ** (p + 1) + norma2((f[i](t_start,
                                                                          x_prev,
                                                                          y_prev,
                                                                          dx_prev,
                                                                          dy_prev) for i in range(0, 2))) ** (p + 1)
    h = (tol / delta) ** (1 / (p + 1)) if h_start == 'auto' else h_start

    while t_end - current_t > 0:
        temp = method(current_t, x_prev, y_prev, dx_prev, dy_prev, h, f[0], f[1])
        error = temp[4]
        steps += 1

        if error < tol:
            current_t += h
            result[current_t] = temp
            x_prev, dx_prev, y_prev, dy_prev = (temp[i] for i in range(0, 4))
        h = h * min(facmax, max(facmin, fac * ((tol / error) ** (1 / (p + 1)))))

        if t_end - current_t - h < 0:
            h = t_end - current_t
            temp = method(current_t, x_prev, y_prev, dx_prev, dy_prev, h, f[0], f[1])
            error = temp[4]
            steps += 1

            if error < tol:
                current_t += h
                result[current_t] = temp
                break
            else:
                h = h / 2

    return result, steps


# equations = (
#   lambda t, x, y, z, dx, dy, dz: 0,
#   lambda t, x, y, z, dx, dz: 1,
#   lambda t, x, y, z, dx, dy: 1
# )
def Calc_23_method_by_tol_interval(tol_start, tol_end, x_0, equations, interval, x_end='periodic', fac=0.8):
    x_end = x_0 if x_end == 'periodic' else -1

    tols = [10 ** (-i) for i in [-math.log10(tol_start) + x * 0.25 for x in range(0, 1 + 4 * int(-math.log10(tol_end) +
                                                                                                 math.log10(
                                                                                                     tol_start)))]]
    global_errors, steps = [], []

    for current_tol in tols:
        current_result, current_steps = Calc(t_start=interval[0],
                                             t_end=interval[1],
                                             h_start='auto',
                                             tol=current_tol,
                                             values=x_0,
                                             f=equations,
                                             p=6,
                                             s=7,
                                             facmax=5.0,
                                             facmin=0.2,
                                             fac=fac)
        current_new_x_0 = current_result[interval[1]]
        steps.append((current_steps, len(current_result)))
        global_errors.append(norma2([current_new_x_0[i] - x_end[i] for i in range(0, 6)]))

    result = {
        'tols': tols,
        'steps': steps,
        'global_errors': global_errors
    }

    return result


# equations = (
#   lambda t, x, y, dx, dy: 1,
#   lambda t, x, y, dx, dy: 1
# )
def Calc_other_method_by_tol_interval(tol_start, tol_end, x_0, equations, interval, method, p, s, fac=0.8,
                                      x_end='periodic'):
    x_end = x_0 if x_end == 'periodic' else -1

    tols = [10 ** (-i) for i in [-math.log10(tol_start) + x * 0.25 for x in range(0, 1 + 4 * int(-math.log10(tol_end) +
                                                                                                 math.log10(
                                                                                                     tol_start)))]]
    global_errors, steps = [], []

    for current_tol in tols:
        current_result, current_steps = \
            Calc_1_1(t_start=interval[0],
                     t_end=interval[1],
                     h_start='auto',
                     tol=current_tol,
                     values=x_0,
                     f=equations,
                     method=method,
                     p=p,
                     s=s,
                     facmax=5.0,
                     facmin=0.2,
                     fac=fac)
        current_new_x_0 = current_result[interval[1]]
        steps.append((current_steps, len(current_result)))
        global_errors.append(norma2([current_new_x_0[i] - x_end[i] for i in range(0, 4)]))

    result = {
        'tols': tols,
        'steps': steps,
        'global_errors': global_errors
    }

    return result
