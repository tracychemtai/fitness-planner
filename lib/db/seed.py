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
          Exercise(
        exercise_name="Bicep Curls", 
        exercise_description="Choose wight, lift dumbbell while isolating the bicep.", 
        category="strength", 
        weight=35, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercise(
        exercise_name="Forearm Curls", 
        exercise_description="Flex wrists, lift weights.", 
        category="strength", 
        weight=30, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercise(
        exercise_name="Dead-lift", 
        exercise_description="Lift-barbell off ground while maintaining good posture. Stand tall.", 
        category="strength", 
        weight=200, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercise(
        exercise_name="Pullups", 
        exercise_description="Hang, lift body, chin over bar.", 
        category="strength", 
        weight=0, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercise(
        exercise_name="Cable Rows", 
        exercise_description="Sit, pull cable to torso.", 
        category="Strength", 
        weight=80, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercise(
        exercise_name="Planks", 
        exercise_description="Hold push-up position", 
        category="Strength", 
        weight=80, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercise(
        exercise_name="Situps", 
        exercise_description="Lie on bench. lift torso.", 
        category="Strength", 
        weight=0, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercise(
        exercise_name="Jog", 
        exercise_description="Light run", 
        category="Cardio", 
        weight=1, 
        units="Mile(s)", 
        reps=1, 
        sets=1),
    Exercise(
        exercise_name="Cycle", 
        exercise_description="Cycle in place", 
        category="Cardio", 
        weight=1, 
        units="Mile(s)", 
        reps=1, 
        sets=1),
    Exercise(
        exercise_name="Lat Pull-downs", 
        exercise_description="Sit, pull bar to chest.", 
        category="Strength", 
        weight=160, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercise(
        exercise_name="Shrugs", 
        exercise_description="Holds dumbbells. Lift shoulders and hold.", 
        category="Strength", 
        weight=100, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercise(
        exercise_name="Deltoid Raises", 
        exercise_description="Choose wight, lift dumbbell sideways while isolating the deltoids.", 
        category="Strength", 
        weight=10, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercise(
        exercise_name="Cable Fly", 
        exercise_description="Pull cables across chest.", 
        category="Strength", 
        weight=120, 
        units="lb", 
        reps=10, 
        sets=2),
    Exercise(
        exercise_name="Cable Tricep Extensions", 
        exercise_description="Pull cable down and extend arms.", 
        category="Strength", 
        weight=80, 
        units="lb", 
        reps=10, 
        sets=2),
]

workouts = [
    Workout(
        workout_name="Push",
        workout_description="In the “push” workout you train all the upper body pushing muscles, i.e. the chest, shoulders and triceps."),
    Workout(
        workout_name="Pull",
        workout_description="In the “pull” workout you train all the upper body pulling muscles, i.e. the back and biceps."), 
    Workout(
        workout_name="Abs & Legs",
        workout_description="And in the “legs” workout you train the entire lower body, i.e. the quads, hamstrings, calves and abdomen."
    )
]

session.add_all(exercises)
session.add_all(workouts)
session.commit()

push_day = workouts[0]

jog = exercises[10]
bench_press = exercises[0]
deltoid_raises = exercises[14]
dumbbell_press = exercises[1]


