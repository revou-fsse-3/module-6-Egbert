def test_get_all_list_animal(test_app, mocker):
    with test_app.test_client() as client:
        # Act
        response = client.get("/animal/")

    assert len(response.json['data']) == 5


def test_put_animal_success(test_app):
    data = {
        "species": "Elephant",
        "age": 12,
        "gender": "Female"
    }
    with test_app.test_client() as client:
        # Act
        response = client.put("/animal/2", json=data)

    assert response.status_code == 200

def test_put_animal_failed(test_app):
    data = {}
    with test_app.test_client() as client:
        # Act
        response = client.put("/animal/1", json=data)

    assert response.status_code == 400

def test_delete_animal_success(test_app):
    data = {
        "species": "Panda",
        "age": 10,
        "gender": "Male"
    }
    with test_app.test_client() as client:
        # Act
        response = client.put("/animal/9", json=data)

    assert response.status_code == 200

def test_delete_animal_failed(test_app):
    data = {}
    with test_app.test_client() as client:
        # Act
        response = client.put("/animal/9", json=data)

    assert response.status_code == 400