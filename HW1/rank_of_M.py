
# Compute rank of a matrix

import numpy as np

M = np.matrix([[2,4,5],[2,6,1],[-2,9,15],[12,0,15],[3,34,-52]])

rank_of_M = np.linalg.matrix_rank(M)

print rank_of_M
