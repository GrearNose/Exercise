def cnt_num_split(s):
    if None == s or 0 == len(s):
        return 0
    cnt = 0
    cur = ''
    for i in range(len(s)):
        cur += s[i]
        if int(cur) % 3 == 0:
            cnt += 1
            # print(cur)
            cur = ''
    return cnt

def test():
    s = '12345'
    # s = '321'
    print(cnt_num_split(s))

if __name__ == '__main__':
    test()
