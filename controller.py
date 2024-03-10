from configuration import app, db
from flask import request, render_template
from models import Employee


@app.route('/employee/')
@app.route('/employee/index')
@app.route('/')
@app.route('/index')
@app.route('/employee')
def welocome_page():
    return render_template('index.html')


@app.route('/employee/save', methods=['GET', 'POST'])
def save_employee():
    # formdata = request.args          #---->GET METHOD DATA
    # print(formdata)
    message = ''
    if request.method == 'POST':
        formdata = request.form  # ---->POST METHOD DATA


        email = formdata.get('empmail')
        if len(email)<10:
            message = "Invalid email Address...!"
            return render_template('add.html', error=message)   # ye message add me bhejna hota hai

        print(formdata)
        emp = Employee(f_name=formdata.get('empfnm'),
                       m_name=formdata.get('empmnm'),
                       l_name=formdata.get('emplnm'),
                       gender=formdata.get('gender'),
                       age=formdata.get('empage'),
                       email=formdata.get('empmail'),
                       photo=formdata.get('empphoto'),
                       dob=formdata.get('empdob'))
        with app.app_context():
            db.session.add(emp)
            db.session.commit()
            message = "Employee Saved Successfully...!"
    return render_template('add.html', result=message)


@app.route('/employee/save1', methods=['GET', 'POST'])
def save_employee1():
    # formdata = request.args          #---->GET METHOD DATA
    # print(formdata)
    message = ''
    if request.method == 'POST':
        formdata = request.form  # ---->POST METHOD DATA
        print('formdata', formdata)


        name = formdata.get('empfnm')
        skills1 = formdata.getlist('skills1')
        skills2 = formdata.getlist('skills3')
        print(name)
        print(skills1)
        print(skills2)

    return render_template('add.html')


@app.route('/employee/update', methods=['GET', 'POST'])
def update_employee():
    formdata = request.form
    empid = formdata.get('empid')
    emp = Employee.query.filter_by(id=empid).first()
    emp.f_name = formdata.get('empfnm')
    emp.m_name = formdata.get('empmnm')
    emp.l_name = formdata.get('emplnm')
    emp.gender = formdata.get('gender')
    emp.age = formdata.get('empage')
    emp.email = formdata.get('empmail')
    emp.photo = formdata.get('empphoto')
    emp.dob = formdata.get('empdob')
    db.session.commit()
    emp_list = Employee.query.all()
    return render_template('list.html', result_list=emp_list)


@app.route('/emp/edit/<int:empid>')
def edit_employee(empid):
    emprecord = Employee.query.filter_by(id=empid).first()
    return render_template('update.html', employee=emprecord)


@app.route('/emp/delete/<int:empid>')
def delete_employee(empid):
    emprecord = Employee.query.filter_by(id=empid).first()
    if emprecord:
        #with app.app_context():
        db.session.delete(emprecord)
        #emprecord.is_deleted = 'Y' ---> this use for the soft delete but column should be present in db
        db.session.commit()

    emp_list = Employee.query.all()
    return render_template('list.html', result_list=emp_list)


@app.route('/employee/list')
def list_of_employee():
    emp_list = Employee.query.all()

    return render_template('list.html', result_list=emp_list)


@app.route('/employee/photo', methods=['GET', 'POST'])
def upload_file():
    error = ('')
    if request.method == 'POST':
        formdata = request.form
        name = formdata.get('emp_name')# for html components
        print('name', name)
        form_multimedia = request.files      #for multimedia content
        print(form_multimedia)
        file = form_multimedia.get('emp_dp')

        print(file.filename)

        filename = file.filename
        if filename.split('.')[-1] in ['.png', '.jpeg']:
            file.save(filename)
        else:
            error = "Invalid File Type"
        #file.save(f"{name}.png")
    return render_template('upload_multimedia.html', error = error)

if __name__ == '__main__':
    app.run(debug=True)
