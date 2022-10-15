from itertools import permutations
a=permutations(list(input()))
for i in a:
    print(*i,sep='')