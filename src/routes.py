from flask_restful import Resource
from src import db, api
from src.models import SalaryModel


class DatabaseApi(Resource):
    def get(self):
        salary = db.session.query(SalaryModel).all()
        return [i.to_dict() for i in salary], 200


api.add_resource(DatabaseApi, '/database', strict_slashes=False)
