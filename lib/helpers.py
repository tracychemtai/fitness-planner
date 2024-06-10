from models import Workout, Exercise, association_table
from sqlalchemy.orm import sessionmaker
from prettycli import bold
from simple_term_menu import TerminalMenu
import os

#initial configuration for SQLAlchemy
def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()

# data base operation function
def create_workout(session, name):
    workout = Workout(name=name)
    session.add(workout)
    session.commit()
    return workout

def get_all_workouts(session):
    return session.query(Workout).all()

def get_workout_by_id(session, workout_id):
    return session.query(Workout).filter(Workout.id == workout_id).first()

def delete_workout(session, workout_id):
    workout = get_workout_by_id(session, workout_id)
    if workout:
        session.delete(workout)
        session.commit()
        
    


def add_exercise_to_workout(session, workout, exercise_name, sets, reps):
    exercise = Exercise(name=exercise_name, sets=sets, reps=reps)
    workout.exercises.append(exercise)
    session.commit()

def delete_exercise_from_workout(session, workout, exercise_id):
    exercise = session.query(Exercise).filter(Exercise.id == exercise_id).first()
    if exercise:
        workout.exercises.remove(exercise)
        session.commit()   

 # User Interaction Functions
def display_menu(options, prompt="Please choose an option"):
    os.system("clear")
    print(bold(prompt))
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    return menu_entry_index, options[menu_entry_index]

def select_workout(session):        

