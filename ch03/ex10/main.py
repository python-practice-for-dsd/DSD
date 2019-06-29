# 3-10
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print(e2f)

# 3-11
print(e2f.get('walrus'))

# 3-12
f2e = {v: k for k, v in e2f.items()}
print(f2e)

# 3-13
print(f2e.get('chien'))

# 3-14
print(set(e2f.keys()))
