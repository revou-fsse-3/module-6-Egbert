from flask import Blueprint, jsonify, request
from app.utils.database import db
from app.models.animal import Animal
from app.utils.api_response import api_response
from app.service.animal_service import Animal_Service
from app.controller.animals.schema.update_animal_request import Update_animal_request
from pydantic import ValidationError
from app.repositories.animals_repo import Animal_Repo

animal_blueprint = Blueprint("animal_endpoint", __name__)

@animal_blueprint.route("/", methods=["GET"])
def get_list_animal():
    try:
        animal_service = Animal_Service()
        animals = animal_service.get_animal()

        return api_response(
            status_code=200,
            message="Successfully retrieved list of animals",
            data=animals
        )
    except Exception as e:
        return e, 500

@animal_blueprint.route("/search", methods=["GET"])
def search_animal():
    try:
        request_data = request.args
        animal_service = Animal_Service()

        animals = animal_service.search_animal(request_data["species"])

        return api_response(
            status_code=200,
            message="",
            data=animals
        )
    except Exception as e:
        return e, 500

@animal_blueprint.route("/<int:animal_id>", methods=["GET"])
def get_animal(animal_id):
    try:
        animals = Animal.query.get(animal_id)

        if not animals:
            return "Animal not found", 404

        return animals.as_dict(), 200
    except Exception as e:
        return e, 500

@animal_blueprint.route("/", methods=["POST"])
def create_animal():
    try:
        data = request.json
        
        animal = Animal()
        animal.species = data["species"]
        animal.age = data["age"]
        animal.gender = data["gender"]
        db.session.add(animal)
        db.session.commit()
    
        return "Animal created", 201
    except Exception as e:
        return str(e), 500

@animal_blueprint.route("/<int:animal_id>", methods=["PUT"])
def update_animal(animal_id):
    try:

        data = request.json
        update_animal_request = Update_animal_request(**data)

        animal_service = Animal_Service()

        animals = animal_service.update_animal(animal_id, update_animal_request)

        return api_response(
            status_code=200,
            message="Updated",
            data=animals
        )
    except ValidationError as e:
        return api_response(
            status_code=400,
            message=e.errors(),
            data={}
        )
    except Exception as e:
        return str(e), 500

@animal_blueprint.route("/<int:animal_id>", methods=["DELETE"])
def delete_animal(animal_id):
    animal = Animal.query.get(animal_id)
    try:
        if not animal:
            return "Animal not found", 404

        db.session.delete(animal)
        db.session.commit()

        return "Successfully deleted the animal", 200
    except Exception as e:
        return str(e), 500
