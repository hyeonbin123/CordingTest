def transform_park(park):
    translation = {'S': 1, 'O': 0, 'X': 99}
    return [[translation[cell] for cell in row] for row in park]

def find_start(park_map):
    for y, row in enumerate(park_map):
        for x, cell in enumerate(row):
            if cell == 1:
                return [y, x]

def is_valid_move(park_map, y, x):
    return 0 <= y < len(park_map) and 0 <= x < len(park_map[0]) and park_map[y][x] != 99

def solution(park, routes):
    park_map = transform_park(park)
    pos = find_start(park_map)
    
    directions = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    
    for route in routes:
        direction, distance = route.split()
        distance = int(distance)
        dy, dx = directions[direction]
        
        new_y, new_x = pos
        for _ in range(distance):
            new_y += dy
            new_x += dx
            if not is_valid_move(park_map, new_y, new_x):
                break
        else:
            pos = [new_y, new_x]
    
    return pos

park, routes = ["SOO","OOO","OOO"], ["E 2","S 2","W 1"]
print(solution(park, routes))