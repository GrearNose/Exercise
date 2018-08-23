try:
    rd = {}
    keys = []
    cnt = 0
    while True:
        cnt += 1
        print(cnt)
        fn,line = input().split()
        fn = fn.split('\\')[-1]
        fn = fn[-16:]
        itm = (fn,line)
        # print(fn)
        # print(line)
        print('got', itm)
        if itm in rd:
            rd[itm] += 1
        else:
            if len(keys) == 8:
                print('remove',keys[0])
                for f,l in keys:print(f,l)
                rd.pop(keys[0])
                keys = keys[1:]
            rd[itm] = 1
            keys.append(itm)
            print('insert',itm)
            for f,l in keys:print(f,l)
        # print(len(rd),len(keys))
        # if len(keys) == 8:
        #     break
except Exception:
    pass
finally:
    for k in keys:
        print(k[0],k[1],rd[k])
    #     # print(k,v)
    #     print(k)
    #     # print(v)
    # print(rd)