n = int(input())
A = [int(x) for x in input().split()]
m = int(input())
q = [int(x) for x in input().split()]


# print('n,A,m,q')
# for x in [n,A,m,q]: print(x)

acc = []
s = 0
for x in A:
    s += x
    acc.append(s)

for a in q:
    if a < 0 or a > acc[-1]:
        print(1)
        continue

    l,h = 0,n-1
    while l <= h:
        mid = (l+h)//2

        if acc[mid-1] < a and a <= acc[mid]:
            print(mid+1)
            break

        elif mid > 0 and a < acc[mid-1]:
            h = mid-1

        elif acc[mid] < a and mid < n:
            l = mid +1
