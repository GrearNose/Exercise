import traceback
from collections import Counter

def sort_by_occurance(s,debug=False):
    cnt = Counter(s)
    if debug:  print(cnt)
    mx = -1
    s,cur = '',''
    while len(cnt.keys())>0:
        k,v = cnt.most_common(1)[0]
        if cnt[k] != mx:
            cur = sorted(list(cur))
            s += ''.join(cur)
            mx = v
            cur = k
        else:
            cur += k
        cnt.pop(k)
    cur = sorted(list(cur))
    s += ''.join(cur)
    return s

def test():
    s = 'aosethfoasfdnssafh'
    print(sort_by_occurance(s,True))

if __name__ == '__main__':
    test()

# try:
#     while True:
#         s = [x for x in input() if x.isalnum() or ' ' == x]
#         s = sort_by_occurance(s)
#         print(s)
# except EOFError:
#     pass
# except Exception as e:
#     traceback.print_exc(e)