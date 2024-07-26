def generate_sequence(length):
    sequence = []
    num = 1
    while len(sequence) < length:
        sequence.extend([num] * num)
        num += 1
    return sequence[:length]


def main():
    A, B = map(int, input().split())
    sequence = generate_sequence(B)
    print(sum(sequence[A-1:B]))

if __name__ == "__main__":
    main()