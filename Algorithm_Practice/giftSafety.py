def giftSafety(gift):
    if len(gift) < 3:
        return 0
    else:
        for letters in range(len(gift) - 2):
            window = gift[letters:letters + 3]
            window_shuffle_1 = window

gift = 'doll'
giftSafety(gift)
