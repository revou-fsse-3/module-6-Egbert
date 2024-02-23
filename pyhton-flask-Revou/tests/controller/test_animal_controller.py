def test_get_animal(test_app):
    response = test_app.get("/animal/")
    assert response.status_code == 200