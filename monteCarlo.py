#Algoritmo de Monte Carlo
#Estudante: Nicolas Luis Kaiser

import numpy as np
import random as rd
import time

print('CALCULO PI -> MONTE CARLO \nA seguir sera representado o calculo do PI atraves do algoritmo de Monte Carlo')

def monteCarlo(N):
  i = 0
  j = 0

  rd.seed(time.time())

  for i in range (N):
    x = rd.uniform(0,1)
    y = rd.uniform(0,1)
    
    d_aux = (x-0.5)*(x-0.5) + (y-0.5)*(y-0.5)
    d = np.sqrt(d_aux)

    if(d<0.5):
      j = j + 1
    else:
      continue

  pi = 4 * (float(j)/float(N))
  return pi

print('PI[100]=',monteCarlo(100))
print('PI[1000]=',monteCarlo(1000))
print('PI[10000]=',monteCarlo(100000))
print('PI[100000]=',monteCarlo(1000000))