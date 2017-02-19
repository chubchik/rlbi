import time

def _dminmax(algs,x):
    mn = min(x[:])
    mx = max(x[:])
    return {'min':mn,'min_number':algs[x.index(mn)],'max':mx,'max_number':algs[x.index(mx)]}


def _dred(x,y):
    x.append(y['min_number'])
    return x


def findOptimumSearch(obj, runs=2**6, algs=['find','find_linear','find_dict_linear','findO'], warmup=['flatten','flattenDict'], debug=False):
  faktor = 1
  start_number = 2
  number_loops = runs
  times = []
  counters = {}
  if len(warmup) > 0:
     for wu in warmup:
         try:
           wufunc = getattr(obj, wu)
           wufunc()
         except AttributeError:
           pass
  while start_number<=number_loops:
    subtimes = []
    for alg in algs:
       if alg!='':
          start = time.time() 
          try:
            func = getattr(obj, alg)
            for i in range(0,start_number):
                tmp = func('Kessler')
          except AttributeError:
            pass
          end = time.time()
          ft = (float(end - start)*faktor)
          subtimes.append(ft)
    start_number = start_number*2
    times.append(subtimes)

  metrics = map(lambda x: _dminmax(algs,x),times)
  reduced_metrics = reduce(lambda x,y: _dred(x,y),metrics,[])
  for line in reduced_metrics:
      if line not in counters:
         counters[line]=1
      else:
         counters[line]+=1
  optimum = sorted(counters, key=counters.__getitem__,reverse=True)[0]
  if debug:
     print times, reduced_metrics, counters, optimum
  return optimum