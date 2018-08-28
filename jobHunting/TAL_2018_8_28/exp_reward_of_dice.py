import traceback

"""
    Problem Description:
    Here is a dice of n faces, each with equal probability to settle on,
    and each yields a reward. There m faces of n that also come with
    a reward that yield another chance to cast the dice.
    Give n,m, and n rewards, figure out the expectation of the final reward.
"""
try:
    while True:
        n,m    = [int(x) for x in input().split()]
        reward = [int(x) for x in input().split()]
        exp1   = sum(reward) / n # expectation of one cast.
        p      = m/n             # the probability of getting a reward.
        exp_final = exp1 * (1 + p/(1-p))
        print('%.2f' % exp_final)
except EOFError:
    pass
except Exception as e:
    traceback.print_exc(e)