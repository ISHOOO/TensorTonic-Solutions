import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    res=[]
    for i in range(len(A[0])):
        res.append([])        
        for j in range(len(A)):
            res[i].append(A[j][i])
    return np.asarray(res)
            