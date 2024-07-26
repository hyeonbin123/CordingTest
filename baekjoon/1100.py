chessboard=[input().strip() for _ in range(8)]
white_check=0
for y in range(8):
    for x in range(8):
        if y%2==0 and x%2==0 and chessboard[y][x]=='F': white_check+=1
        if y%2==1 and x%2==1 and chessboard[y][x]=='F': white_check+=1
print(white_check)