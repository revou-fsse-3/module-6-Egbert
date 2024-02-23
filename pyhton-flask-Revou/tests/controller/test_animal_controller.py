from app import db
from app.service.animal_service import Animal_Service

def test_get_animal(test_app, mocker):
    mock_animal_data = [
        {
            "id": 1,
            "species": "Tiger",
            "age": 10,
            "gender": "Male"
        },
    ]
    mocker.patch.object(Animal_Service, 'get_animal', return_value=mock_animal_data)
    
    # Act
    with test_app.test_client() as client:
        response = client.get("/animal/")

    assert response.status_code == 200
    assert len(response.json['data']) == len(mock_animal_data)
    assert response.json['data'] == mock_animal_data

def test_post_animal(test_app, mocker):
    data = {
        "id": 1,
        "species": "Tiger",
        "age": 10,
        "gender": "Male"
    }
    mocker.patch.object(Animal_Service, 'create_animal', return_value=data)
    
    # Act
    with test_app.test_client() as client:
        response = client.post("/animal/", json=data)

    expected_response = {
        "species": "Tiger",
        "age": 10,
        "gender": "Male"
    }

    assert response.json['data']["species"] == "Tiger"
    assert response.status_code == 201

def test_put_animal(test_app, mocker):
    data = {
        "species": "Tiger",
        "age": 10,
        "gender": "Male"
    }
    mocker.patch.object(Animal_Service, 'update_animal', return_value=data)

    with test_app.test_client() as client:
        response = client.put("/animal/2", json=data)

    assert response.status_code == 200

def test_delete_animal(test_app, mocker):
    expected_response = {
        "species": "Tiger",
        "age": 10,
        "gender": "Male"
    }
    mocker.patch.object(Animal_Service, 'delete_animal', return_value=expected_response)

    with test_app.test_client() as client:
        response = client.delete("/animal/2")

    assert response.status_code == 200


# def test_put_animal_success(test_app):
#     data = {
#         "species": "Elephant",
#         "age": 12,
#         "gender": "Female"
#     }
#     with test_app.test_client() as client:
#         # Act
#         response = client.put("/animal/2", json=data)

#     assert response.status_code == 200

# def test_put_animal_failed(test_app):
#     data = {}
#     with test_app.test_client() as client:
#         # Act
#         response = client.put("/animal/1", json=data)

#     assert response.status_code == 400

# def test_delete_animal_success(test_app):
#     data = {
#         "species": "Panda",
#         "age": 10,
#         "gender": "Male"
#     }
#     with test_app.test_client() as client:
#         # Act
#         response = client.put("/animal/9", json=data)

#     assert response.status_code == 200

# def test_delete_animal_failed(test_app):
#     data = {}
#     with test_app.test_client() as client:
#         # Act
#         response = client.put("/animal/9", json=data)

#     assert response.status_code == 400