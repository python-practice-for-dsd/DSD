from collections import defaultdict

dict_of_lists = defaultdict(list)

dict_of_lists['a'].append('somethis for a')

print(dict_of_lists['a'])

# ['somethis for a']
