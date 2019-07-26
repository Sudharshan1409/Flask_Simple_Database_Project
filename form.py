from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,FloatField

class Add_Student(FlaskForm):
    usn = StringField('USN : ')
    name = StringField('Name : ')
    age = IntegerField('Age : ')
    submit = SubmitField('Submit')

class Add_Teacher(FlaskForm):
    ssn = StringField('SSN : ')
    name = StringField('Name : ')
    exp = IntegerField('Experience : ')
    salary = FloatField('Salary : ')
    submit = SubmitField('Submit')

class Del_Student(FlaskForm):
    usn = StringField('USN : ')
    submit = SubmitField('Submit')

class Del_Teacher(FlaskForm):
    ssn = StringField('SSN : ')
    submit = SubmitField('Submit')
