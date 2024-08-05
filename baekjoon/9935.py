def string_explosion(s, bomb):
    stack = []
    bomb_length = len(bomb)

    for char in s:
        stack.append(char)
        if len(stack) >= bomb_length and ''.join(stack[-bomb_length:]) == bomb:
            del stack[-bomb_length:]

    result = ''.join(stack)
    return result if result else "FRULA"

def main():
    s = input().strip()
    bomb = input().strip()
    
    result = string_explosion(s, bomb)
    print(result)

if __name__ == "__main__":
    main()