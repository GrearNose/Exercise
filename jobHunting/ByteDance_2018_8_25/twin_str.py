from random import randint

def twin_str(s,t):
    """
        Judge whether the given two strings s and t are twin strings.
        String s and t are twin strings if t can be constructed by connecting
        s's head to s's tail forming a ring, and starting at one certain point
        to traverse the ring clockwise or anticlockwise. It's can be easily
        derived that if t can be constructed by s, then s can also be constructed
        by t.
        === Arg ===
        s: one of the strings to judge,
        t: the other string to judge.
        return True if s and t and twin strings, False otherwise.
    """
    if None == s or None == t or len(s) != len(t):
        return False

    for i in range(len(s)):
        s1,s2 = s[:i],s[i:]         # choose the i-th point to cut the ring.
        str1  = s2 + s1             # clockwise
        str2  = s1[::-1] + s2[::-1] # anti-clockwise
        if str1 == t or str2 == t:
            return True
    return False


def twin_str_v2(s,t):
    """
        Another simpler to judge twin strings.
        As cutting at the ring yields a new str consisting of
        one substr from the tail of the original str as its head,
        and the rest of the original str as its tail.
    """
    if None == s or None == t or len(s) != len(t):
        return False
    trial1  = s + s
    trial2  = trial1[::-1]
    is_twin = t in trial1 or t in trial2
    return is_twin

def test():
    s = 'abcdefg'
    s = 'helloWorld'
    # s = 'a'
    s = 'abcd'
    s = 'abcdefghjkglmn'
    s = 'abcdefghjkglmnopqrstuvwxyz'
    s = 'abababbabababab'
    s = 'ababaccadaf'
    for i in range(len(s)):
        str1 = s[i:] + s[:i] # positive, clockwise twin
        str2 = str1[::-1]    # positive, anti-clockwise twin
        stmp = s+s
        print(s,str1,twin_str(s,str1),twin_str_v2(s,str1))
        print(s,str2,twin_str(s,str2),twin_str_v2(s,str2))

        # x = randint(0,len(s))
        # str1 = str1[:x]+str1[x+1:]
        # str2 = str2[:x]+str2[x+1:]
        # print(s,str1,twin_str(s,str1), twin_str_v2(s,str1))
        # print(s,str2,twin_str(s,str2), twin_str_v2(s,str2))

if __name__ == '__main__':
    test()
