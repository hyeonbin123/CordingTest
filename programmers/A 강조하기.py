def solution(myString):
    myString_l = myString.lower()
    
    return myString_l.replace("a", "A")
    
# myString = 'ASDFas fdasdasASDFD FASDFASsfsafs'
myString = 'sdgsdfgsdgsdgdsSDFGSDFGSDFGSDFGSDFGHFDSHSDGSDG'
print(solution(myString))