try:
    while True:
        pwd = input()
        # print(pwd)
        if len(pwd)<=8:
            # print('short')
            print('NG')
            continue
        s = {}
        for c in pwd:
            if str.islower(c):
                s['lower'] = 1
            elif str.isupper(c):
                s['upper'] = 1
            elif str.isnumeric(c):
                s['num'] = 1
            else:
                s['other'] = 1
            # print(c,s)
        if sum(s.values()) < 3:
            # print("too simple")
            print('NG')
            continue
        for i in range(len(pwd)-1):
            for ln in range(3,len(pwd[i+1:])):
                if pwd[i:i+ln] in pwd[i+1:]:
                    # print('repeat:', pwd[i:i+2])
                    print('NG')
                    continue
        print('OK')
        # break
except Exception:
    pass