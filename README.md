# CLI Fit-Track Pro

## Table of Contents
- [Group Members](#Group-members)
- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)

## Group Members
- Tracy Chemtai -Scrum Master
- Victor Maina - member
- Aron Kiprotich- member
- Charity Wachira - member

## Project Description
The CLI Fitness Planner is a command-line interface application designed to help users plan for their fitness activities. Users can create workout plans, view exercises, and delete exercises over time.

## Features
- Create a new workout
- View workouts
- Add exercise to workout
- Delete exercise from workout
- Select workout
- Export and import workout data
- User-friendly command-line interface

## Project Structure 
```
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
├── cli.py
├── db
│   ├── models.py
│   └── seed.py
├── debug.py
└── helpers.py
```


## Installation
To install and run the CLI Fitness Planner, follow these steps:

1. Clone the repository:
    bash
    git clone https://github.com/tracychemtai/fitness-planner
2. Navigate to the project directory:
    bash
    cd fitness-planner
    
3. Install the required dependencies like SQLALchemy and Alembic before you begin.You can do this straight from the command line:
# Install dependencies
pipenv install sqlalchemy alembic

# Add Pipfile and Pipfile.lock to Git
git add Pipfile Pipfile.lock

# Commit the changes
git commit -m 'add sqlalchemy and alembic to pipenv'

# Push the changes
git push

# Activate the virtual environment
pipenv shell

 ## Usage
To start using the CLI Fitness Planner, run the following command in your terminal:
bash
python fitness_planner.py
```

## Commands
Here are some of the main commands you can use within the application:

- create a new workout: Create a new workout plan
- View workout: view the exercise to your plan
- Delete workout: delete the workout 
- Add new exercise to workout:adding new exercises to workout
- Delete exercise from workout: deleting exercises from workout
- Select workout: selecting workout
- Exit
- export_data: Export your workout data
- import_data: Import workout data

### Command Details

#### create_workout
Prompts the user to enter the name of the workout plan 

### view_workout
Displays a list of exercises in the current workout plan, including details such as exercise names, sets, reps

### delete_workout
Prompts the user to select a workout plan to delete from their list of plans. 

### add_exercise
Prompts the user to enter details for the new exercise, such as the name, sets, reps, and any notes.

### Delete an exercise from a workout plan
Prompts the user to select an exercise to delete from the current workout plan. 

### Select a workout plan
Prompts the user to choose a workout plan from their list of plans. This command sets the selected plan as the active workout plan for viewing, adding, or deleting exercises.

### exit
Terminates the CLI fitness planner application. Use this command to exit the program safely.


## Contributing
We welcome contributions from the community! If you have any suggestions, bug reports, or improvements, please create an issue or submit a pull request.

### Steps to Contribute
1. Fork the repository
2. Create a new branch (git checkout -b feature/YourFeature)
3. Commit your changes (git commit -m 'Add some feature')
4. Push to the branch (git push origin feature/YourFeature)
5. Create a new Pull Request

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
