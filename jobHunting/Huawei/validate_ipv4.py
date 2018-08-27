def is_valid_ipv4(s):
    s = s.split('.')
    if 4 != len(s):
        return False
    valid = True
    for seg in s:
        if not seg.isdigit():
            valid = False
            break
        n = int(seg)
        if  n<0 or n > 255:
            valid = False
            break
    return valid

def test():
    s = []
    s.append('10.138.151.1')
    s.append('10.138.151.sd')
    s.append('10.138.151.-2')
    s.append('10.138.151.256')
    s.append('10.138.a.256')
    s.append('982.138.2.256')
    s.append('138.2.22')
    s.append('0.138.2.22')
    for ip in s:
        print(ip, is_valid_ipv4(ip))

if __name__ == '__main__':
    test()
