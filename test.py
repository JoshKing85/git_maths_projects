import numpy as np
from multiset import Multiset
set = [13, 13, np.nan, 0,]
s = Multiset(set)
new_s = {0}
super_set = s + new_s
print(s)
print(super_set.issubset(s))