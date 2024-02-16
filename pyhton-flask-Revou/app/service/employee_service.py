from app.repositories.employee_repo import Employee_Repo


class Employee_Service:
    def __init__(self):
        self.employee_repo = Employee_Repo()

    def get_employee(self):
        employees = self.employee_repo.get_list_employee()
        return [employee.as_dict() for employee in employees]
    
    def search_employee(self, staff):
        employees = self.employee_repo.search_employee(staff)
        return [employee.as_dict() for employee in employees]

    def update_employee(self, id, employee_data_dto):
        update_employee = self.employee_repo.update_employee(id, employee_data_dto)
        return update_employee.as_dict()