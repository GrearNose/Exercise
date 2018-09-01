import traceback

def min_attack(life, norm, buffe):
    """
        To kill a monster with life endurance value 'life', one can attack it
        constantly and this will cuase its 'life' indcrease a 'norm' each time,
        while one can also attack it one time every two chances, and this will
        cause a 'buffe' decrease of its 'life'. Given life, norm and buffe,
        figure out the minimum chances to kill the monster.
    """
    f2,f1 = max(2*norm,buffe),norm
    if life <= f1: # f(n-2)
        return 1
    if life <= 2: # f(n-1)
        return 2
    fn_1, fn_2 = f2, f1 # f(n-1), f(n-2)
    fn = f2
    cnt = 2
    while fn < life:
        cnt += 1
        fn = max(fn_1 + norm, fn_2 + buffe)
        fn_1, fn_2 = fn,fn_1
    return cnt

# def test():
#     life, norm, buffe = 13, 3, 5
#     print(min_attack(life,norm,buffe))

# if __name__ == '__main__':
#     test()

try:
    while True:
        life, norm, buffe = int(input().strip()),int(input().strip()),int(input().strip())
        print(min_attack(life,norm,buffe))
except EOFError:
    pass
except Exception as e:
    traceback.print_exc(e)