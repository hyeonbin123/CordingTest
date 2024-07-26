def classify_triangle(a,b,c):

    if sum([a,b,c]) != 180:
        return "Error"
    
    if [a,b,c] == [60,60,60]:
        return 'Equilateral'
    elif a == b or a == c or b == c:
        return 'Isosceles'
    else:
        return 'Scalene'
    
Angles = [int(input().strip()) for _ in range(3)]
print(classify_triangle(*Angles))