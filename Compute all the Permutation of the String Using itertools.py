from itertools import permutations

words = [''.join(p) for p in permutations('pro')]

print(words)
