import traceback

def search_sudoku(sudoku,ix_row,ix_col):
    if None == sudoku or None == ix_row or None == ix_col:
        return
    cnt_r = [len(r) for r in ix_row]
    cnt_c = [len(c) for c in ix_col]
    if sum(cnt_r) == 45:
        return True # found a solu.
    min_r = min([x for x in cnt_r if x > 0])
    min_c = min([x for x in cnt_c if x > 0])

    # try one row or col with the min num of vacant cells
    if min_r < min_c:
        r = cnt_r.index(1)
        nums = [x for x in range(1,10) if x not in sudoku[r]]
        
        c = ix_row[r][0] # fetchh the col index.
        sudoku[r][c] = 45 - sum(sudoku[r])
        ix_row[r] = []   # as the vacant is filled.
        update = True
    if 1 in cnt_c:
        c = cnt_c.index(1)
        r = cnt_c[c][0]
        sudoku[r][c] = 45 - sum([sudoku[i][c] for i in range(9)])
        cnt_col[c]
        update = True    

def solve_sudoku(sudoku)
    ix_row,ix_col = [], []
    for i in range(9):
        ix_r,ix_c = [],[]
        for j in range(9):
            if 0 == sudoku[j][i]: ix_c.append(j)
            if 0 == sudoku[i][j]: ix_r.append(j)
        ix_row.append(ix_r)
        ix_col.append(ix_c)
    search_sudoku(sudoku,ix_row,ix_col)

try:
    while True:
        sudoku = []
        for i in range(9):
            r = [int(x) for x in input().strip().split()]
            sudoku.append(r)
        solve_sudoku(sudoku)
        for r in sudoku:
            for x in r:
                print(x,end=' ')
            print()        
except EOFError:
    pass
except Exception as e:
    traceback.print_exc(e)