import traceback
try:
    while True:
        inputs = input().strip().split()
        n = int(inputs[0])
        data_head = int(inputs[1])
        ix = 0
        data,ix_next = [None]*n, [None]*n
        for i in range(2,2*n-1,2):
            p,q = [int(x) for x in inputs[i:i+2]] # p<-q
            if p in data:
                ix_p = data.index(p)
            else:
                ix_p = ix
                ix += 1
                data[ix_p] = p
                if p == data_head: 
                    ix_head = ix_p
            if q in data:
                ix_q = data.index(q)
            else:
                ix_q = ix
                ix += 1
                data[ix_q] = q
                if q == data_head: 
                    ix_head = ix_q
            ix_next[ix_q] = ix_p # q -> p
            print(i,[p,ix_p],[q,ix_q])
        data_to_del = int(inputs[-1])
        print(data)
        print(ix_next)
        print(ix,ix_head)
        ix = ix_head
        while None != ix_next[ix]:
            if data[ix] != data_to_del:
                print(data[ix],end=' ')
            ix = ix_next[ix]
except EOFError:
    pass
except Exception as e:
    traceback.print_exc(e)