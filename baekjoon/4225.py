import math

def cross_product(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    def build_half_hull(points):
        hull = []
        for p in points:
            while len(hull) >= 2 and cross_product(hull[-2], hull[-1], p) <= 0:
                hull.pop()
            hull.append(p)
        return hull[:-1]

    lower = build_half_hull(points)
    upper = build_half_hull(points[::-1])
    return lower + upper

def rotating_calipers(points):
    hull = convex_hull(points)
    n = len(hull)
    if n <= 2:
        return distance(hull[0], hull[1])

    k = 1
    while cross_product(hull[n-1], hull[0], hull[(k+1) % n]) > cross_product(hull[n-1], hull[0], hull[k]):
        k += 1

    min_width = float('inf')
    for i in range(n):
        while cross_product(hull[i], hull[(i+1) % n], hull[(k+1) % n]) > cross_product(hull[i], hull[(i+1) % n], hull[k]):
            k = (k + 1) % n
        
        width = abs(cross_product(hull[i], hull[(i+1) % n], hull[k])) / distance(hull[i], hull[(i+1) % n])
        min_width = min(min_width, width)

    return min_width

def solve():
    case = 1
    while True:
        n = int(input())
        if n == 0:
            break

        points = [tuple(map(float, input().split())) for _ in range(n)]
        min_width = rotating_calipers(points)
        print(f"Case {case}: {math.ceil(min_width * 100) / 100:.2f}")
        case += 1

solve()