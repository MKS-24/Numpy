

# %timeit [j**99 for j in range(1,9)]
# 5.29 µs ± 182 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)


# import numpy as np  
# %timeit np.arange(1,9)**99
# 3.88 µs ± 69.2 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)


# numpy is faster then list in big calculation otherwise list is faster then numpy array in small calculation