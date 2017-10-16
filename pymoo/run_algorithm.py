import os

import numpy as np

from algorithms.nsao import NSAO
from algorithms.nsga import NSGA
from operators.polynomial_mutation import PolynomialMutation
from problems.zdt import ZDT1
from rand.my_random_generator import MyRandomGenerator
from util.misc import get_f


def write_final_pop_obj(pop, run):
    f_name = os.path.join('results', problem.__class__.__name__ + '_RUN' + str(run) + str('.out'))
    f = open(f_name, 'w')
    for ind in pop:
        f.write('%f \t %f\n' % (ind.f[0], ind.f[1]))
    f.close()


if __name__ == '__main__':
    problem = ZDT1(n_var=5)
    print(problem)

    x, f, g = NSGA().solve(problem, evaluator=10000, return_only_non_dominated=True)

    print("DONE")
