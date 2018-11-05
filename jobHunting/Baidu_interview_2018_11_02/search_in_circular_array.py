# surely this is the first version and it's incorrect.
def find_in_circular_arr(arr,val):
    assert isinstance(arr,(list,tuple))
    assert isinstance(val,int)
    i,j = 0,len(arr)-1
    while i < j:
        m = (i+j) >> 1
        if arr[m] == val:
            return m
        if arr[m] > arr[i]: # left segment
            if arr[m] < val:
                j = m - 1
            elif arr[m] > val:
                i = m+1
        else: # right segment
           if arr[m] > val:
               j = m -1
           else:
               i = m + 1
    print("not found")
    return -1 # not found

def find_in_circular_arr_v2(arr,val):
    assert isinstance(arr,(list,tuple))
    assert isinstance(val,int)
    i,j = 0,len(arr)-1
    # find the border, the ending index of the left segment
    while i + 1 < j:
        m = (i+j) >> 1
        if arr[m] > arr[i]:
              i = m
        elif arr[m] < arr[j]:
              j = m
        else:
            raise Exception("not a circular array!")
    ix_border = i # ending index of the left segment.
    # print('ix_border:', ix_border)
    if arr[0] <= val and val <= arr[ix_border]:
        # print("search the left segment...")
        ix = bisearch(arr,0, ix_border, val)
    elif arr[ix_border+1] <= val and val <= arr[-1]:
        ix = bisearch(arr,ix_border+1,len(arr)-1, val)
    else:
        ix = -1
    return ix

def bisearch(arr, ix_begin, ix_end, val):
    assert isinstance(arr,(list,tuple))
    assert isinstance(val,int)
    assert isinstance(ix_begin,int)
    assert isinstance(ix_end,int)
    assert 0 <= ix_begin
    assert ix_begin <= ix_end
    i,j = ix_begin,ix_end
    while i <= j:
        # print(i,j,arr[i],arr[j])
        m = (i+j)>>1
        if arr[m] < val:
            i = m + 1
        elif arr[m] > val:
            j = m - 1
        else:
            return m
    return -1 # not found


def find_in_circular_arr_v3(arr,val):
    assert isinstance(arr,(list,tuple))
    assert isinstance(val,int)
    i,j = 0,len(arr)-1
    while i <= j:
        m = (i+j) >> 1
        if val == arr[m]:
            return m
        elif arr[m] >= arr[i]: # arr[m] belongs the left segment
            if arr[i] <= val:  # val might be in the left segment,
                if val <= arr[m]: # search its left part.
                    j = m
                else: # val might be in its right part, 
                      # but as the border is unknown, so move i towards right instead.
                    i = m+1
            elif val <= arr[j]:
                i = m +1
            else: # arr[j] < val and val < arr[i], so not found
                return -1
        elif arr[m] <= arr[j]: # arr[m] belongs to the right segment
            if arr[i] <= val:
                j = m - 1
            elif val <= arr[j]: # search val in the right segment
                if arr[m] <= val: # search right part of the right segment
                    i = m
                else: # val < arr[m]
                    # val might be in the left part of the segment, 
                    # but the border is unknown, so move j towards left instead.
                    j = m - 1
            else:
                return -1 # not found
        else:  # arr[j] < val and val < arr[i], so not found
            raise Exception('Not a circular array!')

    # print("not found")
    return -1 # not found

def find_in_circular_arr_v4(arr,val):
    assert isinstance(arr,(list,tuple))
    assert isinstance(val,int)
    if 0 == len(arr):
        return -1
    i,j = 0,len(arr)-1
    while i <= j:
        m = (i+j) >> 1
        if val < arr[m]:
            if arr[i] <= val: # then arr[i] < arr[m], arr[m] belongs to the left segment,
                # val can only be in the left part of the left segment.
                if arr[i] == val: return i
                j = m - 1
            elif val <= arr[j]: # val can only be in the right segment.
                # but still not sure arr[m] belongs to which segment;
                if arr[m] <= arr[j]: # arr[m] belongs to the righ segment,
                # so val might be in its left part, but cannot directly search
                # this part as the border of the two segments is unknown, so, instead,
                # narrow the search range by moving j towards left.
                    j = m - 1
                else: # arr[m] belongs to the left segment, but val is not within it.
                    # thus narrow the searching range by moving i towards right.
                    i = m + 1
            else: # arr[j] < val and val < arr[i], so not found.
                return -1

        elif arr[m] < val:
            if arr[i] <= val: # val can only be in the left segment,
            # but not sure arr[m] belongs to which segment
                if arr[i] <= arr[m]: # arr[m] belongs to the left segment
                    i = m + 1 # search the right part of the left segment
                else: # arr[m] belongs to the right segment,
                # narrow the searching range by moving j towards left.
                    j = m - 1
            elif val <= arr[j]: # i.e. arr[m] < val <= arr[j], thus arr[m] belongs to the right segment.
                # search the right part of the right segment.
                i = m + 1
            else: # arr[j] < val and val < arr[i], so not found.
                return -1

        else:
            return m
    return -1

def test():
    arr = [3,4,5,6,7,8,9,0,1,2]
    # arr = [1,2,3,4,5,6,7,8,9,0]
    # arr = list(range(10))
    # arr = [0]
    # arr = [0,0]
    # arr = [0,0,0]
    print('arr:', arr)
    for val in [12,45,31] + arr + [-1,-4,-9]:
        print('val:',val, end ='; ')
        # ix = find_in_circular_arr(arr,val)
        # ix = find_in_circular_arr_v2(arr,val)
        # ix = find_in_circular_arr_v3(arr,val)
        ix = find_in_circular_arr_v4(arr,val)
        print('ix,val,correct:', ix,arr[ix],val==arr[ix])

if __name__ == '__main__':
    test()