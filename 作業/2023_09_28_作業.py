import random

class Player:
#attribute
    def __init__(self, name:str):
        self.name = name
#method
    def __play(self):
        score = ''
        while score == '':   
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            dice3 = random.randint(1,6)
            dice4 = random.randint(1,6) 
            D = sorted([dice1, dice2, dice3, dice4])
            if (D[0] == D[1] == D[2] == D[3]):
                if D[0] == 1:
                    score = 13
                if D[0] == 2:
                    score = 14
                if D[0] == 3:
                    score = 15
                if D[0] == 4:
                    score = 16
                if D[0] == 5:
                    score = 17
                if D[0] == 6:
                    score = 18
            elif (D[0] != D[1] != D[2] != D[3]):
                score = ''
            elif (D[0] == D[1] == D[2]) or (D[1] == D[2] == D[3]): 
                score = ''
            else:
                if D[0] == D[1]:
                    score = D[2] + D[3]
                elif D[1] == D[2]:
                    score = D[0] + D[3]
                elif D[2] == D[3]:
                    score = D[0] + D[1] 
        
        return f'骰子一:{dice1}\n骰子二:{dice2}\n骰子三:{dice3}\n骰子四:{dice4}\n得分:{score}'

#property
    @property
    def value(self):
        return self.__play()

#被呼叫時傳出字串
    def __repr__(self) -> str:
        descript = f"姓名:{self.name}"
        return descript

p1 = Player('甲')
print(p1)
print(p1.value)
print()
p2 = Player('乙')
print(p2)
print(p2.value)