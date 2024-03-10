from configuration import app, db
from sqlalchemy import DateTime
from datetime import datetime


class Employee(db.Model):
    __tablename__ = 'EMPLOYEE_MASTER'
    id = db.Column('id', db.Integer, primary_key=True)
    f_name = db.Column('firstname', db.String(30))
    m_name = db.Column('middlename', db.String(30))
    l_name = db.Column('lastname', db.String(30))
    gender = db.Column('gender', db.String(30))
    age = db.Column('age', db.Integer)
    email = db.Column('email', db.String(30))
    photo = db.Column('photo', db.String(30))
    dob = db.Column('dob', db.String(30))
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)


print('tables are created...')
with app.app_context():
    db.create_all()
