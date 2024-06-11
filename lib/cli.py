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
    