import sys
input = sys.stdin.readline

n=int(input().strip())
nums=[0]*10001
for _ in range(n):
    num=int(input().strip())
    nums[num]+=1
for i in range(1,10001):
    if nums[i]>0:
        for _ in range(nums[i]):
            print(str(i))