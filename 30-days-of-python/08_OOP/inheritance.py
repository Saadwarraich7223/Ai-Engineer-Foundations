class Animal:
    def __init__(self,name,age , weight,food):
        self.name=name
        self.age=age
        self.weight=weight
        self.food=food
    def eat(self):
        print(f"{self.name} eats {self.food}")  
    def sleeps(self):
        print(f"{self.name} sleeps ")  
    def make_sound(self):
        print(f"{self.name} makes sound ") 
     
    
        
class Dog(Animal):
    def __init__(self, name,age,breed,weight,food):
        self.breed=breed
        super().__init__(name,age,weight,food)
    def fetches_ball(self):
        print(f"{self.name} fetches ball.")
    def about(self):
        print(f"{self.name} is a {self.breed}")
    def make_sound(self):
        print(f"{self.name} says woof woof")
        
class Cat(Animal):
    def __init__(self,name,age,weight,food,lives):
        self.lives=lives
        super().__init__(name,age,weight,food)
    def lives_left(self):
        print(f"{self.name} has {self.lives} lives left.")
    def climbs(self):
        print(f"{self.name} climbs walls and trees")
        
  
    
    
animals=[
    Dog('jim',4,"golden retrival",'20kg',"Bone"),
    Cat('TIm',4,'20kg',"Cat Food",9)
    
]

for animal in animals:
    animal.eat()
    animal.sleeps()
    animal.make_sound()
    
    
jim=Dog('jim',4,"golden retrival",'20kg',"Bone")
jim.sleeps()
jim.eat()
jim.fetches_ball()
jim.about()
jim.make_sound()


tim=Cat('TIm',4,'20kg',"Cat Food",9)
tim.sleeps()
tim.eat()
tim.climbs()
tim.lives_left()