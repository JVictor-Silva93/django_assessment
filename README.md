# Django Assessment

Complete the below multiple choice and true/false questions. Annotate them on a `.md` file or word document to be submitted with your code. 
Use the code in the `AssessmentBlog` folder in this repo, or you may create your Django project and app from scratch, the choice is yours.
Explain your process in part 3 Code Assessment of your `.md` file or word document. 
Remember to comment your code!

## I. Multiple Choice Questions

1. Which of the following is the primary configuration file for a Django project?
   - a) `settings.py`
   - b) `config.py`
   - c) `django.conf`
   - d) `main.py`

2. How do you start a new Django **app** named 'blog'?
   - a) `django startapp blog`
   - b) `django newapp blog`
   - c) `django createapp blog`
   - d) `python manage.py startapp blog`

3. In a Django view, what is the purpose of the `HttpResponse` class?
   - a) To redirect the user to a different webpage.
   - b) To render a template and send it to the user.
   - c) To capture form input from the user.
   - d) To send an HTML response to the user.

4. What is the command to run a Django development server on port 8080?
   - a) `python manage.py runserver`
   - b) `python manage.py runserver 8080`
   - c) `django serve --port 8080`
   - d) `django runserver -p 8080`

5. Which command is used to start a new Django **project** named 'myproject'?
   - a) `django-admin createproject myproject`
   - b) `python manage.py startproject myproject`
   - c) `django-admin startproject myproject`
   - d) `django new myproject`

6. Which Django object allows you to interact with the database, equivalent to running SQL commands?
   - a) Manager
   - b) Model
   - c) Middleware
   - d) Migrations

7. If you wanted to redirect a user to a different webpage after they submitted a form, which Django function would you use?
   - a) `HttpResponse()`
   - b) `render()`
   - c) `redirect()`
   - d) `send()`

8. Which command applies changes to the database based on model changes?
   - a) `python manage.py migrate`
   - b) `python manage.py makemigrations`
   - c) `python manage.py applymigrations`
   - d) `python manage.py dbupdate`

8. What purpose does the `MEDIA_URL` setting in Django serve?
   - a) It specifies the URL for static files.
   - b) It specifies the URL for user-uploaded files.
   - c) It sets the URL for the Django admin site.
   - d) It sets the base URL for the entire Django project.

10. Which decorator is commonly used in Django views to ensure that a user is logged in before they can access a particular view?
   - a) `@authenticate`
   - b) `@verify`
   - c) `@require_login`
   - d) `@login_required`

11. If you wanted to store the date and time a model instance was created, which field and option would you use in a Django model?
   - a) `DateField(auto_now=True)`
   - b) `DateTimeField(auto_now_add=True)`
   - c) `TimeField(auto_created=True)`
   - d) `DateField(add_now=True)`

## II. True or False

1. Django’s `FileField` automatically manages file storage when deleting or replacing a file.

2. In Django, the `models.py` file is primarily used to define the structure of your database tables.

3. The `django-admin` tool can be used to start a new Django project.

4. Middleware in Django is a series of classes or methods that process requests before reaching the view and responses before going back to the client.

6. In Django's ORM, the `QuerySet` object is evaluated (i.e., converted to an actual database query) only when it's explicitly saved.

7. When you use Django's built-in `User` model, passwords are stored in plain text in the database.

8. The `urlpatterns` list in Django is used to determine which view should be displayed for a given URL path.

9. In Django, if you don't specify a primary key field for your model, it will automatically generate an `id` field that acts as an auto-incrementing primary key.

10. A Django `Form` object is only used for rendering forms and doesn't handle any form validation.

11. In a Django model, setting the `blank` attribute to `True` for a field means that the field will have a default value in the database.

## III. Code Assessment

### Challenge 1: Basic Blog Application
**Objective:** Create a basic blog application using Django.

**Details:**

- **Models:**
  - `Post`: Should have fields for title, content, publication date, and author.
  - `Comment`: Should have fields for post (foreign key to Post), author name, content, and comment date.
  
- **Views and URLs:**
  - List of all posts.
  - Detail view for a single post, displaying comments underneath.
  - Form to add a new post.
  - Form to add a comment to a post.

- **Bonus:** Implement user authentication where only logged-in users can write posts but anyone can comment.

### Challenge 2: Custom Admin Interface
**Objective:** Customize the Django admin interface for better usability.

**Details:**

- Add the Post and Comment models (from challenge 1) to the admin interface.
- Customize the list display for Post to show the title, author, and publication date.
- Make the title field in the Post model clickable in the list display.
- Implement a search bar to filter posts by title.
- In the Comment admin interface, display comments inline when viewing a Post.

