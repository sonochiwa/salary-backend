from sqlalchemy import delete, asc

from datetime import date

from src import db, app
from src.models import SalaryModel


def employees():
    # sql_session_1 = SalaryModel(
    #     name='Creep Fishman',
    #     position=1,
    #     salary=45000,
    #     date=date(2022, 10, 27),
    # )
    #
    # sql_session_2 = SalaryModel(
    #     name='Ryan Gosling',
    #     position=2,
    #     salary=35000,
    #     date=date(2022, 10, 27),
    # )
    #
    # sql_session_3 = SalaryModel(
    #     name='John Wick',
    #     position=3,
    #     salary=150000,
    #     date=date(2022, 10, 27),
    # )

    # db.session.add(sql_session_1)
    # db.session.add(sql_session_2)
    # db.session.add(sql_session_3)
    # sql1 = delete(SalaryModel).where(SalaryModel.id == 2)

    # db.session.query(SalaryModel).filter(SalaryModel.id).order_by(asc(SalaryModel.id)).all()

    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    with app.app_context():
        employees()
