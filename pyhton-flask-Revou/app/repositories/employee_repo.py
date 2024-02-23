from app.models.employee import Employee
from app.utils.database import db

class Employee_Repo():
    def get_list_employee(self):
        employees = Employee.query.all()
        return employees
    
    def create_employee(self, employee):
        db.session.add(employee)
        db.session.commit()
        return employee

    def search_employee(self, role):
        employees = Employee.query.filter(Employee.role.like(f"%{role}%")).all()
        return employees

    def update_employee(self, id, employee):
        employee_obj = Employee().query.get(id)
        employee_obj.role = employee.role
        employee_obj.schedule = employee.schedule
        employee_obj.staff = employee.staff
        
        db.session.commit()
        return employee_obj

    def delete_employee(self, id):
        employee_obj = Employee.query.get(id)

        db.session.delete(employee)
        db.session.commit()
        return employee_obj