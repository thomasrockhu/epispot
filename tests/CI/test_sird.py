import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
repodir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(0, repodir)

import epispot as epi


def R_0(t):
    return 5 * 2.718 ** ((- 1 / 200) * (t - 30) ** 2)


def N(t):
    return 1e5 + 10 * t


def p_rec(t):
    return 1.0


def rec_rate(t):
    return 1 / 7


def alpha(t):
    return 2.718 ** ((- 1 / 15) * (t - 30) ** 2)


def rho(t):
    return 1 / 2


Model = epi.pre.SIRD(R_0, N, p_rec, rec_rate, alpha, rho)
epi.plots.plot_comp_nums(Model, range(0, 120))
print('Test complete: Build passing.')
