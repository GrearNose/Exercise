import traceback

def mazeGo(maze):
    n,m = len(maze),len(maze[0])
    # print('n,m:',n,m)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    i = 0
    maze[0][0] = 'x'
    track = [(-1,0,0)]  # ix_prev, r,c
    cand = [(-1,0,0,0)] # ix_prev,ix_self, r, c
    dis = [n+m-2]
    ix_prev = 0
    found = False
    while i < n*m and not found:
        i += 1
        d_m = min(dis)
        ix = dis.index(d_m)
        _,ix_self,r0,c0 = cand[ix]
        ix_prev = ix_self # this node is prior to other nodes derived from it.
        # print(i,(r0,c0))
        # take out the current point from the candidates.
        del dis[ix]
        del cand[ix]
        for mv in moves:
            r,c = r0+mv[0], c0+mv[1]
            if 0<=r and  r<n and 0<=c and c<m and '0' == maze[r][c]:
                maze[r][c] = 'x'
                d = n-r-1 + m-c-1
                track.append((ix_prev,r,c)) # track down this node.
                # add to as a cadidate.
                dis.append(d)
                ix_cur = len(track)-1
                cand.append((ix_prev,ix_cur,r,c))
                if r == n-1 and c == m-1:
                    found = True
                    break
    # trace back the route.
    s = []
    ix = len(track)-1
    while True:
        p = tuple(track[ix][1:])
        s.append(p)
        if track[ix][0] == -1:
            break
        ix = track[ix][0]

    s = s[::-1]
    return s

try:
    while True:
        n,m = [int(x) for x in input().strip().split()]
        maze = []
        for _ in range(n):
            r = list(input().strip().split())
            maze.append(r)
        # print('maze:')
        # for r in maze:
        #     print(r)
        s = mazeGo(maze)
        # print('search track:')
        # for r in maze:
        #     print(r)        
        # print('route:')
        for p in s:
            print(p)
except EOFError:
    pass
except Exception as e:
    traceback.print_exc(e)