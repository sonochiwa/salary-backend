from src import db


class SalaryModel(db.Model):
    __tablename__ = 'salary'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    position = db.Column(db.Integer, nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __init__(self, name, position, salary, date):
        self.name = name
        self.position = position
        self.salary = salary
        self.date = date

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'position': self.position,
            'salary': self.salary,
            'date': self.date.strftime('%Y-%m-%d'),
        }