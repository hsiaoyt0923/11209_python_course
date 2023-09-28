class Person:
#attribute
    def __init__(self,n:str, weight:int, height:int):
        self.__name = n
        self.weight = weight
        self.height = height

#property
    @property
    def name(self) -> str: 
        return self.__name
    
    @property
    def getBMI(self) -> float:
        return self.bmi()


    def __str__(self) -> str:
        return f'name:{self.__name}\nweight:{self.weight}\nheight:{self.height}'

#method       
    def bmi(self):
        return round(self.weight / (self.height*0.01)**2, ndigits=2)


# __name__指這份文件；__main__是預設名稱
if __name__ == '__main__':
    p1 = Person('Eddie',60,175)
    print(p1.name)
    print('BMI:',p1.getBMI)