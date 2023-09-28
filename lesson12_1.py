class Person:
#attribute
    def __init__(self,name:str, weight:int, height:int):                         
        self.__name = name
        self.weight = weight
        self.height = height

    def __str__(self): 
        return f'name:{self.__name}\nweight:{self.weight}\nheight:{self.height}'
#method       
    def bmi(self):                                                               
        return round(self.weight / (self.height*0.01)**2, ndigits=2)


if __name__ == '__main__':
    p1 = Person('Eddie',60,175)
    print(p1)
    print('BMI:',p1.bmi())