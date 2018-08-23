try:
    while True:
        N,m = [int(x) for x in input().split()]
        prices = [0] * m
        values = [0] * m
        Q      = [0] * m
        for i in range(m):
            v,p,q = [int(x) for x in input().split()]
            prices[i] = v
            values[i] = v*p
            Q[i]      = q

        for i in range(m):
            if Q[i] > 0:
                ix = Q[i] - 1
                prices[i] += prices[ix]
                values[i] += values[ix]

        pre = [0]*prices[0] + [values[0]] * (N+1-prices[0])
        cur = pre.copy()
        # print(0, pre[start_price:])
        # print("len",len(pre))
        for i in range(1,m):
            for j in range(prices[i],N+1):
                if prices[i] <= j:
                    cur[j] = max(pre[j], pre[j-prices[i]]+values[i])
                else:
                    cur[j] = pre[j]
            pre,cur = cur,pre
        print(pre[-1])
except Exception:
    pass