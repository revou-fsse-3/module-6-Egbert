from app.models.employee import Employee
from app.utils.database import db

class Employee_Repo():
    def get_list_employee(self):
        employees = Employee.query.all()
        return employees

    def search_employee(self, staff):
        employees = Employee.query.filter(Employee.role.like(f"%{staff}%")).all()
        return employees

    def update_employee(self, id, employee):
        employee_obj = Employee().query.get(id)
        employee_obj.staff = employee.staff
        employee_obj.role = employee.role
        employee_obj.schedule = employee.schedule
        
        db.session.commit()
        return employee_obj