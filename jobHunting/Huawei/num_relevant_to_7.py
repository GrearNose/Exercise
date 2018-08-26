import traceback
try:
    while True:
        n = int(input())
        cnt = 0
        for i in range(7,n+1):
            if 0 == i%7 or '7' in '%d'%i:
                cnt += 1
        print(cnt)
except EOFError:
    pass
except Exception as e:
    traceback.print_exc(e)