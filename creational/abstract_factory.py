import random

class PetShop:
    ''' A pet shop '''
    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory()
        print('We have a lovely {}'.format(pet))
        print('It says {}'.format(pet.speak()))

class Dog:
    def speak(self):
        return 'woof'

    def __str__(self):
        return 'Dog'


class Cat:
    def speak(self):
        return 'meow'

    def __str__(self):
        return 'Cat'

def random_animal():
    return random.choice([Dog, Cat])()


if __name__ == '__main__':
    cat_shop = PetShop(Cat)
    cat_shop.show_pet()
    print('')

    shop = PetShop(random_animal)
    for _ in range(3):
        shop.show_pet()
        print('=' * 20)

### OUTPUT ###
# We have a lovely Cat
# It says meow

# We have a lovely Dog
# It says woof
# ====================
# We have a lovely Cat
# It says meow
# ====================
# We have a lovely Cat
# It says meow
# ====================