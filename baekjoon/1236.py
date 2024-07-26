def min_guards_to_add(castle, y, x):
    row_has_guard = [False] * y
    col_has_guard = [False] * x
    
    for j in range(y):
        for i in range(x):
            if castle[j][i] == 'X':
                row_has_guard[j] = True
                col_has_guard[i] = True
    
    rows_without_guard = row_has_guard.count(False)
    cols_without_guard = col_has_guard.count(False)
    
    return max(rows_without_guard, cols_without_guard)

y, x = map(int, input().strip().split())
castle = [input().strip() for _ in range(y)]

print(min_guards_to_add(castle, y, x))