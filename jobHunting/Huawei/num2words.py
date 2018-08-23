import traceback
def num2words(n):
    if 0 == n:
        return 'zero'
    radix0 = ['one','two','three','four','five','six','seven','eight','nine']
    radix1 = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    radix2 = ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    radix3 = ['thousand','million','billion']
    def numWithinHundred(n):
        s = []
        if 0 == n:
            return s
        d1 = n % 10
        n //= 10
        d2 = n % 10
        n //= 10
        if d1 != 0 and d2 != 1: # 0x or [2-9]x
            s.append(radix0[d1-1])
        if d2 != 0:
            if d2 == 1:
                s.append(radix1[d1])
            else: # [2-9]x
                s.insert(0,radix2[d2-1])
        d3 = n % 10
        if d3 > 0:
            s.insert(0,'and')
            s.insert(0,'hundred')
            s.insert(0, radix0[d3-1])
            
        return s
    stack = []
    ix_radix = 0 # ix for radix3
    while n > 0:
        num_cur = numWithinHundred(n)
        if ix_radix > 0:
            num_cur.append(radix3[ix_radix-1])
        stack.append(num_cur)
        n //= 1000
        ix_radix += 1
    print(stack)
    num_word = []
    while len(stack) >0:
        num_word.extend(stack.pop())
    num_str = ' '.join(num_word)    

    return num_str

try:
    while True:
        n = int(input().strip())
        num_str = num2words(n)
        print(num_str)
except EOFError:
    pass
except Exception as e:
    traceback.print_exc(e)