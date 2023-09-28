import random

class Player:
    def __init__(self, name:str):
        self.name = name
        self.__dice1 = random.randint(1,6)
        self.__dice2 = random.randint(1,6)
        self.__dice3 = random.randint(1,6)
        self.__dice4 = random.randint(1,6)

    def __play() -> int:
        value = 0
        pair = 0
        value_t = 0 
        n = sorted([self.__dice1, self.__dice2, self.__dice3, self.__dice4])
        while value == 0:
            for x in range(4):
                for j in range(x+1,4) :
                    if n[x] == n[j] :
                        pair += 1
                        value_t += n[j]
            if pair == 1 :
                value = sum(n)-value_t*2
            elif  pair == 2:
                value = max(n)*2
            else:
                if pair == 6 and self.__dice1 == 1:
                    value = 13
                if pair == 6 and self.__dice1 == 2:
                    value = 14
                if pair == 6 and self.__dice1 == 3:
                    value = 15
                if pair == 6 and self.__dice1 == 4:
                    value = 16
                if pair == 6 and self.__dice1 == 5:
                    value = 17
                if pair == 6 and self.__dice1 == 6:
                    value = 18
                else :
                    value = 0  
        return value

    @property
    def value(self) -> int:
        self.__play()

    def __repr__(self) -> str:
        descript = ""
        descript += "徐國堂\n"
        descript += f"骰子1:{self.__dice1}\n"
        descript += f"骰子2:{self.__dice2}\n"
        descript += f"骰子3:{self.__dice3}\n"
        descript += f"骰子4:{self.__dice4}\n"
        dsecript += f"得分:{value}分"
        return descript
    
if __name__ == "__main__":
    p1 = Player("robert")
    print(p1.value)
    print(p1)

    p2 = Player("robert")
    print(p2.value)
    print(p2)