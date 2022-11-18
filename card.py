from utils import row_number
import random

class card:
    # 背面：畫有1-6個起司洞，各六張
    # 正面：18張起司卡以及18張陷阱卡
    def __init__(self):
        # initial 36's cards
        self.front_cardnum = 0
        self.back_cardnum = 36
        # queue(front, back)
        self.card = []
        self.card_ontop = []
    def _get_backcard(self, range):
        return row_number(min(range), max(range))
    def _get_back_range(self, back_status):
        key_list = []
        for i in range(len(back_status)):
            if back_status[i] > 0:
                key_list += [i]
        return key_list
    def draw_card(self, num):
        for _ in range(num):
            if self.card:
                self.card_ontop.append(self.card[0])
                self.card.pop(0)
    def initial_card(self):
        # 1~6為背面點數(1~6) 
        # 0,1為正面卡面(起司卡或陷阱卡)
        front_status = {1:6, 2:6, 3:6, 4:6, 5:6, 6:6}
        back_status = {0:18, 1:18}
        # front
        for key in front_status:
            for _ in range(front_status[key]):
                num = self._get_backcard(self._get_back_range(back_status))
                back_status[num] -= 1
                self.card.append([key, num])
        for _ in range(3):
            random.shuffle(self.card)
        self.draw_card(6)
