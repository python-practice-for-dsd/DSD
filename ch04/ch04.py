# 4-1
guess_me = 7
if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')

# 4-2
guess_me = 7
start = 1
while True:
    if guess_me > start:
        print('too low')
    elif guess_me == start:
        print('found it!')
        break
    else:
        print('oops')
        break
    start += 1

# 4-3

# testList = list()
# for i in range(0, 4):
#     testList.append(i)

# for i in testList:
#     print(i)
testList = [print(i) for i in range(0, 4)]
# for i in testList:
#     print(i)

# 4-4
testList = [i for i in range(10) if i % 2 == 0]
print(testList)

# 4-5
squares = {i: i*i for i in range(10)}
print(squares)
# squares = dict()
# for i in range(10):
#     squares[i] = i*i
# print(squares)

# 4-6
# odd = set()
# for i in range(10):
#     if i % 2 != 0:
#         odd.add(i)
# print(odd)
odd = {i for i in range(10) if i % 2 != 0}
print(odd)

# 4-7


# 4-8
def good():
    return ['Harry', 'Ron', 'Hermione']


print(good())

# 4-9
for thing in ({'Got %s' % number} for number in range(10)):
    print(thing)


# def gene():
#     for number in range(10):
#         yield 'Got %s' % number


# print(type(gene()))
# for thing in gene():
#     print(thing)

# 4-10
def decoratar(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, ** kwargs)
        print('end')
        return result
    return new_func


@decoratar
def add(a, b):
    print(a+b)
    return a + b


add(1, 2)
# new_func = decoratar(add)
# print(type(new_func))
# print(new_func)
# # <function decoratar.<locals>.new_func at 0x10e3ff158>
# new_func(1, 2)


# 4-11
class OopsException(Exception):
    pass


try:
    raise OopsException()
except OopsException:
    print('Caught an oops')

# 4-12
titles = ['Creature of Habit', 'Crewel Fate']
plots = [' A num turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
# print(zip(titles, plots))
print(movies)
print(list(zip(titles, plots)))
