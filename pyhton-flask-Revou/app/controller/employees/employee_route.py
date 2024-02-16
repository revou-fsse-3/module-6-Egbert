from flask import Blueprint, jsonify, request
from app.utils.database import db
from app.models.employee import Employee
from app.utils.api_response import api_response
from app.service.employee_service import Employee_Service
from app.controller.employees.schema.update_employee_request import Update_employee_request
from pydantic import ValidationError

employee_blueprint = Blueprint("employee_endpoint", __name__)

@employee_blueprint.route("/", methods=["GET"])
def get_list_employee():
    try:
        employee_service = Employee_Service()

        employees = employee_service.get_employee()

        return api_response(
            status_code=200,
            message="Successfully retrieved list of employees",
            data=employees
        )
    except Exception as e:
        return e, 500

@employee_blueprint.route("/search", methods=["GET"])
def search_employee():
    try:
        request_data = request.args
        employee_service = Employee_Service()

        employees = employee_service.search_employee(request_data["staff"])

        return api_response(
            status_code=200,
            message="",
            data=employees
        )
    except Exception as e:
        return e, 500

@employee_blueprint.route("/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    try:
        employees = Employee.query.get(employee_id)

        if not employees:
            return "Employee not found", 404

        return employees.as_dict(), 200
    except Exception as e:
        return e, 500

@employee_blueprint.route("/", methods=["POST"])
def create_employee():
    try:
        data = request.json
        
        employee = Employee()
        employee.staff = data["staff"]
        employee.role = data["role"]
        employee.schedule = data["schedule"]
        db.session.add(employee)
        db.session.commit()
    
        return "Employee created", 201
    except Exception as e:
        return str(e), 500

@employee_blueprint.route("/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    try:

        data = request.json
        update_employee_request = Update_employee_request(**data)

        employee_service = Employee_Service()

        employees = employee_service.update_employee(employee_id, update_employee_request)

        return api_response(
            status_code=200,
            message="Updated",
            data=employees
        )
    except ValidationError as e:
        return api_response(
            status_code=400,
            message=e.errors(),
            data={}
        )
    except Exception as e:
        return str(e), 500

@employee_blueprint.route("/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)
    try:
        if not employee:
            return "Employee not found", 404

        db.session.delete(employee)
        db.session.commit()

        return "Successfully deleted the employee", 200
    except Exception as e:
        return str(e), 500
