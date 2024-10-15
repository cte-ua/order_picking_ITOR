

import os
from docplex.mp.model import Model

def CPLEX_model(O, S, Q, L, h, n, f):
    solver = os.path.splitext(os.path.basename(__file__))[0]
    model = Model(name=solver)
...