from .core import np
from itertools import count


def grad_vec(grad_logp, x):
    """ grad_logp should be a list of gradient logps, respective to each
        paramter in x
    """
    try:
        grads = np.array([each(*x) for each in grad_logp])
        return grads
    except TypeError:  # Happens when grad_logp isn't iterable
        grad_logp = [grad_logp]
        return grad_vec(grad_logp, x)
