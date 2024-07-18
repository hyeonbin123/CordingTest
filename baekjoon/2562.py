su={int(input().strip()) : i for i in range(1,10)}
print(max(su.keys()))
print(su[max(su.keys())])