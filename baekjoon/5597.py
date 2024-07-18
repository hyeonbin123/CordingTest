all_students=set(range(1,31))
submitted=set(int(input().strip()) for _ in range(28))
for i in sorted(all_students-submitted):
    print(i)