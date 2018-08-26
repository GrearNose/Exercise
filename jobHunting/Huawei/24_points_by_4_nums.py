import traceback
from itertools import permutations

def expr_to_a_val(nums,val):
    """
        Given four numbers, judge whether there exists an expression
        consists of them and operator '+-*/'.
    """
    if None == nums or None == val or 4 != len(nums):
        return False

    operators = '+-*/'
    for p1 in permutations(nums,2):
        for op1 in operators:
            expr = '(' + p1[0] + op1 + p1[1] + ')'
            if '/' == op1 and 0 == eval(p1[1]):
                continue
            rest1 = nums.copy()
            rest1.remove(p1[0])
            rest1.remove(p1[1])
            rest1.append(expr)
            # print(nums,p1,rest1)
            for p2 in permutations(rest1,2):
                for op2 in operators:
                    expr = '(' + p2[0] + op2 + p2[1] + ')'
                    if '/' == op2 and 0 == eval(p2[1]):
                        continue
                    rest2 = rest1.copy()
                    rest2.remove(p2[0])
                    rest2.remove(p2[1])
                    rest2.append(expr)
                    # print(rest2)
                    for p3 in permutations(rest2,2):
                        for op3 in operators:
                            expr = p3[0] + op3 +p3[1]
                            if '/' == op3 and 0 == eval(p3[1]):
                                continue
                            # print(expr)
                            if val == eval(expr):
                                return True,expr
    return False

def test():
    nums = '7,2,1,10'.split(',')
    print('nums:', nums)
    val = 24
    rslt = expr_to_a_val(nums,val)
    if False != rslt:
        print(rslt[1])
    else:
        print(rslt)

if __name__ == '__main__':
    test()

# try:
#     while True:
#         nums = input().split()
#         val = 24
#         if expr_to_a_val(nums,val):
#             print('true')
#         else:
#             print('false')
# except EOFError:
#     pass
# except Exception as e:
#     print(expr)
#     traceback.print_exc(e)