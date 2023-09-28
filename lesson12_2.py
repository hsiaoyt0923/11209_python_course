import random

class Player:
    def __init__(self, name:str):
        self.name = name
        self.__dice1 = random.randint(1,6)
        self.__dice2 = random.randint(1,6)
        self.__dice3 = random.randint(1,6)
        self.__dice4 = random.randint(1,6)

    def __play() -> int:
        value=''
        pair = 0
        score_t = 0 
        n = sorted([self.__dice1, self.__dice2, self.__dice3, self.__dice4])
        for x in range(4):
            for j in range(x+1,4) :
                if n[x] == n[j] :
                    t += 1
                    score_t += n[j]
        if pair == 1 :
            value = sum(n)-score_t*2
        elif  pair == 2:
            value = max(n)*2
        elif  pair == 6:
            value = max(n)*100
        else :
            value = 0  
        return value

    @property
    def value(self) -> int:
        #呼叫self.__play()
        pass

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