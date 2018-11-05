M,N = [int(x) for x in input().split(',')]
seats = []
fans = set()
for i in range(M):
    s = input()
    r = [int(x) for x in s.split(',')]
    seats.append(r)
    for j in range(N):
        if seats[i][j]==1: fans.add((i,j))
    print(r)       

print('fans:')
cnt = 0
for f in fans:
    print(f,end=', ')
    cnt += 1
    if cnt % 8 == 0: print()
print()

groups = {}
g_id = 1
while len(fans) > 0:
    g_id += 1
    groups[g_id] = 0
    f = fans.pop()
    cur_group = [f]
    print("\ng_id-%d: "%g_id,end=' ')
    while len(cur_group) > 0: # DFS
        r,c = cur_group.pop()
        groups[g_id] += 1
        seats[r][c] = g_id
        print("[%d,%d]"%(r,c), end=', ')
        for i in range(r-1,r+2):
            for j in range(c-1,c+2):
                if i==r and j==c:
                    continue
                if i<0 or j<0 or i>=M or j>=N:
                    continue
                if seats[i][j] == 1:
                    fans.remove((i,j))
                    seats[i][j] = g_id
                    cur_group.append((i,j))
                    # print('(%d,%d)'%(i,j),end=', ')

print('updated array:')
for r in seats:
    for c in r:
        if c> 0:
            print(c-1,end=' ')
        else:
            print('.', end=' ')
    print()

# print('records:',groups)
print('%d,%d'%(len(groups),max(groups.values())))