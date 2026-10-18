def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here

	# Using nested list comprehension:
	# return [[scalar * val for val in row] for row in matrix]
	
	# Using 2 for loops:
	for row in matrix:
			for j in range(len(row)):
				row[j] *= scalar
	return matrix
