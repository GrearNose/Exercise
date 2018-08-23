def snake_matrix(n):
    snake = []
    i = 1
    for r in range(1,n+1):
        cnt = 0
        while cnt < r:
            if cnt > 0:
                snake[ix_r].append(i)
            else:
                snake.append([i])
                ix_r = r - 1
            ix_r -= 1
            i += 1
            cnt += 1
    return snake

def test():
    n = 5
    s = snake_matrix(n)
    for r in s:
        for c in r[:-1]:
            print(c,end=' ')
        print(r[-1])

if __name__ == '__main__':
    test()