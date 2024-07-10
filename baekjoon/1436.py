def find_nth_666_title(n):
    count = 0
    number = 666
    while True:
        if '666' in str(number):
            count += 1
            if count == n:
                return number
        number += 1

def main():
    n = int(input())
    result = find_nth_666_title(n)
    print(result)

if __name__ == "__main__":
    main()