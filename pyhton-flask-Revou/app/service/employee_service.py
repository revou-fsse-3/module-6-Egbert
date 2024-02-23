from app.repositories.employee_repo import Employee_Repo
from app.models.employee import Employee


class Employee_Service:
    def __init__(self):
        self.employee_repo = Employee_Repo()

    def get_employee(self):
        employees = self.employee_repo.get_list_employee()
        return [employee.as_dict() for employee in employees]

    def search_employee(self, role):
        employees = self.employee_repo.search_employee(role)
        return [employee.as_dict() for employee in employees]

    def create_employee(self, role):
        employee = Employee()

        employee.role = employee_data_dto.role
        employee.schedule = employee_data_dto.schedule
        employee.staff = employee_data_dto.staff
        
        create_employee = self.employee_repo.create_employee(employee)
        return create_employee.as_dict()

    def update_employee(self, id, employee_data_dto):
        update_employee = self.employee_repo.update_employee(id, employee_data_dto)
        return update_employee.as_dict()
    
    def delete_employee(self, id):
        employee = Employee.query.get(id)
        if not employee:
            return "Employee not found"
        
        deleted_employee = self.employee_repo.delete_employee(id)
        return deleted_employee.as_dict()