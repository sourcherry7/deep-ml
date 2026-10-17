def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	if not a or not b:
		return -1
	elif len(a) != len(b):
		return -1
	else:
		return [a[k] + b[k] for k in range(len(a))]