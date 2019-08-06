from collections import OrderedDict
from pprint import pprint

plain = {'a': 1, 'b': 2, 'c': 3}

fancy = OrderedDict(plain)
pprint(fancy)

# OrderedDict([('a', 1), ('b', 2), ('c', 3)])
