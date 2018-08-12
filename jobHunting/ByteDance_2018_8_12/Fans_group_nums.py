M,N = [int(x) for x in input().split(',')]
fans,visited = [],[]
for i in range(M):
    r = [int(x) for x in input().split(',')]
    fans.append(r)
    visited.append([False]*N)
    print(r)

def gather_group(r,c):
    global fans
    global cnt_group
    if visited[r][c]: return False
    visited[r][c] = True
    if fans[r][c] == 0: return False
    fans[r][c] = g_id # set the group id.
    print('(%d,%d)'%(r,c),end=', ')
    if g_id not in cnt_group: # add to the group
        cnt_group[g_id] = 1
    else:
        cnt_group[g_id] += 1

    for i in range(r-1,r+2): # for all the neighboors.
        for j in range(c-1,c+2):
            if i<0 or j<0 or i>=M or j>=N or (i==r and j==c):
                continue
            gather_group(i,j)
    return True


g_id = 1
cnt_group = {}
for i in range(M):
    for j in range(N):
        if gather_group(i,j):
            g_id += 1
            print()
            found = True

print('grouped fans:')
for r in fans:
    for c in r:
        if c > 0:
            print(c,end=' ')
        else:
            print('.', end=' ')
    print()

print(cnt_group)
print(len(cnt_group),max(cnt_group.values()))
