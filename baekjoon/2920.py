c_major=list(map(int,input().strip().split()))
print('ascending' if c_major == sorted(c_major) else 'descending' if c_major == sorted(c_major,reverse=True) else 'mixed')