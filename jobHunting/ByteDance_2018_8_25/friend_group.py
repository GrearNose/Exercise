n = int(input())
friends = [[]]
# print('friends list:')
for i in range(n):
    f = [int(x) for x in input().split()[:-1]]
    friends.append(f)
    # print(i+1,f)
# for i in range(1,n+1):
#     for f in friends[i]:
#         friends[f].append(i)

visited = [True] + [False]*n
cnt,cnt_g = 0,0
while cnt < n:
    ix = visited.index(False)
    visited[ix]= True
    stack = [ix]
    group = set([ix])
    is_new_g = True
    while len(stack) > 0:
        p = stack.pop()
        cnt += 1
        for f in friends[p]:
            if not visited[f]:
                stack.append(f)
                group.add(f)
                visited[f] = True
            elif f not in group:
                is_new_g = False
    if is_new_g:
        cnt_g += 1
    # print('group:', cnt_g, group)

print(cnt_g)

