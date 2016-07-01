
# Compute (AB)T

import numpy as np

A = np.matrix([[2,4,5],[2,6,1],[-2,9,15],[12,0,15],[3,34,-52]])

B = np.matrix([[2,4,5,4], [2,6,1,4], [-2,9,15,4]])

C = A*B

print C.transpose()
