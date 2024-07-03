from collections import deque

def check(deck1, deck2, target):
    operand = set(deck2)
    for card in deck1:
        if target - card in operand:
            deck1.remove(card)
            deck2.remove(target-card)
            return True
    return False

def solution(coin, cards):
    hand = cards[:len(cards) // 3]
    deck = deque(cards[len(cards) // 3:])
    pending = []
    turn = 1
    while coin >= 0 and deck:
        pending.append(deck.popleft())
        pending.append(deck.popleft())
        
        if check(hand, hand, len(cards) + 1):
            pass
        elif coin >= 1 and check(hand, pending, len(cards) + 1):
            coin -= 1
        elif coin >= 2 and check(pending, pending, len(cards) + 1):
            coin -= 2
        else:
            break
        turn += 1
    return turn























test_cases=[[4,[3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]],
           [3,[1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]],
           [2,[5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]],
           [10,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]]

for test in test_cases:
    coin,cards = test
    print(solution(coin,cards))
    # break