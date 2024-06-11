# cli.py
import os
from helpers import (
    get_session, create_workout, get_all_workouts,
    add_exercise_to_workout, delete_exercise_from_workout,
    select_workout, display_menu, exit_program
)
from models import Base
from sqlalchemy import create_engine, func
from prettycli import red, bold
from simple_term_menu import TerminalMenu
from models import Base, Workout, Exercise, association_table
from sqlalchemy.orm import sessionmaker

# Initialize the database session
engine = create_engine('sqlite:///fitness_data.db')
Base.metadata.create_all(engine)
session = get_session(engine)

def get_lowest_available_id(session, model):
    # Find the highest existing ID in the table
    highest_id = session.query(func.max(model.id)).scalar()
    if highest_id is None:
        return 1
    
     # Create a set of all existing IDs
    existing_ids = set(row[0] for row in session.query(model.id).all())
    
    # Find the lowest available ID
    for id in range(1, highest_id + 1):
        if id not in existing_ids:
            return id
    
    # If all IDs from 1 to highest_id are taken, return the next highest ID
    return highest_id + 1

def add_exercise_to_workout(session, workout, name, sets, reps):
    # Get the lowest available ID for the Exercise model
    lowest_available_id = get_lowest_available_id(session, Exercise)
    
    # Create the new exercise without specifying the ID
    new_exercise = Exercise(name=name, sets=sets, reps=reps)
    
    # Associate the new exercise with the workout
    workout.exercises.append(new_exercise)
    
    # Add and commit the new exercise to the session
    session.add(new_exercise)
    session.commit()