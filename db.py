import os
from form import *
from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

###DATABASE SECTION###

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Student(db.Model):

    __tablename__ = 'Student'
    usn = db.Column(db.Text,primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self,usn,name,age):
        self.usn = usn
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student USN : {self.usn}, Student Name : {self.name}, Student Age : {self.age}"
class Teacher(db.Model):

    ssn = db.Column(db.Text,primary_key = True)
    name = db.Column(db.Text)
    exp = db.Column(db.Integer)
    salary = db.Column(db.Float)

    def __init__(self,ssn,name,exp,salary):
        self.ssn = ssn
        self.name = name
        self.exp = exp
        self.salary = salary

    def __repr__(self):
        return f"Teacher SSN : {self.ssn}, Teacher Name : {self.name}, Teacher Experience : {self.exp}, Teacher Salary : {self.salary}"
