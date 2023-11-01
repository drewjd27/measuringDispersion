import numpy as np
import pandas as pd

jlh_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
# HITUNG RANGE
range = jlh_kucing.max() - jlh_kucing.min()
print(range)

# HITUNG INTERQUARTILE RANGE
iqr = np.percentile(jlh_kucing, 75) - np.percentile(jlh_kucing, 25)
print(iqr)

# HITUNG VARIANCE
jlh_kucing_series = pd.Series(jlh_kucing)
print(jlh_kucing_series.var())

# HITUNG STANDAR DEVIASI
print(jlh_kucing_series.std())