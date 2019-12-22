from collections import namedtuple
from itertools import starmap

data = (("assigned", 10), ("open", 20), ("closed", 30))
nt = namedtuple("Indicators", "name value")
Indicators_Data = starmap(nt, data)

