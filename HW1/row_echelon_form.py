
# Get the row echelon form of a matrix M

import scipy as sp

M = sp.Matrix([[1,0,1,3], [2,3,4,7], [-1,-3,-3,-4]])

row_echelon_form_of_M = M.rref()

print row_echelon_form_of_M
