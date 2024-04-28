# PyE-Commerce
To run this project, follow these steps:
1. Set Up Python Environment
   Ensure you have Python installed on your system. Django requires Python 3.6 or later.

2. Install Django
   Install Django using pip: pip install django

3. Install Project Dependencies

4. Set Up Database
   Configure the database settings in settings.py (default is mySQL) or use other supported databases like PostgreSQL, MySQL, etc
   Migrating Data for this project,
   Update Django models (models.py) to reflect the desired changes. Use Django's migration system (makemigrations and migrate) to apply these changes to the database schema.
   Then use this command: python manage.py makemigrations
                          python manage.py migrate


5. Create a Superuser (Admin)
   Create a superuser to access the Django admin interface: python manage.py createsuperuser

6. Run the Development Server
   Start the Django development server: python manage.py runserver
   The server will start at http://127.0.0.1:8000/ by default

7. Run Tests
   To run tests for this Django project: python manage.py test
