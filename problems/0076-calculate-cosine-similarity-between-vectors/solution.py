import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	scale = np.linalg.norm(v1, 2) * np.linalg.norm(v2, 2)
	vec_product = np.vdot(v1, v2)
	return  float(vec_product / scale)