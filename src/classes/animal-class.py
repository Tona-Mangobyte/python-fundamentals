from dataclasses import dataclass

@dataclass
class AnimalClass:
    name: str
    habitat: str
    teeth: int = 0

animal = AnimalClass('lion', 'savannah', 30)
print(animal) # Output: AnimalClass(name='lion', habitat='savannah', teeth=30)
duck = AnimalClass(habitat='lake', name='duck')
print(duck) # Output: AnimalClass(name='duck', habitat='lake', teeth=0)
