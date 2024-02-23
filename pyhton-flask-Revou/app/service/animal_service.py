from app.repositories.animals_repo import Animal_Repo
from app.models.animal import Animal


class Animal_Service:
    def __init__(self):
        self.animal_repo = Animal_Repo()

    def get_animal(self):
        animals = self.animal_repo.get_list_animal()
        return [animal.as_dict() for animal in animals]

    def search_animal(self, species):
        animals = self.animal_repo.search_animal(species)
        return [animal.as_dict() for animal in animals]

    def create_animal(self, species):
        animal = Animal()

        animal.species = animal_data_dto.name
        animal.age = animal_data_dto.age
        animal.gender = animal_data_dto.gender
        
        create_animal = self.animal_repo.create_animal(animal)
        return create_animal.as_dict()

    def update_animal(self, id, animal_data_dto):
        update_animal = self.animal_repo.update_animal(id, animal_data_dto)
        return update_animal.as_dict()
    
    def delete_animal(self, id):
        animal = Animal.query.get(id)
        if not animal:
            return "Animal not found"
        
        deleted_animal = self.animal_repo.delete_animal(id)
        return deleted_animal.as_dict()