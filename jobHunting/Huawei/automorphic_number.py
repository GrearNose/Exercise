import traceback

def automorphic_num_cnt(n):
    cnt = 0
    nums = []
    for i in range(n+1):
        sq = str(i**2)
        si = str(i)
        if sq.endswith(si):
            nums.append(i)
            cnt += 1
    return cnt,nums

def test():
    n = 200
    cnt,nums = automorphic_num_cnt(n)
    print(cnt, nums)

if __name__ == '__main__':
    test()

# try:
#     while True:
#         n = int(input())
#         print(automorphic_num_cnt(n))
# except EOFError:
#     pass
# except Exception as e:
#     traceback.print_exc(e)