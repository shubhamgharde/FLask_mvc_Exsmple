


#
# envivorment careation from path folder
# adreess me jakar CMD open karna hai
# --pip install virtualenv
# --virtualenv venv
# --venv\Scripts\activate
# --pip install flask
# --pip install pymysql
# --pip install flask-sqlalchemy
#
# database queries-->
# --create databse (name);
# --drop database (name);
# --use db name;
# --show tables;
# --desc employee;
# --select * from employee;
#











from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@localhost/flaskk_db'
db = SQLAlchemy(app)

#db -->instance of a SQLALCHEMY --> FLASK --> FLASK-DATABASE CONNACTION..

class Employee(db.Model):
    id = db.Column('emp_id',db.Integer(),primary_key=True)
    name = db.Column('emp_name',db.String(40))
    email = db.Column('emp_email',db.String(40),unique=True)
    salary = db.Column('emp_salary',db.Float())
    role = db.Column('emp_role',db.String(40))


#create table--->
with app.app_context():
    db.create_all()

#insert single
e1 = Employee(id=101,name='AAA',email='abc@gmail.com',salary=28333.45,role='SSE')
with app.app_context():
    db.session.add(e1)
    db.session.commit()

#bulk_insert
e2 = Employee(id=102,name='AAA1',email='abc1@gmail.com',salary=58333.45,role='SSE')
e3 = Employee(id=103,name='AAA2',email='abc2@gmail.com',salary=26333.45,role='SE')
e4 = Employee(id=104,name='AAA3',email='abc3@gmail.com',salary=77333.45,role='Manager')
with app.app_context():
    db.session.add_all([e2,e3,e4])
    db.session.commit()

#retrive karne ke liye SELECT QUERY HOTI HAI
emp1 = Employee.query.filter_by(id=101).first()
print(emp1)

emplist = Employee.query.all()
print(emplist)

#delete

emp2 = Employee.query.filter_by(id=102).first()
if emp2:
    db.session.delete(emp2)
    with app.app_context():
        db.session.commit()

#update
emp3 = Employee.query.filter_by(id=103).first()
if emp3:
    emp3.name = 'Shubham'
    with app.app_context():
        db.session.commit()

