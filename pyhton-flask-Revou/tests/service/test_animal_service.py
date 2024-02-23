from app.controller.animals.schema.create_animal_request import Create_animal_request
from app.models.animal import Animal
from app.service.animal_service import Animal_Service
from app.repositories.animals_repo import Animal_Repo

def test_get_list_animal(test_app, mocker):
    """service get animal success"""

    mock_animal_data = [
        Animal(id=1, species='Tiger', age=10, gender='Male'),
        Animal(id=2, species='Panda', age=12, gender='Female'),
    ]
    mocker.patch.object(Animal_Repo, 'get_list_animal', return_value=mock_animal_data)

    with test_app.test_request_context():
        animal_service = Animal_Service().get_animal()

    assert len(animal_service) == 2
    assert animal_service[0]['species'] == 'Tiger'
    assert animal_service[1]['gender'] == 'Female'