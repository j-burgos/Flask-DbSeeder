# Flask-Seed

A (hopefully) soon to be, Flask extension that helps creating seed data for a database using SQLAlchemy models

Highly influenced by Laravel seeds

## Usage

    from flask_seed.seeder import Seeder
    from models.auth import User, Role

    seeder = Seeder(db)

    seeder.add_seed([
        User(username='admin', password='password', roles=[Role(name='admin'), Role(name='user')]),
        User(username='user', password='password', roles=[Role(name='user')]),
    ])

    seeder.run()

## TODO:

- Follow Flask extension conventions
- Fix bugs with related data
