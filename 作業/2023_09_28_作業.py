import random
class Player:
#attribute
    def __init__(self, name:str):
        self.name = name
        value = ''
        while value == '':
            self.__dice1 = random.randint(1,6)
            self.__dice2 = random.randint(1,6)
            self.__dice3 = random.randint(1,6)
            self.__dice4 = random.randint(1,6)
#method
        def __play(self) -> int:
            D = sorted([self.__dice1, self.__dice2, self.__dice3, self.__dice4])
            if (D[0] == D[1] == D[2] == D[3]):
                if D[0] == 1:
                    value = 13
                if D[0] == 2:
                    value = 14
                if D[0] == 3:
                    value = 15
                if D[0] == 4:
                    value = 16
                if D[0] == 5:
                    value = 17
                if D[0] == 6:
                    value = 18
            elif (D[0] != D[1] != D[2] != D[3]):
                value = ''
            elif (D[0] == D[1] == D[2]) or (D[1] == D[2] == D[3]): 
                value = ''
            else:
                if D[0] == D[1]:
                    value = D[2] + D[3]
                elif D[1] == D[2]:
                    value = D[0] + D[3]
                elif D[2] == D[3]:
                    value = D[0] + D[1] 
        return value
#property
    @property
    def value(self) ->int:
        return self.__play()
    
    def __repr__(self) -> str:
        descript = ""
        descript += f"姓名:{self.name}\n"
        descript += f"骰子1:{self.__dice1}\n"
        descript += f"骰子2:{self.__dice2}\n"
        descript += f"骰子3:{self.__dice3}\n"
        descript += f"骰子4:{self.__dice4}\n"
        dsecript += f"得分:{self.__play()}分"
        return descript

