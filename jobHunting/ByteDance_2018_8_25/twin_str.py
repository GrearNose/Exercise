from random import randint

def twin_str(s,t):
    """
        Judge whether the given two strings s and t are twin strings.
        String s and t are twin strings if t can be constructed by connecting
        s's head to s's tail forming a ring, and starting at one certain point
        to traverse the ring clockwise or anticlockwise. It's can be easily
        derived that if t can be constructed by s, and s can also be constructed
        by t.
        === Arg ===
        s: one of the string to judge,
        t: the other string to judge.
        return True if s and t and twin strings, False otherwise.
    """
    if None == s or None == t or len(s) != len(t):
        return False

    for i in range(len(s)):
        s1,s2 = s[:i],s[i:] # choose the point at i to cut.
        str1 = s1[::-1] + s2[::-1] # anti-clockwise
        str2 = s2 + s1[::-1] # clockwise
        if str1 == t or str2 == t:
            return True
    return False


def test():
    s = 'abcdefg'
    s = 'helloWorld'
    # s = 'a'
    s = 'abcd'
    for i in range(len(s)):
        str1 = s[:i][::-1] + s[i:][::-1]
        str2 = s[i:] + s[:i][::-1]
        stmp = s + s
        print(s,str1,twin_str(s,str1), str1 in stmp or str1 in stmp[::-1])
        print(s,str2,twin_str(s,str2), str2 in stmp or str2 in stmp[::-1])

        x = randint(0,len(s))
        str1 = str1[:x]+str1[x+1:]
        str2 = str2[:x]+str2[x+1:]
        print(s,str1,twin_str(s,str1))
        print(s,str2,twin_str(s,str2))

if __name__ == '__main__':
    test()



