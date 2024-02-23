from app.controller.employees.schema.create_employee_request import Create_employee_request
from app.models.employee import Employee
from app.service.employee_service import Employee_Service
from app.repositories.employee_repo import Employee_Repo

def test_get_list_employee(test_app, mocker):
    """service get employee success"""

    mock_employee_data = [
        Employee(id=1, role='Care', schedule='daily', staff='Zookeeper'),
        Employee(id=2, role='Medical', schedule='daily', staff='Veterinarian'),
    ]
    mocker.patch.object(Employee_Repo, 'get_list_employee', return_value=mock_employee_data)

    with test_app.test_request_context():
        employee_service = Employee_Service().get_employee()

    assert len(employee_service) == 2
    assert employee_service[0]['role'] == 'Care'
    assert employee_service[1]['staff'] == 'Veterinarian'