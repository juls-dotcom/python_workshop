import numpy as np
a = np.arange(25).reshape((5, 5))
b = np.arange(75).reshape((5, 5, 3))

(a[:, :, None] + b)[::2, -1]
