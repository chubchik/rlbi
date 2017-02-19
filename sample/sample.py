#-*- coding: utf-8 -*-
from rlbig.BioTree import Gobiidae
from rlbig.BioOptimization import findOptimumSearch

g = Gobiidae(optimization_runs=2**8)

print g.find(text='Babka')
print g.find(text='Babka',alg='findF')
print g.find(text='Babka',type='Genus')
print g.find(text='Babka',alg='findF',type='Genus')