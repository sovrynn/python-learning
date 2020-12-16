from random import randint

# randint() takes two arguments, the start and end of random interval
# Values are generated in the range [start (inclusive) - end (inclusive)]
for _ in range(10):
    value = randint(0, 5)
    print(value)
