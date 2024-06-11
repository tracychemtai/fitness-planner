from lib.models import Workout, Exercise
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 

print("🌱 Seeding DB...")

engine = create_engine('sqlite:///fitness_data.db')
Session = sessionmaker(bind=engine)
session = Session()