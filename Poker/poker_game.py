import sys
from collections import defaultdict
from collections import Counter
from itertools import combinations
class poker:

    def __init__(self):

        self.values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "A":14}




        self.card_order_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12,
                                "K": 13, "A": 14}
        self.hand_dict = {10: "royal-flush", 9: "straight-flush", 8: "four-of-a-kind", 7: "full-house", 6: "flush", 5: "straight",
                     4: "three-of-a-kind", 3: "two-pairs", 2: "one-pair", 1: "highest-card"}

    def check_hand(self,hand):
        if self.check_royal_flush(hand):
            return 10
        if self.check_straight_flush(hand):
            return 9
        if self.check_four_of_a_kind(hand):
            return 8
        if self.check_full_house(hand):
            return 7
        if self.check_flush(hand):
            return 6
        if self.check_straight(hand):
            return 5
        if self.check_three_of_a_kind(hand):
            return 4
        if self.check_two_pairs(hand):
            return 3
        if self.check_one_pairs(hand):
            return 2
        return 1

    def check_royal_flush(self,hand):
        values = [i[0] for i in hand]
        value1 = ['J', '10', 'Q', 'K', 'A']


        if self.check_straight_flush(hand):
            if set(value1) == set(values):
                return True
            else:
                return False



    def check_straight_flush(self,hand):
        if self.check_flush(hand) and self.check_straight(hand):
            return True
        else:
            return False

    def check_four_of_a_kind(self,hand):
        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if sorted(value_counts.values()) == [1,4]:
            return True
        return False

    def check_full_house(self,hand):
        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if sorted(value_counts.values()) == [2,3]:
            return True
        return False

    def check_flush(self,hand):
        suits = [i[1] for i in hand]
        if len(set(suits))==1:
            return True
        else:
            return False

    def check_straight(self,hand):
        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v] += 1
        rank_values = [self.card_order_dict[i] for i in values]
        value_range = max(rank_values) - min(rank_values)
        if len(set(value_counts.values())) == 1 and (value_range==4):
            return True
        else:
            #check straight with low Ace
            if set(values) == set(["A", "2", "3", "4", "5"]):
                return True
            return False

    def check_three_of_a_kind(self,hand):
        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if set(value_counts.values()) == set([3,1]):

            return True
        else:
            return False

    def check_two_pairs(self,hand):
        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if sorted(value_counts.values())==[1,2,2]:
            return True
        else:
            return False

    def check_one_pairs(self,hand):

        values = [i[0] for i in hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if 2 in value_counts.values():
            return True
        else:
            return False

sys.stdin=open("poker-hands.txt")
P1W=0
P2W=0
for line in sys.stdin:
    cards= line

    cards = list(map(lambda x:x, cards.split()))
    hand = cards[:5]
    deck = cards[5:]
    # print("Hand:", " ".join(hand), "Deck:", " ".join(deck), "Best hand:", play(cards))
    Player = poker()
    P1= Player.check_hand(hand)
    P2= Player.check_hand(deck)


    if P1 > P2:
        P1W += 1

    elif P1 < P2:
        P2W += 1

print("Expected output of provided test file")
print(P1W,P2W)

