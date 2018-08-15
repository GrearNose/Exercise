"""
Problem Description
Given a string of digits, figure out how many ways
to divide it into two valid numbers and optionally
add radix points to them. A a number is valid if it does
not start with 0 except that it has only decimal part,
in which case it can at most have one 0; and its decimal
part does not end with zero.
"""

def com_num(s):
    """
        convert a str s into all valid number forms
        by optionally adding a radix point to all possible positions.
    """
    num = []
    if len(s) == 1: # only one digit, no way to add radix point.
        return [s]
    if s[0] != '0': # valid integer if not starts with '0'.
        num.append(s)
    for i in range(1,len(s)): # try all possible pos to insert a radix point.
        s1 = s[:i]
        s2 = s[i:]
        if len(s1) > 1 and s1[0] == '0' : continue # integer part starts with '0'.
        if s2[-1] == '0': continue # decimal part ends with '0'.
        tmp = s[:i] +'.' + s[i:]   # otherwise it's a valid real num.
        num.append(tmp)
    return num

# s = '00011'
# s = '123'
# s = '00103'
# s = '1201'
# s = '0102'
s = '010'
# s = input()
pairs = set()
for i in range(1,len(s)):
    s1 = s[:i]
    s2 = s[i:]
    # print('s1:',s1, 's2:',s2)
    if len(s1) > 1 and all([c == '0' for c in s1]): continue
    if len(s2) > 1 and all([c == '0' for c in s2]): continue
    num1 = com_num(s1)
    num2 = com_num(s2)
    # print('num1:',num1, 'num2:',num2)
    if len(num1) == 0: continue
    if len(num2) == 0: continue
    for n1 in num1:
        for n2 in num2:
            pairs.add((n1,n2)) # use a set to exclude redundancy.
            # print(n1,n2)
            # pass

# print(pairs)
print(len(pairs))
