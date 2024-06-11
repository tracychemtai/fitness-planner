# fitness-planner



## Introduction

Fork and clone this lesson
for a template for your CLI. Take a look at the directory structure before we
begin:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── cli.py
    ├── db
    │   ├── models.py
    │   └── seed.py
    ├── debug.py
    └── helpers.py
```


## Generating Your Pipenv

You might have noticed in the file structure- there's already a Pipfile! That
being said, we haven't put much in there- just Python version 3.8 and ipdb.

Install any dependencies you know you'll need for your project, like SQLAlchemy
and Alembic, before you begin. You can do this straight from the command line:

```console
$ pipenv install sqlalchemy alembic
```

From here, you should run your second commit:

```console
$ git add Pipfile Pipfile.lock
$ git commit -m'add sqlalchemy and alembic to pipenv'
$ git push
```

Now that your environment is set up, run `pipenv shell` to enter it.

***

## Generating Your Database

Once you're in your environment, you can start development wherever you'd like.
We think it's easiest to start with setting up your database.

`cd` into the `lib/db` directory, then run `alembic init migrations` to set up
Alembic. Modify line 58 in `alembic.ini` to point to the database you intend to
create, then replace line 21 in `migrations/env.py` with the following:

```py
from models import Base
target_metadata = Base.metadata
```

We haven't created our `Base` or any models just yet, but we know where they're
going to be. Navigate to `models.py` and start creating those models. Remember
to regularly run `alembic revision --autogenerate -m'<descriptive message>'` and
`alembic upgrade head` to track your modifications to the database and create
checkpoints in case you ever need to roll those modifications back.

If you want to seed your database, now would be a great time to write out your
`seed.py` script and run it to generate some test data. You may want to use
Pipenv to install Faker to save you some time.

***


## Resources

- [Setting up a respository - Atlassian](https://www.atlassian.com/git/tutorials/setting-up-a-repository)
- [Create a repo- GitHub Docs](https://docs.github.com/en/get-started/quickstart/create-a-repo)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
