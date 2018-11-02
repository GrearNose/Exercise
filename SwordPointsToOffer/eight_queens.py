from itertools import permutations,combinations
ids = list(range(8))
cnt = 0
for p in permutations(ids,len(ids)):
    valid = True
    for i,j in combinations(ids,2):
        if abs(i-j) == abs(p[i]-p[j]):
            valid = False
            break
    if valid:
        cnt += 1
        print(cnt)
        for ix in p:
            for i in range(len(p)):
                if i != ix:
                    print('.',end=' ')
                else:
                    print('*',end=' ')
            print()