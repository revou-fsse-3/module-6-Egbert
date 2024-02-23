def test_get_animal(test_app):
    with test_app.test_client() as client:
        # Act
        response = client.get("/animal/")

    assert response.status_code == 200