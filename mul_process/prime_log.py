from math import sqrt
from timeit import default_timer as timer
import concurrent.futures
def is_prime(x):
  if x < 2:
    return False

  if x == 2:
    return True

  if x % 2 == 0:
    return False

  limit = int(sqrt(x)) + 1
  for i in range(3, limit, 2):
    if x % i == 0:
      return False

  return True

if __name__ == "__main__":
  """
  for i in range(2,30):
    if is_prime(i):
      print(i, end=", ")
  """

  input = [ i for i in range( 10 ** 13, 10 ** 13 + 5000000)]
  #start = timer()
  #result = [ i for i in input if is_prime(i)]
  #print("it took {:.2f} sec.".format(timer() - start))

  # concurrent
  start = timer()
  result = []
  with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(is_prime, i) for i in input]
    for i, future in enumerate(concurrent.futures.as_completed(futures)):
      if future.result():
        result.append(input[i])

  print('Result 2:', result)
  print('Took: {:.2f} seconds.'.format(timer() - start))
# 8 process: 10 s, 1 process : 35 s, 4 processes: 12.3 s


