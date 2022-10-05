

class Man:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class Pet:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def __str__(self):
        return self.name


man = Man('Max')
pet = Pet('Crocker', man)

man.name = 'Alex'
print(man)
print(pet)
