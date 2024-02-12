## Django Quotes Website (Final project)

In tasks earlier we scraped the site http://quotes.toscrape.com.

Now we need to independently implement an analogue of such a site on `Django`:

     We implemented the possibility of registering on the site and entering the site.
     Made it possible to add a new author to the site only for a registered user.
     Made it possible to add a new quote to the site with an indication of the author only for registered users.
     Migrated your existing MongoDB database to Postgres for your site using a custom script.
     Made it possible to go to each author's page without user authentication.
     All quotes are viewable without user authentication.
     Pagination has been added (these are the next and previous buttons on our website).
     Implement a password reset mechanism for a registered user;
     All environment variables must be stored in the `.env` file and used in the `settings.py` file.

Console commands that we use in the project (launch from folder `\hw10\hw_django`):
- to create a project structure:
    * `python manage.py quotes`  
- to create applications inside the project:
    * `python manage.py startapp quotes` 
    * `python manage.py startapp users` 
- to start the server:
    * `python manage.py runserver`
- for migration:
    * `python manage.py makemigrations` 
    * `python manage.py migrate`
    * `python -m utils.migration`