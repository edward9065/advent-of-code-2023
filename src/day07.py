from collections import Counter
from functools import cmp_to_key
card_values = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

# value is arbitrary, but it's higher the higher the hand type is - this is for use in comparison
def get_hand_value(hand: str) -> int: 
    card_counter = Counter(hand)
    two_most_common = card_counter.most_common(2)
    if two_most_common[0][1] > 3:
        return two_most_common[0][1] + 2
    elif two_most_common[0][1] == 3:
        return two_most_common[0][1] + two_most_common[1][1]
    else:
        return two_most_common[0][1] + 1 

    
def cmp_hands(hand1: list, hand2: list):
    val1 = get_hand_value(hand1[0])
    val2 = get_hand_value(hand2[0])
    if(val1 == val2):
        for i in range(5):
            if hand1[0][i] == hand2[0][i]:
                continue
            else:
                return card_values[hand1[0][i]] - card_values[hand2[0][i]]
        return 0
    else:
        return val1-val2


with open("../input/day07.txt", encoding="utf-8") as input:
    data = input.read().split("\n")

data = [row.split(" ") for row in data]
data.sort(key=cmp_to_key(cmp_hands))
print(data)
total_winnings = 0
for rank, hand in enumerate(data):
    total_winnings += (int(rank)+1)*int(hand[1])
print(total_winnings)
     

