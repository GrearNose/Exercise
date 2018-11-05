# coding=utf-8
import sys 
from itertools import product

def inner_join(a,b):
    assert isinstance(a,(list,tuple))
    assert isinstance(b,(list,tuple))
    a.sort(key=lambda x: x[0])
    b.sort(key=lambda x: x[0])
    result = []
    i,j = 0,0
    while i < len(a) and j < len(b):
        if a[i][0] < b[j][0]:
            i += 1
        elif a[i][0] > b[j][0]:
            j += 1
        else:
            i_up = i
            while i_up < len(a) and a[i_up][0] == a[i][0]:
                i_up += 1
            j_up = j
            while j_up< len(b) and b[j_up][0] == b[j][0]:
                j_up += 1
            result += [item[0] + item[1][1:] for item in product(a[i:i_up],b[j:j_up])]
            i,j = i_up,j_up
    return result

def test():
    x = [(1,2),(1,3),(2,3)]
    y = [(1,2),(1,3),(2,4)]
    for it in inner_join(x,y):
        print(it)

if __name__ == '__main__':
    test()
