# freeCodeCamp - Data Analysis with Python Project
# https://www.linkedin.com/in/vasilis-timoudas
# https://github.com/vasilis-timoudas

import numpy as np

def calculate(list):
  if len(list) < 9:
    raise "List must contain nine numbers."

  a = np.array(list)
  a = a.reshape(3, 3)

  calculations = {
    'mean': [np.mean(a, axis=0).tolist(), np.mean(a, axis=1).tolist(), np.mean(a.flatten()).tolist()],
    'variance': [np.var(a, axis=0).tolist(), np.var(a, axis=1).tolist(), np.var(a.flatten()).tolist()],
    'standard deviation': [np.std(a, axis=0).tolist(), np.std(a, axis=1).tolist(), np.std(a.flatten()).tolist()],
    'max': [np.max(a, axis=0).tolist(), np.max(a, axis=1).tolist(), np.max(a.flatten()).tolist()],
    'min': [np.min(a, axis=0).tolist(), np.min(a, axis=1).tolist(), np.min(a.flatten()).tolist()],
    'sum': [np.sum(a, axis=0).tolist(), np.sum(a, axis=1).tolist(), np.sum(a.flatten()).tolist()]
  }

  return calculations
    
