

class Dog:
    species = 'canine'
    def __init__(self, name,breed,location):
        self.name = name #can add whatever onto each dog. every dog like this
        self.tricks = []
        self.breed = breed
        self.location = location

    

    def bark(self):
        print(f"{self.name} says BARK!")
    
    def learn_trick(self,new_trick):
        if new_trick not in self.tricks:
            self.tricks.append(new_trick)

    def preform_trick(self,trick):
        if trick in self.tricks:
            print(f"{self.name} preforms {trick}!")
        else:
            print(f"{self.name} does not know {trick}. :( Boo.")

#otter = Dog("Otter",'Husky',"near you!")
jules = Dog("Jules","Corgi","Fresno")
jules.learn_trick('sit')

print(jules.species)


