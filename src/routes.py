from flask import request
from flask_restful import Resource
from src import db, api
from src.models import SalaryModel
from datetime import date


class DatabaseApi(Resource):
    def get(self):
        salary = db.session.query(SalaryModel).order_by(SalaryModel.id.asc())
        return [i.to_dict() for i in salary], 200


class Employee(Resource):
    def post(self):
        employee_json = request.json
        try:
            if employee_json['position'] == 1:
                salary = int(employee_json['salary'])
                bonus = int(employee_json['bonus'])
                salary = salary + bonus
            elif employee_json['position'] == 2:
                hours_worked = int(employee_json['hours_worked'])
                overtime = int(employee_json['overtime'])
                hourly_rate = int(employee_json['hourly_rate'])
                salary = (hourly_rate * hours_worked) + (overtime * hourly_rate * 2)
            elif employee_json['position'] == 3:
                salary = int(employee_json['salary'])
                deals = int(employee_json['deals'])
                deal_bonus = int(employee_json['deal_bonus'])
                salary = salary + (deals * deal_bonus)
            salary = SalaryModel(
                name=employee_json['name'],
                position=employee_json['position'],
                salary=salary,
                date=date.today()
            )
            db.session.add(salary)
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': 'Created successfully'}, 200

    def delete(self, id):
        employee = db.session.query(SalaryModel).filter_by(id=id).first()
        db.session.delete(employee)
        db.session.commit()
        return {'message': 'Deleted successfully'}, 204


api.add_resource(DatabaseApi, '/database', strict_slashes=False)
api.add_resource(Employee, '/employee', '/employee/<id>', strict_slashes=False)
