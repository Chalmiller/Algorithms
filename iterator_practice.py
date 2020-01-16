iterator = [1,2,3,4,5,6,7,8]
iterable_iterator = iter(iterator)

for i in iterable_iterator:
    print(i)
    print(next(iterable_iterator))

