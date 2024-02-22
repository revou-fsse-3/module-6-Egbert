from app.repositories.animals_repo import Animal_Repo


class Animal_Service:
    def __init__(self):
        self.animal_repo = Animal_Repo()

    def get_animal(self):
        animals = self.animal_repo.get_list_animal()
        return [animal.as_dict() for animal in animals]

    def search_animal(self, species):
        animals = self.animal_repo.search_animal(species)
        return [animal.as_dict() for animal in animals]

    def update_animal(self, id, animal_data_dto):
        update_animal = self.animal_repo.update_animal(id, animal_data_dto)
        return update_animal.as_dict()