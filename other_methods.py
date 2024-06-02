def FehlbergRK67(t, x_prev, y_prev, dx_prev, dy_prev, h, fdx, fdy,
                 fx=lambda t, x, y, dx, dy: dx,
                 fy=lambda t, x, y, dx, dy: dy):
    kx = dict()
    ky = dict()
    kdx = dict()
    kdy = dict()

    values = (x_prev, y_prev, dx_prev, dy_prev)

    k = [kx, ky, kdx, kdy]
    f = [fx, fy, fdx, fdy]

    for i in range(0, 4):
        k[i][0] = f[i](t, *values)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * (2 / 33) * k[j][0] for j in range(0, 4))
        k[i][1] = f[i](t + (2 / 33) * h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * (4 / 33) * k[j][1] for j in range(0, 4))
        k[i][2] = f[i](t + (4 / 33) * h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * ((1 / 22) * k[j][0] +
                                          (3 / 22) * k[j][2]) for j in range(0, 4))
        k[i][3] = f[i](t + (2 / 11) * h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * ((43 / 64) * k[j][0] +
                                          (-165 / 64) * k[j][2] +
                                          (77 / 32) * k[j][3]) for j in range(0, 4))
        k[i][4] = f[i](t + (1 / 2) * h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * ((-2383 / 486) * k[j][0] +
                                          (1067 / 54) * k[j][2] +
                                          (-26312 / 1701) * k[j][3] +
                                          (2176 / 1701) * k[j][4]) for j in range(0, 4))
        k[i][5] = f[i](t + (2 / 3) * h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * ((10077 / 4802) * k[j][0] +
                                          (-5643 / 686) * k[j][2] +
                                          (116259 / 16807) * k[j][3] +
                                          (-6240 / 16807) * k[j][4] +
                                          (1053 / 2401) * k[j][5]) for j in range(0, 4))
        k[i][6] = f[i](t + (6 / 7) * h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * ((-733 / 176) * k[j][0] +
                                          (141 / 8) * k[j][2] +
                                          (-335763 / 23296) * k[j][3] +
                                          (216 / 77) * k[j][4] +
                                          (-4617 / 2816) * k[j][5] +
                                          (7203 / 9152) * k[j][6]) for j in range(0, 4))
        k[i][7] = f[i](t + h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * ((15 / 352) * k[j][0] +
                                          (-5445 / 46592) * k[j][3] +
                                          (18 / 77) * k[j][4] +
                                          (-1215 / 5632) * k[j][5] +
                                          (1029 / 18304) * k[j][6]) for j in range(0, 4))
        k[i][8] = f[i](t, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * ((-1833 / 352) * k[j][0] +
                                          (141 / 8) * k[j][2] +
                                          (-51237 / 3584) * k[j][3] +
                                          (18 / 7) * k[j][4] +
                                          (-729 / 512) * k[j][5] +
                                          (1029 / 1408) * k[j][6] +
                                          1 * k[j][8]) for j in range(0, 4))
        k[i][9] = f[i](t + h, *temp_var)

    errx, erry, errdx, errdy = ((11 / 270) * h * (ks[0] + ks[7] - ks[8] - ks[9]) for ks in k)
    error = (errx ** 2 + erry ** 2 + errdx ** 2 + errdy ** 2) ** (1 / 2)

    x_next = x_prev + h * ((77 / 1440) * kx[0] +
                           (1771561 / 6289920) * kx[3] +
                           (32 / 105) * kx[4] +
                           (243 / 2560) * kx[5] +
                           (16807 / 74880) * kx[6] +
                           (11 / 270) * kx[7])

    y_next = y_prev + h * ((77 / 1440) * ky[0] +
                           (1771561 / 6289920) * ky[3] +
                           (32 / 105) * ky[4] +
                           (243 / 2560) * ky[5] +
                           (16807 / 74880) * ky[6] +
                           (11 / 270) * ky[7])

    dx_next = dx_prev + h * ((77 / 1440) * kdx[0] +
                             (1771561 / 6289920) * kdx[3] +
                             (32 / 105) * kdx[4] +
                             (243 / 2560) * kdx[5] +
                             (16807 / 74880) * kdx[6] +
                             (11 / 270) * kdx[7])

    dy_next = dy_prev + h * ((77 / 1440) * kdy[0] +
                             (1771561 / 6289920) * kdy[3] +
                             (32 / 105) * kdy[4] +
                             (243 / 2560) * kdy[5] +
                             (16807 / 74880) * kdy[6] +
                             (11 / 270) * kdy[7])

    x1_next = x_prev + h * ((11 / 864) * kx[0] +
                            (1771561 / 6289920) * kx[3] +
                            (32 / 105) * kx[4] +
                            (243 / 2560) * kx[5] +
                            (16807 / 74880) * kx[6] +
                            (11 / 270) * kx[8] +
                            (11 / 270) * kx[9])

    y1_next = y_prev + h * ((11 / 864) * ky[0] +
                            (1771561 / 6289920) * ky[3] +
                            (32 / 105) * ky[4] +
                            (243 / 2560) * ky[5] +
                            (16807 / 74880) * ky[6] +
                            (11 / 270) * ky[8] +
                            (11 / 270) * ky[9])

    dx1_next = dx_prev + h * ((11 / 864) * kdx[0] +
                              (1771561 / 6289920) * kdx[3] +
                              (32 / 105) * kdx[4] +
                              (243 / 2560) * kdx[5] +
                              (16807 / 74880) * kdx[6] +
                              (11 / 270) * kdx[8] +
                              (11 / 270) * kdx[9])

    dy1_next = dy_prev + h * ((11 / 864) * kdy[0] +
                              (1771561 / 6289920) * kdy[3] +
                              (32 / 105) * kdy[4] +
                              (243 / 2560) * kdy[5] +
                              (16807 / 74880) * kdy[6] +
                              (11 / 270) * kdy[8] +
                              (11 / 270) * kdy[9])

    # return x1_next, dx1_next, y1_next, dy1_next, error
    return x_next, dx_next, y_next, dy_next, error


def DoPriRK54(t, x_prev, y_prev, dx_prev, dy_prev, h, fdx, fdy):
    fx = lambda t, x, y, dx, dy: dx
    fy = lambda t, x, y, dx, dy: dy

    kx = dict()
    ky = dict()
    kdx = dict()
    kdy = dict()

    values = (x_prev, y_prev, dx_prev, dy_prev)

    k = [kx, ky, kdx, kdy]
    f = [fx, fy, fdx, fdy]

    for i in range(0, 4):
        k[i][0] = f[i](t, *values)

    for i in range(0, 4):
        temp_var = tuple(values[j] +
                         h * (1 / 5) * k[j][0] for j in range(0, 4))
        k[i][1] = f[i](t + (1 / 5) * h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] +
                         h * ((3 / 40) * k[j][0] +
                              (9 / 40) * k[j][1]) for j in range(0, 4))
        k[i][2] = f[i](t + (3 / 10) * h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] +
                         h * ((44 / 45) * k[j][0] +
                              (-56 / 15) * k[j][1] +
                              (32 / 9) * k[j][2]) for j in range(0, 4))
        k[i][3] = f[i](t + (4 / 5) * h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] +
                         h * ((19372 / 6561) * k[j][0] +
                              (-25360 / 2187) * k[j][1] +
                              (64448 / 6561) * k[j][2] +
                              (-212 / 729) * k[j][3]) for j in range(0, 4))
        k[i][4] = f[i](t + (8 / 9) * h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] +
                         h * ((9017 / 3168) * k[j][0] +
                              (-355 / 33) * k[j][1] +
                              (46732 / 5247) * k[j][2] +
                              (49 / 176) * k[j][3] +
                              (-5103 / 18656) * k[j][4]) for j in range(0, 4))
        k[i][5] = f[i](t + h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] +
                         h * ((35 / 384) * k[j][0] +
                              (500 / 1113) * k[j][2] +
                              (125 / 192) * k[j][3] +
                              (-2187 / 6784) * k[j][4] +
                              (11 / 84) * k[j][5]) for j in range(0, 4))
        k[i][6] = f[i](t + h, *temp_var)

    x_next, y_next, dx_next, \
    dy_next = (values[i] +
               h * ((35 / 384) * k[i][0] +
                    (500 / 1113) * k[i][2] +
                    (125 / 192) * k[i][3] +
                    (-2187 / 6784) * k[i][4] +
                    (11 / 84) * k[i][5]) for i in range(4))

    x1_next, y1_next, dx1_next, \
    dy1_next = (values[i] +
                h * ((5179 / 57600) * k[i][0] +
                     (7571 / 16695) * k[i][2] +
                     (393 / 640) * k[i][3] +
                     (-92097 / 339200) * k[i][4] +
                     (187 / 2100) * k[i][5] +
                     (1 / 40) * k[i][6]) for i in range(4))

    errx, erry, errdx, \
    errdy = (h * ((35 / 384 - 5179 / 57600) * k[i][0] +
                  (500 / 1113 - 7571 / 16695) * k[i][2] +
                  (125 / 192 - 393 / 640) * k[i][3] +
                  (-2187 / 6784 + 92097 / 339200) * k[i][4] +
                  (11 / 84 - 187 / 2100) * k[i][5] +
                  (-1 / 40) * k[i][6]) for i in range(4))

    error = (errx ** 2 + erry ** 2 + errdx ** 2 + errdy ** 2) ** (1 / 2)
    return x_next, dx_next, y_next, dy_next, error


def FehlbergRK45(t, x_prev, y_prev, dx_prev, dy_prev, h, fdx, fdy,
                 fx=lambda t, x, y, dx, dy: dx,
                 fy=lambda t, x, y, dx, dy: dy):
    kx = dict()
    ky = dict()
    kdx = dict()
    kdy = dict()

    values = (x_prev, y_prev, dx_prev, dy_prev)

    k = [kx, ky, kdx, kdy]
    f = [fx, fy, fdx, fdy]

    for i in range(0, 4):
        k[i][0] = f[i](t, *values)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * (1 / 4) * k[j][0] for j in range(0, 4))
        k[i][1] = f[i](t + (1 / 4) * h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * ((3 / 32) * k[j][0] +
                                          (9 / 32) * k[j][1]) for j in range(0, 4))
        k[i][2] = f[i](t + (3 / 8) * h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * ((1932 / 2197) * k[j][0] +
                                          (-7200 / 2197) * k[j][1] +
                                          (7296 / 2197) * k[j][2]) for j in range(0, 4))
        k[i][3] = f[i](t + (12 / 13) * h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * ((439 / 216) * k[j][0] +
                                          (-8) * k[j][1] +
                                          (3680 / 513) * k[j][2] +
                                          (-845 / 4104) * k[j][3]) for j in range(0, 4))
        k[i][4] = f[i](t + 1 * h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * ((-8 / 27) * k[j][0] +
                                          2 * k[j][1] +
                                          (-3544 / 2565) * k[j][2] +
                                          (1859 / 4104) * k[j][3] +
                                          (-11 / 40) * k[j][4]) for j in range(0, 4))
        k[i][5] = f[i](t + (1 / 2) * h, *temp_var)

    x_next, y_next, dx_next, dy_next = (values[i] + h * ((25 / 216) * k[i][0] +
                                                         (1408 / 2565) * k[i][2] +
                                                         (2197 / 4104) * k[i][3] +
                                                         (-1 / 5) * k[i][4]) for i in range(4))

    x1_next, y1_next, dx1_next, dy1_next = (values[i] + h * ((16 / 135) * k[i][0] +
                                                             (6656 / 12825) * k[i][2] +
                                                             (28561 / 56430) * k[i][3] +
                                                             (-9 / 50) * k[i][4] +
                                                             (2 / 55) * k[i][5]) for i in range(4))

    errx, erry, errdx, errdy = (h * ((25 / 216 - 16 / 135) * k[i][0] +
                                     (1408 / 2565 - 6656 / 12825) * k[i][2] +
                                     (2197 / 4104 - 28561 / 56430) * k[i][3] +
                                     (-1 / 5 + 9 / 50) * k[i][4] +
                                     (-2 / 55) * k[i][5]) for i in range(4))

    error = (errx ** 2 + erry ** 2 + errdx ** 2 + errdy ** 2) ** (1 / 2)

    # return x1_next, dx1_next, y1_next, dy1_next, error
    return x_next, dx_next, y_next, dy_next, error


def DoPriRK65(t, x_prev, y_prev, dx_prev, dy_prev, h, fdx, fdy):
    fx = lambda t, x, y, dx, dy: dx
    fy = lambda t, x, y, dx, dy: dy

    kx = dict()
    ky = dict()
    kdx = dict()
    kdy = dict()

    values = (x_prev, y_prev, dx_prev, dy_prev)

    k = [kx, ky, kdx, kdy]
    f = [fx, fy, fdx, fdy]

    for i in range(0, 4):
        k[i][0] = f[i](t, *values)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * (1 / 10) * k[j][0] for j in range(0, 4))
        k[i][1] = f[i](t + (1 / 10) * h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * ((-2 / 81) * k[j][0] + (20 / 81) * k[j][1]) for j in range(0, 4))
        k[i][2] = f[i](t + (2 / 9) * h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * ((615 / 1372) * k[j][0] +
                                          (-270 / 343) * k[j][1] +
                                          (1053 / 1372) * k[j][2]) for j in range(0, 4))
        k[i][3] = f[i](t + (3 / 7) * h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * ((3243 / 5500) * k[j][0] +
                                          (-54 / 55) * k[j][1] +
                                          (50949 / 71500) * k[j][2] +
                                          (4998 / 17875) * k[j][3]) for j in range(0, 4))
        k[i][4] = f[i](t + (3 / 5) * h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * ((-26492 / 37125) * k[j][0] +
                                          (72 / 55) * k[j][1] +
                                          (2808 / 23375) * k[j][2] +
                                          (-24206 / 37125) * k[j][3] +
                                          (338 / 459) * k[j][4]) for j in range(0, 4))
        k[i][5] = f[i](t + (4 / 5) * h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * ((5561 / 2376) * k[j][0] +
                                          (-35 / 11) * k[j][1] +
                                          (-24117 / 31603) * k[j][2] +
                                          (899983 / 200772) * k[j][3] +
                                          (-5225 / 1836) * k[j][4] +
                                          (3925 / 4056) * k[j][5]) for j in range(0, 4))
        k[i][6] = f[i](t + h, *temp_var)

    for i in range(0, 4):
        temp_var = tuple(values[j] + h * ((465467 / 266112) * k[j][0] +
                                          (-2945 / 1232) * k[j][1] +
                                          (-5610201 / 14158144) * k[j][2] +
                                          (10513573 / 3212352) * k[j][3] +
                                          (-424325 / 205632) * k[j][4] +
                                          (376225 / 454272) * k[j][5]) for j in range(0, 4))
        k[i][7] = f[i](t + h, *temp_var)

    x_next, y_next, dx_next, dy_next = (values[i] + h * ((821 / 10800) * k[i][0] +
                                                         (19683 / 71825) * k[i][2] +
                                                         (175273 / 912600) * k[i][3] +
                                                         (395 / 3672) * k[i][4] +
                                                         (785 / 2704) * k[i][5] +
                                                         (3 / 50) * k[i][6]) for i in range(4))

    x1_next, y1_next, dx1_next, dy1_next = (values[i] + h * ((61 / 864) * k[i][0] +
                                                             (98415 / 321776) * k[i][2] +
                                                             (16807 / 146016) * k[i][3] +
                                                             (1375 / 7344) * k[i][4] +
                                                             (1375 / 5408) * k[i][5] +
                                                             (-37 / 1120) * k[i][6] +
                                                             (1 / 10) * k[i][7]) for i in range(4))

    errx, erry, errdx, errdy = (h * ((821 / 10800 - 61 / 864) * k[i][0] +
                                     (19683 / 71825 - 98415 / 321776) * k[i][2] +
                                     (175273 / 912600 - 16807 / 146016) * k[i][3] +
                                     (395 / 3672 - 1375 / 7344) * k[i][4] +
                                     (785 / 2704 - 1375 / 5408) * k[i][5] +
                                     (3 / 50 + 37 / 1120) * k[i][6] +
                                     (-1 / 10) * k[i][7]) for i in range(4))

    error = (errx ** 2 + erry ** 2 + errdx ** 2 + errdy ** 2) ** (1 / 2)
    return x1_next, dx1_next, y1_next, dy1_next, error
