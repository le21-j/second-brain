import numpy as np


c = np.float64(3 * 10**8)                                    # propagation velocity in the free space [m/s]
h_BS = np.float64(3.5)                                       # antenna height of the base station [m]
h_UT = np.float64(3.5)                                       # antenna height of the user terminal [m]
h_E = np.float64(1)                                          # effective environment height [m]
h_prime_BS = h_BS - h_E                                      # effective antenna height of the base station [m]
h_prime_UT = h_UT - h_E                                      # effective antenna height of the user terminal [m]


def get_distance2D(p1: tuple[np.float64, np.float64, np.float64], p2: tuple[np.float64, np.float64, np.float64]):
    d = np.sqrt(np.power(p1[0] - p2[0], 2) + np.power(p1[1] - p2[1], 2))
    return d


def get_distance3D(p1: tuple[np.float64, np.float64, np.float64], p2: tuple[np.float64, np.float64, np.float64]):
    d = np.sqrt(np.power(p1[0] - p2[0], 2) + np.power(p1[1] - p2[1], 2) + np.power(p1[2] - p2[2], 2))
    return d


def get_PL_LOS(p1: tuple[np.float64, np.float64, np.float64], p2: tuple[np.float64, np.float64, np.float64], f_c: np.float64):
    d_2D = get_distance2D(p1, p2)
    d_3D = get_distance3D(p1, p2)
    d_BP = (np.float64(4) * h_prime_BS * h_prime_UT * f_c) / c
    if (d_2D < 10):
        if (d_3D >= 1) and (d_3D <= 150):
            PL_LOS = np.float64(32.4) + np.float64(17.3)*np.log10(d_3D) + np.float64(20)*np.log10(f_c * 10**(-9))
    else:
        if (d_2D >= 10) and (d_2D <= d_BP):
            PL_LOS = np.float64(32.4) + np.float64(21)*np.log10(d_3D) + np.float64(20)*np.log10(f_c * 10**(-9))
        elif (d_2D >= d_BP) and (d_2D <= 5 * 10**3):
            PL_LOS = np.float64(32.4) + np.float64(40)*np.log10(d_3D) + np.float64(20)*np.log10(f_c * 10**(-9)) - np.float64(9.5)*np.log10(np.power(d_BP, 2) + np.power(p1[2] - p2[2], 2))
    return PL_LOS


def get_PL_NLOS(p1: tuple[np.float64, np.float64, np.float64], p2: tuple[np.float64, np.float64, np.float64], f_c: np.float64):
    d_2D = get_distance2D(p1, p2)
    d_3D = get_distance3D(p1, p2)
    if (d_2D < 10):
        if (d_3D >= 1) and (d_3D <= 150):
            PL_prime_NLOS = np.float64(17.3) + np.float64(38.3)*np.log10(d_3D) + np.float64(24.9)*np.log10(f_c * 10**(-9))
    else:
        if (d_2D >= 10) and (d_2D <= 5 * 10**3):
            PL_prime_NLOS = np.float64(22.4) + np.float64(35.3)*np.log10(d_3D) + np.float64(21.3)*np.log10(f_c * 10**(-9)) - np.float64(0.3)*(p2[2] - np.float64(1.5))
    PL_NLOS = max(get_PL_LOS(p1, p2, f_c), PL_prime_NLOS)
    return PL_NLOS


def get_Pr(p1: tuple[np.float64, np.float64, np.float64], p2: tuple[np.float64, np.float64, np.float64]):
    d_2D = get_distance2D(p1, p2)
    if (d_2D < 10):
        if (d_2D <= 1.2):
            pr_LOS = np.float64(1)
        elif (d_2D > 1.2) and (d_2D < 6.5):
            pr_LOS = np.exp(-(d_2D - np.float64(1.2))/np.float64(4.7))
        elif (d_2D >= 6.5):
            pr_LOS = np.exp(-(d_2D - np.float64(6.5))/np.float64(32.6)) * np.float64(0.32)
    else:
        if d_2D <= 18:
            pr_LOS = np.float64(1)
        elif d_2D > 18:
            pr_LOS = (np.float64(18)/d_2D) + (np.exp(-d_2D/np.float64(36)) * (np.float64(1) - (np.float64(18)/d_2D)))
    return pr_LOS


def get_PL(p1: tuple[np.float64, np.float64, np.float64], p2: tuple[np.float64, np.float64, np.float64], f_c: np.float64):
    PL = get_Pr(p1, p2) * get_PL_LOS(p1, p2, f_c) + (np.float64(1) - get_Pr(p1, p2)) * get_PL_NLOS(p1, p2, f_c)
    return PL


def get_channel_gain(p1: tuple[np.float64, np.float64, np.float64], p2: tuple[np.float64, np.float64, np.float64], f_c: np.float64):
    g = np.float64(1) / np.power(np.float64(10), get_PL(p1, p2, f_c) / np.float64(10))
    return g
