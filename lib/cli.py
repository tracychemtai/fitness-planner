import os
from helpers import (
    get_session, create_workout, get_all_workouts, 
    add_exercise_to_workout, delete_exercise_from_workout, 
    select_workout, display_menu, exit_program
)
from models import Base
from sqlalchemy import create_engine
from ipdb import set_trace
from prettycli import red, bold
from simple_term_menu import TerminalMenu
from models import Base, Workout, Exercise, association_table 
from sqlalchemy.orm import sessionmaker
import os

# Initialize the database session
engine = create_engine('sqlite:///fitness_data.db')
Base.metadata.create_all(engine)
session = get_session(engine)

class Cli():
    def start(self):
        os.system("clear")
        print(bold("Welcome to the Fitness Planner! 💪"))
        options = ["Create a new workout", "View existing workouts", "Delete workout", "Add exercise to workout", "Delete exercise from workout", "Select workout", "exit"]
        index, selection = display_menu(options)
        print(f"You have selected {selection}!")
        return selection
