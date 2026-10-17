import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here

    norms_1d = ['l1', 'l2', 'linf']
    norms_2d = ['frobenius']

    # if norm_type not in norms_1d or norm_type not in norms_2d:
    #     raise Exception('Use a valid norm.')
    if norm_type in norms_1d:
        if arr.ndim != 1:
            arr = np.ravel(arr)
        if norm_type == 'l1':
            return float(np.sum(np.abs(arr)))
        elif norm_type == 'l2':
            return float(np.sqrt(arr.dot(arr)))
        elif norm_type == 'linf':
            return float(np.max(np.abs(arr)))
    else:
        if arr.ndim != 2:
            raise ValueError('Use 2d vectors for Frobenius norm.')
        return float(np.linalg.norm(arr, 'fro'))

            
