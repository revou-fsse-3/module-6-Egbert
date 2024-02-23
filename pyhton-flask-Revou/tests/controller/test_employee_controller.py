from app import db
from app.service.employee_service import Employee_Service

def test_get_employee(test_app, mocker):
    mock_employee_data = [
        {
            "id": 1,
            "role": "Care",
            "schedule": "daily",
            "staff": "Zookeeper"
        },
    ]
    mocker.patch.object(Employee_Service, 'get_employee', return_value=mock_employee_data)
    
    # Act
    with test_app.test_client() as client:
        response = client.get("/employee/")

    assert response.status_code == 200
    assert len(response.json['data']) == len(mock_employee_data)
    assert response.json['data'] == mock_employee_data

def test_post_employee(test_app, mocker):
    data = {
        "id": 1,
        "role": "Care",
        "schedule":"daily",
        "staff": "Male"
    }
    mocker.patch.object(Employee_Service, 'create_employee', return_value=data)
    
    # Act
    with test_app.test_client() as client:
        response = client.post("/employee/", json=data)

    expected_response = {
        "role": "Care",
        "schedule":"daily",
        "staff": "Male"
    }

    assert response.json['data']["role"] == "Care"
    assert response.status_code == 201

def test_put_employee(test_app, mocker):
    data = {
        "role": "Care",
        "schedule":"daily",
        "staff": "Male"
    }
    mocker.patch.object(Employee_Service, 'update_employee', return_value=data)

    with test_app.test_client() as client:
        response = client.put("/employee/2", json=data)

    assert response.status_code == 200

def test_delete_employee(test_app, mocker):
    expected_response = {
        "role": "Care",
        "schedule":"daily",
        "staff": "Male"
    }
    mocker.patch.object(Employee_Service, 'delete_employee', return_value=expected_response)

    with test_app.test_client() as client:
        response = client.delete("/employee/2")

    assert response.status_code == 200

def test_delete_employee_not_found(test_app, mocker):
    expected_response = "Employee not found"
    mocker.patch.object(Employee_Service, 'delete_employee', return_value=expected_response)

    with test_app.test_client() as client:
        response = client.delete("/employee/2")

    assert response.status_code == 404
    assert response.json['data'] == "employee empty"