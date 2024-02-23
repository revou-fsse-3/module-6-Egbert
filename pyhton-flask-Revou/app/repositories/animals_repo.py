from app.models.animal import Animal
from app.utils.database import db

class Animal_Repo():
    def get_list_animal(self):
        animals = Animal.query.all()
        return animals
    
    def create_animal(self, animal):
        db.session.add(animal)
        db.session.commit()
        return animal

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

    def delete_animal(self, id):
        animal_obj = Animal.query.get(id)

        db.session.delete(animal)
        db.session.commit()
        return animal_obj