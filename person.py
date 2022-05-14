
class Person:
    def __init__(self, name, age):
        if not name or type(name) is not str:
            raise ValueError("Missing name!")
        """ if isinstance(age, int): """
        if not str(age).isdigit():
            raise ValueError("Age is not an integer")
        elif int(age) < 18 or int(age) > 130:
            raise ValueError("Age must be between 18 and 130.")
        self.name = name
        self.age = age
        
    @property
    def name(self):
        print(">> Returning name")
        return self._name 
    
    @name.setter
    def name(self, name):
        self._name = name
    
    def __str__(self):
        print(f"{self.name} {self.age}")
        """  print(f"{self._name} {self.age}") """
    
    """ Same for all objects/instances """  
    @classmethod      
    def print_hey(self):
        print("Hey!")
        
    @classmethod
    def get(cls):
        return cls("cls_name", 22)

def main():
    person = Person(input("Name? "), input("Age? "))  
    person.__str__() 
    Person.print_hey()
    person2 = Person.get()
    print(person2.name + " " + str(person2.age))
    print(f"{person2.name} {person2.age}")
        
if __name__ == "__main__":
    main()
        
    
    
    