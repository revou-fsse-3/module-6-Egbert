from app.models.animal import Animal
from app.utils.database import db

class Animal_Repo():
    def get_list_animal(self):
        animals = Animal.query.all()
        return animals

    def search_animal(self, species):
        animals = Animal.query.filter(Animal.species.like(f"%{species}%")).all()
        return animals

    def update_animal(self, id, animal):
        animal_obj = Animal().query.get(id)
        animal_obj.species = animal.species
        animal_obj.age = animal.age
        animal_obj.gender = animal.gender
        
        db.session.commit()
        return animal_obj