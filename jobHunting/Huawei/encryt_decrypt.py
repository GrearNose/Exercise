import traceback

def encrypt_decrypt(txt,isEncrypt=True):
    if None == txt or 0 == len(txt):
        return None
    msg = []
    offset = 1 if isEncrypt else -1
    for c in txt:
        if c.isalpha():
            if c.islower():
                asc = ord(c.upper()) + offset
                w = chr(asc) if asc <= ord('Z') else 'A'
            else:
                asc = ord(c.lower()) + offset
                w = chr(asc) if asc <= ord('z') else 'a'
        elif c.isdigit():
            asc = ord(c) + offset
            w = chr(asc) if asc <= ord('9') else '0'
        else:
            w = c
        msg.append(w)
        return ''.join(msg)
def test():
    plaintext = "TJm5Jpgv9gokaSPV4xa77ZeT7W08RI7G7DIp77k9Hx8zM9VfrK47qL05VaC6uf8P1p0EMu259D1Oj0P4lFi36MM";
    cipher    = "ylV2Zv83sVqf1LF0P6soqMYF1aAv0i61iy0oScauz4Wv6HGo30C9v1xFus8e9JZ0VG6JF1680h2Zk3OV26ZYjg5YQHT09ig";
    print(encrypt_decrypt(plaintext))
    print(encrypt_decrypt(cipher,False))    

# try:
#     while True:
#         plaintext = input()
#         cipher    = input()
#         print(encrypt_decrypt(plaintext))
#         print(encrypt_decrypt(cipher,False))
# except Exception as e:
#     # traceback.print_exc(e)
#     pass