def the_kth_y(x,k):
    """
        Given a positve integer x, there exists a postive integer y, such that
            x+y = x|y.
        There are many such y satifying this equation, try to find the kth y.
    """
    if None == x or None == k or x < 0 or k < 0:
        return None
    bx = '{:b}'.format(x)
    bk = '{:b}'.format(k)
    print('x: %d %s'%(x,bx), '\nk: %d %s'%(k,bk))
    bx = list(bx)
    bk = list(bk)
    # Algorithm
    # Take the folowing one as an example:
    # '10101' + '10' = '10111' == '10101' | '10'
    # '10101' + '1010' = '11111' == '10101' | '1010'
    # '10101' + '1' = '10110' != '10101' | '10'
    # It's easy to find that this equation require y's binary bit be '0' where
    # x's corresponding binary bit is '1', but can be '0' or '1' elsewhere.
    # Thus the kth y is the kth permutation of '01' bits at positions where
    # x's binary bit is '0', i.e.
    # constructing y's binary str, by replacing '0' in x's binary str with k's
    # binary str, and replacing '1' in x's binary str with '0', from right to
    # left. If the len of k's binary str is longer than the number '0' in x's
    # binary str, concatenate the axtra substr of k's binary at the left end
    # with the replcaed str. Finaly, here is the binary str of y.
    s  = '' # to record the binary str.
    while len(bk) > 0:
        while len(bx) > 0 and bx[-1] == '1':
            s = '0' + s
            bx.pop()
        if len(bx) > 0:
            bx.pop()
            s = bk.pop() + s
        else:
            s = ''.join(bk) + s
            break

    y = int(s,2)
    print('y:', y, s)

    return y

def test():
    x,k = 7,5
    y = the_kth_y(x,k)

if __name__ == '__main__':
    test()
