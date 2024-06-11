from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Association table for many-to-many relationship between Workout and Exercise
association_table = Table('association', Base.metadata,
    Column('workout_id', Integer, ForeignKey('workout.id')),
    Column('exercise_id', Integer, ForeignKey('exercise.id'))
)

class Workout(Base):
    __tablename__ = 'workout'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    exercises = relationship('Exercise', secondary=association_table, back_populates='workouts')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Workout(id={self.id}, name={self.name})>'

class Exercise(Base):
    __tablename__ = 'exercise'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    sets = Column(Integer, nullable=False)
    reps = Column(Integer, nullable=False)
    workouts = relationship('Workout', secondary=association_table, back_populates='exercises')

    def __init__(self, name, sets, reps):
        self.name = name
        self.sets = sets
        self.reps = reps

    def __repr__(self):
        return f'<Exercise(id={self.id}, name={self.name}, sets={self.sets}, reps={self.reps})>'