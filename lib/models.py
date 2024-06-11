from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Association table for many-to-many relationship between Workout and Exercise
association_table = Table('association', Base.metadata,
    Column('workout_id', Integer, ForeignKey('workout.id')),
    Column('exercise_id', Integer, ForeignKey('exercise.id'))
)