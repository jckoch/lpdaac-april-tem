range_end = 5


def gen():
    for i in range(range_end):
        print(f'yielding the value...')
        yield i


g = gen()
# g is a generator object
print(g)

# iterate through it twice
print(next(g))
print(next(g))

# consume the rest of it
for i in g:
    print(i)


g = (i for i in range(range_end))
# g is a generator expression
print(g)

# iterate through it twice
print(next(g))
print(next(g))

# consume the rest of it
for i in g:
    print(i)
