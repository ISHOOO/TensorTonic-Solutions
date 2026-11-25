import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # return 1/(1+np.exp(x))
    if isinstance(x,int):
        return 1/(1+np.exp(-x))
    if isinstance(x,list):
        res=-np.asarray(x, dtype= float)
        res=1/(1+np.exp(res))
        return res