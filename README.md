# rlbig - RL (Richelieu Lyceum) Bioinformatics Group
Biological qualifier for the Gobiidae family


# Example how to execute
from rlbig.BioTree import Gobiidae
from rlbig.BioOptimization import findOptimumSearch

g = Gobiidae(optimization_runs=2**8)

print g.find(text='Babka')
print g.find(text='Babka',alg='findF')
print g.find(text='Babka',type='Genus')
n = g.find(text='brauneri',alg='findF',type='Species')

print n[0].head.spots