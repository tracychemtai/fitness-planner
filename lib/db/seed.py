from lib.models import Workout, Exercise
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 

print("🌱 Seeding DB...")

engine = create_engine('sqlite:///fitness_data.db')
Session = sessionmaker(bind=engine)
session = Session()


session.query(Exercise).delete()
session.query(Workout).delete()

exercises = [
    Exercise(
        exercise_name="Bench Press", 
        exercise_description="Lie on bench, lift barbell to chest, extend arms.", 
        category="strength", 
        weight=150, 
        units="lb", 
        reps=10, 
        sets=2), 
         Exercise(
        exercise_name="Dumbbell Press", 
        exercise_description="Lift barbells from shoulder height, extend arms.", 
        category="strength", 
        weight=50, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercise(
        exercise_name="Squat", 
        exercise_description="Bend knees, lower hips, stand up.", 
        category="strength", 
        weight=250, 
        units="lb", 
        reps=10, 
        sets=2),