class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


class SuperDog(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def fly(self):
        print(self.name.title() + " is flying away.")


my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Lucy', 4)
print("Your dog is called " + your_dog.name + " and is " + str(your_dog.age) + " years old")
your_dog.sit()

sup = SuperDog('Ace', 82)
print(sup.name + ' is ' + str(sup.age) + ' years old!!!')
sup.fly()
