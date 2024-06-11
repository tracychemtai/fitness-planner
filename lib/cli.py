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

class Cli():
    def start(self):
        while True:
            os.system("clear")
            print(bold("Welcome to the Fitness Planner! 💪"))
            options = ["Create a new workout", "View workouts", "Delete workout", "Add exercise to workout", "Delete exercise from workout", "Select workout", "Exit"]
            index, selection = display_menu(options)
            print(f"You have selected {selection}!")
            if selection == "Exit":
                break
            else:
                handle_selection(selection)

def handle_selection(selection):
    if selection == "Create a new workout":
        name = input("Enter the name of the new workout (or 'Back' to return to the main menu): ")
        if name.lower() == 'back':
            return
        create_workout(session, name)
    elif selection == "View workouts":
        workouts = get_all_workouts(session)
        print("Existing workouts:")
        for workout in workouts:
            print(f"ID: {workout.id}, Name: {workout.name}")
        input("Press Enter to return to the main menu...")
    elif selection == "Delete workout":
        workouts = get_all_workouts(session)
        print("Existing workouts:")
        for workout in workouts:
            print(f"ID: {workout.id}, Name: {workout.name}")
        workout_id = input("Enter the ID of the workout you want to delete (or 'Back' to return to the main menu): ")
        if workout_id.lower() == 'back':
            return
        try:
            workout_id = int(workout_id)
            session.query(Workout).filter(Workout.id == workout_id).delete()
            session.commit()
        except ValueError:
            print("Invalid input. Please enter a valid workout ID or 'Back'.")
    elif selection == "Add exercise to workout":
        workout = select_workout(session)
        if workout:
            exercise_name = input("Enter the exercise name (or 'Back' to return to the main menu): ")
            if exercise_name.lower() == 'back':
                return
            sets = input("Enter the number of sets (or 'Back' to return to the main menu): ")
            if sets.lower() == 'back':
                return
            reps = input("Enter the number of reps (or 'Back' to return to the main menu): ")
            if reps.lower() == 'back':
                return
            try:
                sets = int(sets)
                reps = int(reps)
                add_exercise_to_workout(session, workout, exercise_name, sets, reps)
            except ValueError:
                print("Invalid input. Please enter valid values or 'Back'.")
    elif selection == "Delete exercise from workout":
        workout = select_workout(session)
        if workout:
            print("Exercises in the selected workout:")
            for exercise in workout.exercises:
                print(f"ID: {exercise.id}, Name: {exercise.name}")
            exercise_id = input("Enter the ID of the exercise to delete (or 'Back' to return to the main menu): ")
            if exercise_id.lower() == 'back':
                return
            try:
                exercise_id = int(exercise_id)
                delete_exercise_from_workout(session, workout, exercise_id)
            except ValueError:
                print("Invalid input. Please enter a valid exercise ID or 'Back'.")
    elif selection == "Select workout":
        workouts = get_all_workouts(session)
        print("Existing workouts:")
        for workout in workouts:
            print(f"ID: {workout.id}, Name: {workout.name}")
        workout_id = input("Enter the ID of the workout to view exercises (or 'Back' to return to the main menu): ")
        if workout_id.lower() == 'back':
            return
        try:
            workout_id = int(workout_id)
            workout = session.get(Workout, workout_id)
            if workout:
                print("Exercises in the selected workout:")
                for exercise in workout.exercises:
                    print(f"ID: {exercise.id}, Name: {exercise.name}, Sets: {exercise.sets}, Reps: {exercise.reps}")
                input("Press Enter to return to the main menu...")
            else:
                print("Workout not found.")
        except ValueError:
            print("Invalid input. Please enter a valid workout ID or 'Back'.")
    else:
        exit_program()

if __name__ == "__main__":
    app = Cli()
    app.start()

