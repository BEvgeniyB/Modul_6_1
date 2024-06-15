class Animal:
    fed = False  # (накормленный)
    alive = True  # (живой)

    def __init__(self, nn):
        self.name = nn

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
            self.alive = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
            self.fed = False

class Plant:
    edible = False  #(съедобность),

    def __init__(self, nn):
        self.name = nn


class Mammal(Animal):
   pass


class Predator(Animal):
    pass



class Flower(Plant):
    edible = False


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
#input()
print(a1.alive)
print(a2.fed)
