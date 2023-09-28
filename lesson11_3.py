class Person:
    def __init__(self,name:str, weight:int, height:int):
        self.name = name
        self.weight = weight
        self.height = height

    def __str__(self):
        return f'name:{self.name}\nweight:{self.weight}\nheight:{self.height}'

if __name__ == '__main__':
    p1 = Person('Eddie',26,175)
    print(p1)