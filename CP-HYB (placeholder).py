import math

from docplex.cp.model import CpoModel
from docplex.cp.model import *

def CPOptimizer_model(O, S, Q, L, h, r, q, d, n, f):  
    
    solver = os.path.splitext(os.path.basename(__file__))[0]    
    model = CpoModel(name = solver)
    
    d_max = math.ceil(max(d.loc[s] for s in S))    
    n_max = math.ceil(max(n.loc[l] for l in L))
    h_max = math.ceil(max(2 * h.loc[l] for l in L))
    l_max = len(L)
    hh = [2 * h.loc[l] for l in L]
    
	... remaing

    return model
    
  
  