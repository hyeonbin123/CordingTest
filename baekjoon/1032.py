t=int(input().strip())
filenames=[input().strip() for _ in range(t)]
check=filenames.pop(0)
result=''
for i in range(len(check)):
    patten_check=True
    for j in range(len(filenames)):
        if filenames[j][i] != check[i]:
            patten_check=False
            break
    if patten_check: result+=check[i]
    else: result+='?'
print(result)