import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    # 两个类变量
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        # 类变量引用时，不加self也可以
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        # 两重循环，相当于ranks这个是内层循环

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__=="__main__":
    deck = FrenchDeck()
    print(len(deck))
    print(deck[34])
    # print(f._cards)
    # 随机抽取
    from random import choice
    print(choice(deck))
    # 支持切片
    print(deck[10:14:2])
    # 可迭代
    for card in deck:
        print(card)
        break
    # 反向迭代
    for card in reversed(deck):
        print(card)
        break
    # 排序
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank) 
        return rank_value * len(suit_values) + suit_values[card.suit]
    for card in sorted(deck, key=spades_high):
        print(card)
        break