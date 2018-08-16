"""
Problem description
John is attending a lesson. He will attains different gain at each period of
time, while he sleeps within some periods of time, and can be waked up ONE time
to keep awake for the next k periods of time. Figure out when to wake he up
to maximum the total gains of the lesson.

Input
1st line: two integers, n and k, indicating the number of periods of the lesson
    and the number of period of time John will keep awake after being waked up.
2nd line: n integers, the gains at eaech period of time.
3rd line: n integers of 0s and 1s, 0 means sleeping and 1 means awake.

Output
one integer, the max total gains John can attain.
"""



n,k = [int(x) for x in input().split()]
gains = [int(x) for x in input().split()]
awake = [int(x) for x in input().split()]
# print('n,k',n,k)
# print('gains:', gains)
# print('awake:', awake)

extra_gain = 0
base_gain  = 0

for j in range(k):
    if 0 == awake[j]:
        extra_gain += gains[j]
    else:
        base_gain += gains[j]
mx_gain = extra_gain
ix_wake = 0
# print('extra, base:',extra_gain,base_gain)
for i in range(1,n-k+1):
    if 0 == awake[i-1]:
        extra_gain -= gains[i-1]
    if 0 == awake[k+i-1]:
        extra_gain += gains[k+i-1]
    else:
        base_gain += gains[k+i-1]
    if extra_gain > mx_gain:
        mx_gain = extra_gain
        ix_wake = i
    # print('extra, base:',extra_gain,base_gain)

print(base_gain+mx_gain)

