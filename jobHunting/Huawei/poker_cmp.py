from collections import Counter
import traceback

"""
    Problem Description
    a poker consists of 54 faces: 3~A,2, four for each, joker and JOKER,
    with the following rank:
        3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER
    Given two set of cards, each represented by space-separated chars, 
    and they are connected by '-'.
        e.g. 4 4 4 4-joker JOKER
    compare the rank relation of them, and print the higher one if they can be
    compared, 'ERROR' otherwise.
    Type of cards (in ascending rank order):
        individual(no reoccurance), pairs(occurance of 2),straight
        (5 consective cards) triple(occurance of 3), bomb(occurance of 4),
        and two-joker (both joker and JOKER appear).
    Rule for comparing:
        Comparision can only be made between two set of cards of same type, 
        except for bomb and two-joker, which can be compared with any other
        type of cards. When comparing two set of cards of the same type,
        the higher one is the one with larger face value. When their type
        is 'straight', the comparision between them is the comparision
        between theirs minimum ones.
    Inputs:
        a string of two set of cards connected by '-'  and each consists
        of chars separated by space. e.g. "4 4 4 4-joker JOKER".
        These two set of cards are ensured to be different.
    Output:
        The one with higher rank if they can be compared, 'ERROR' otherwise.
"""

poker_id  = [3,4,5,6,7,8,9,10,'J','Q','K','A',2,'joker','JOKER']
poker_id  = [str(i) for i in poker_id]
types     = ['Indiv','Pairs','Triple','Straight','Bomb','jokers']
rank_indv = {poker_id[i]:i+1 for i in range(len(poker_id))}
rank_type = {types[i]:i+1 for i in range(len(types))}
types_mp  = {1:'Indiv',2:'Pairs',3:'Triple',4:'Bomb',5:'Straight','jokers':'jokers'}

def poker_type(pokers):
    if None == pokers or 0 == len(pokers):
        return None
    pokers = [rank_indv[p] for p in pokers]
    cnt = Counter(pokers)
    ptypes = {}
    for occ in range(1,4+1):
        ps = [k for k in cnt if occ == cnt[k]]
        ptypes[types_mp[occ]] = max(ps) if len(ps)>0 else 0
    str_min = -1
    p_uniq = sorted(cnt)
    for i in range(4,len(p_uniq)):
        if 4 == p_uniq[i] - p_uniq[i-4]:
            str_min = p_uniq[i-4]
    ptypes[types_mp[5]] = str_min if -1 != str_min else 0
    
    if rank_indv['joker'] in cnt and rank_indv['JOKER'] in cnt:
        ptypes[types_mp['jokers']] = 1
    else:
        ptypes[types_mp['jokers']] = 0
    return ptypes

def poker_compare(p1,p2):
    for t in types[-2:][::-1]: # for the last two types
        if p1[t] > p2[t]:
            return True
        elif p1[t] < p2[t]:
            return False
    for t in types[:-2][::-1]:
        if p1[t] and p2[t]:
            if p1[t] > p2[t]:
                return True
            elif p1[t] < p2[t]:
                return False
    return 'ERROR'


def test():
    cards   = 'joker JOKER-K K K K'
    p10,p20 = cards.split('-')
    p1      = poker_type(p10.split())
    p2      = poker_type(p20.split())
    print('p1:', p1)
    print('p2:', p2)
    p_cmp = poker_compare(p1,p2)
    if p_cmp not in (True, False):
        print('ERROR')
    p = p10 if p_cmp else p20
    print(p)

if __name__ == '__main__':
    test()

# try:
#     while True:
#         p10,p20 = input().split('-')
#         p1 = poker_type(p10.split())
#         p2 = poker_type(p20.split())
#         # print(p1,p2);break
#         p_cmp = poker_compare(p1,p2)
#         if p_cmp not in (True, False):
#             print('ERROR')
#         elif True == p_cmp:
#             print(p10)
#         else:
#             print(p20)
# except EOFError:
#     pass
# except Exception as e:
#     traceback.print_exc(e)