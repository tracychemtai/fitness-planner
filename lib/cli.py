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


    def handle_selection(selection):
    if selection == "Create a new workout":
        name = input("Enter the name of the new workout: ")
        create_workout(session, name)
    elif selection == "View existing workouts":
        workouts = get_all_workouts(session)
        print(workouts)
    elif selection == "Delete workout":
        workouts = get_all_workouts(session)
        print(workouts)
        workout_id = int(input("Enter the ID of the workout you want to delete: "))
        session.query(Workout).filter(Workout.id == workout_id).delete()
        session.commit()
    elif selection == "Add exercise to workout":
        workout = select_workout(session)
        if workout:
            exercise_name = input("Enter the exercise name: ")
            sets = int(input("Enter the number of sets: "))
            reps = int(input("Enter the number of reps: "))
            add_exercise_to_workout(session, workout, exercise_name, sets, reps)
    elif selection == "Delete exercise from workout":
        workout = select_workout(session)
        if workout:
            exercise_id = int(input("Enter the ID of the exercise to delete: "))
            delete_exercise_from_workout(session, workout, exercise_id)
    elif selection == "Select workout":
        workout = select_workout(session)
        if workout:
            print(workout.exercises)
    else:
        exit_program()

if __name__ == "__main__":
    

    app = Cli()
    selection = app.start()
    handle_selection(selection)
