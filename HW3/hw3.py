import numpy as np
import math
import copy
from sympy import *

m_example = Matrix([[2, 4, 2], [5, 1, 3], [8, 6, 3]])

print("Example matrix: \n")
print(m_example)

def get_determinant(m):
	num_cols = m.shape[0] # extract number of columns
	det_list = [] # list for use later on

	# exit if too big
	if (num_cols > 10):
		return "Matrix too big"

	# if 2x2 then calculate determinant easily, otherwise recursive call
	if (num_cols == 2): 
		atimesd = m.row(0)[0] * m.row(1)[1] 
		btimesc = m.row(0)[1] * m.row(1)[0]
		return atimesd - btimesc
	else:
		# for each column
		for j in xrange(0, num_cols):
			new_matrix = copy.deepcopy(m)
			new_matrix.row_del(0) # make the matrix smaller
			new_matrix.col_del(j)

			multiple = math.pow(-1, j) * m.row(0)[j] # multiplier formula

			new_det = get_determinant(new_matrix) # get the determinant of the smaller matrix
			det_list.append(new_det * multiple) # add determinant to list

	return sum(det_list) # return final result

print("\nExample matrix determinant: ")
print(get_determinant(m_example))

print("\nExample triangle points: \n")
points_example = [(3, 4), (1, 7), (2, 1)] # example data
print(points_example)

# takes a list of tuples
def area_of_triangle(points):
	point1 = points[0] # extract the tuples
	point2 = points[1]
	point3 = points[2]

	# create the matrix
	triangle_matrix = Matrix([[point1[0], point1[1], 1],
							[point2[0], point2[1], 1],
							[point3[0], point3[1], 1]])

	return .5 * get_determinant(triangle_matrix) # compute result

print("\nExample triangle area, calculated with determinant method: ")
print(area_of_triangle(points_example))

problem11matrix = Matrix([[4,3,2],[1,2,6],[5,8,1]])

print("\nEigenvalues for problem 11 matrix: \n")
print(problem11matrix.eigenvals())

print("\nEigenvectors for problem 11 matrix: \n")
print(problem11matrix.eigenvects())
