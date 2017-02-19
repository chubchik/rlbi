

def memoize(function):
  '''
  memoize decorator for caching some function calls
  '''
  memo = {}
  def wrapper(*args):
    if args in memo:
      return memo[args]
    else:
      rv = function(*args)
      memo[args] = rv
      return rv
  return wrapper