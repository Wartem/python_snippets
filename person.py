class Person:
    """ This class is a test representation of a person.
    Reminders to self:
    Check Pylint for clean code.
    pycodestyle auto formats code
    Black auto formats code"""

    SPECIES = "Human"

    def __init__(self, name, age):
        if not name or not isinstance(name, str):
            raise ValueError("Missing name!")
        if not str(age).isdigit():
            raise ValueError("Age is not an integer")
        if int(age) < 18 or int(age) > 130:
            raise ValueError("Age must be between 18 and 130.")
        self._name = name
        self._age = age

    @property
    def name(self):
        print("     >> Returning name")
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        print("     >> Returning age")
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def __str__(self):
        return f"{self.name} {self.age}"

    """ Same for all objects/instances """

    @classmethod
    def print_hey(cls):
        print("Hey!", cls.SPECIES)

    @classmethod
    def get(cls):
        return cls("cls_name", 22)


class King(Person):
    def __init__(self, name, age, country):
        super().__init__(name, age)
        self.country = country

    def __str__(self):
        return super().__str__() + " " + self.country


def main():
    person = Person(input("Name? "), input("Age? "))
    print("String test", person.__str__())
    Person.print_hey()
    person2 = Person.get()
    print(person2.name + " " + str(person2.age))
    print(f"{person2.name} {person2.age}")
    king = King("Karl", 76, "Sweden")
    print(king.name + " " + str(king.age) + " " + king.country)
    print(king.__str__())


if __name__ == "__main__":
    main()
