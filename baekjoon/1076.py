# 1
color=['black','brown','red','orange','yellow','green','blue','violet','grey','white']
resistances={color[i]:[str(i),10**i] for i in range(10)}
result=''
for i in range(3):
    resistance=input().strip()
    if i!=2:
        result+=resistances[resistance][0]
    else:
        result=int(result)*resistances[resistance][1]
print(result)

#2
v="black brown red orange yellow green blue violet grey white".split()
print((v.index(input())*10+v.index(input()))*10**v.index(input()))