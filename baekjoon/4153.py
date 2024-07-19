while True:
    triangle = sorted(list(map(int,input().strip().split())))
    if triangle[0]==0 and triangle[1]==0 and triangle[2]==0: break
    print("right" if triangle[2]**2==triangle[0]**2+triangle[1]**2 else "wrong")