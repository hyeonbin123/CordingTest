import sys

def spread_dust(room, R, C):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    new_room = [[0] * C for _ in range(R)]
    
    for x in range(R):
        for y in range(C):
            if room[x][y] > 0:
                spread_amount = room[x][y] // 5
                spread_count = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != -1:
                        new_room[nx][ny] += spread_amount
                        spread_count += 1
                new_room[x][y] += room[x][y] - spread_amount * spread_count
            elif room[x][y] == -1:
                new_room[x][y] = -1
    
    return new_room

def operate_air_purifier(room, air_purifier, R, C):
    top = air_purifier[0]
    
    for i in range(top - 1, 0, -1):
        room[i][0] = room[i-1][0]
    for i in range(C - 1):
        room[0][i] = room[0][i+1]
    for i in range(top):
        room[i][C-1] = room[i+1][C-1]
    for i in range(C - 1, 1, -1):
        room[top][i] = room[top][i-1]
    room[top][1] = 0

    bottom = air_purifier[1]
    
    for i in range(bottom + 1, R - 1):
        room[i][0] = room[i+1][0]
    for i in range(C - 1):
        room[R-1][i] = room[R-1][i+1]
    for i in range(R - 1, bottom, -1):
        room[i][C-1] = room[i-1][C-1]
    for i in range(C - 1, 1, -1):
        room[bottom][i] = room[bottom][i-1]
    room[bottom][1] = 0

def simulate(room, air_purifier, R, C, T):
    for _ in range(T):
        room = spread_dust(room, R, C)
        operate_air_purifier(room, air_purifier, R, C)
    return room

def calculate_dust(room):
    return sum(sum(row) for row in room) + 2

R, C, T = map(int, input().split())
room = []
air_purifier = []

for i in range(R):
    row = list(map(int, input().split()))
    room.append(row)
    if -1 in row:
        air_purifier.append(i)

final_room = simulate(room, air_purifier, R, C, T)

print(calculate_dust(final_room))