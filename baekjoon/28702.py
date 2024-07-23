def fizzbuzz(n):
    if n % 15 == 0: return "FizzBuzz"
    if n % 3 == 0: return "Fizz"
    if n % 5 == 0: return "Buzz"
    return str(n)

fizzbuzzs=[input().strip() for _ in range(3)]
for index,value in enumerate(fizzbuzzs):
    if value.isdigit():
        print(fizzbuzz(int(value)+(3-index)))
        break