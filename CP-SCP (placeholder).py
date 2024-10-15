import math

from docplex.cp.model import CpoModel
from docplex.cp.model import *


def CPOptimizer_model(O, S, Q, L, h, r, q, d, n, f):    

    # simplified model that uses few variables
    solver = os.path.splitext(os.path.basename(__file__))[0]    
....