from db import *

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/Add_Student',methods = ['GET','POST'])
def add_student():
    form = Add_Student()

    if form.validate_on_submit():
        print('hi')
        usn = form.usn.data
        name = form.name.data
        age = form.age.data
        news = Student(usn,name,age)
        db.session.add(news)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('adds.html',form = form)

@app.route('/Add_Teacher',methods = ['GET','POST'])
def add_teacher():
    form = Add_Teacher()
    if form.validate_on_submit():
        ssn = form.ssn.data
        name = form.name.data
        exp = form.exp.data
        salary = form.salary.data
        newt = Teacher(ssn,name,exp,salary)
        db.session.add(newt)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('addt.html',form = form)

@app.route('/Del_Student',methods = ['GET','POST'])
def del_student():
    form = Del_Student()
    if form.validate_on_submit():
        usn = form.usn.data
        news = Student.query.get(usn)
        db.session.delete(news)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('dels.html',form = form)

@app.route('/Del_Teacher',methods = ['GET','POST'])
def del_teacher():
    form = Del_Teacher()
    if form.validate_on_submit():
        ssn = form.ssn.data
        newt = Teacher.query.get(ssn)
        db.session.delete(newt)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('delt.html',form = form)

@app.route('/List')
def list():
    student = Student.query.all()
    teacher = Teacher.query.all()
    return render_template('list.html',Student = student,Teacher = teacher)



if __name__ == '__main__':
    app.run(debug = True)
