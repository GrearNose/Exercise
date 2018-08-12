"""
Give a set of people, and the friendships of them, for a certain
person of them, figure out person who is the most likely his friend,
i.e. they are not friend but they share the most number of friends.
If there are more than one such person, give out the one with smallest
id.
"""

s = input()
num,hero = [int(x) for x in s.split()]
friends = []
for i in range(num):
    line = input().split()
    his_friends = [int(f) for f in line]
    friends.append(his_friends)

his_friends = friends[hero]
print('his_friends:', his_friends)

cnt = [0]*num
for f in his_friends:
    print('friends of %d:'%f, friends[f])
    for p in friends[f]:
        if p not in his_friends:
            cnt[p] += 1

likelihood = max(cnt)
if likelihood == 0:
    print(-1)

for i in range(num):
    if cnt[i] == likelihood and i != hero:
        print(i)
        break
