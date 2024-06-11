# import random
# import string

# def generate_id(length=8):
#     """Generate a random string of letters and digits """
#     letters_and_digits = string.ascii_letters + string.digits
#     rand_string = ''.join(random.choice(letters_and_digits) for i in range(length))
#     return rand_string

# class Exercise:
#     def __init__(self, name, reps, sets, id=None):
#         self.name = name
#         self.reps = reps 
#         self.sets = sets
#         self.id = id or generate_id()

#     def __repr__(self):
#         return f"Exercise('{self.name}', {self.reps}, {self.sets}, '{self.id}')"

# exercises = []

# def add_exercise(name, reps, sets):
#     exercise = Exercise(name, reps, sets)
#     exercises.append(exercise)
#     return exercise

# def remove_exercise(id):
#     for i, ex in enumerate(exercises):
#         if ex.id == id:
#             del exercises[i]
#             return
#     print(f"Exercise with id {id} not found")

# def view_exercises():
#     for ex in exercises:
#         print(ex)