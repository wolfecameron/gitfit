'''
This file contains all tables for the gitfit database 
GitFit uses a SQLAlchemy database so all tables inherit 
from the Model class inside of sqlalchemy
'''
from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy.types import Column, Integer, String


'''
this class creates the user table for the gitfit database
it inherits from the general SQLAlchemy model class
'''
class User(Model):
	id = Column(Integer, primary_key = True)
	username = Column(String(20), unique = True)
	email = Column(String(50), unqiue = True)
	password = Column(String(80))




