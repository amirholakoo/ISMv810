
### Step 2: Update and Upgrade Your System

It's a good practice to ensure your system's package list and installed packages are up to date. In your terminal, run:

bashCopy code

`sudo apt-get update
sudo apt-get upgrade`

This process may take some time, depending on your internet connection and the number of updates available.

### Step 3: Install Python and Virtual Environment

Django is a Python-based framework, so you need Python installed. RPI4 usually comes with Python pre-installed, but let's ensure it's up to date.

1.  Install Python 3 and pip:

bashCopy code

`sudo apt-get install python3 python3-pip`

1.  Install Virtualenv:

bashCopy code

`sudo pip3 install virtualenv`

Virtual environments allow you to manage Python packages for different projects separately.

### Step 4: Setting Up a Project Directory

Choose where you want to store your project files. It's common to use the home directory for simplicity.

1.  Navigate to the Home Directory:

bashCopy code

`cd ~`

1.  Create a New Directory for Your Project:

Replace `myproject` with whatever you want to name your project:

bashCopy code

`mkdir myproject
cd myproject`

### Step 5: Create a Virtual Environment

Inside your project directory, create a virtual environment to isolate your project's Python/Django packages.

bashCopy code

`virtualenv myprojectenv`

Activate the virtual environment:

bashCopy code

`source myprojectenv/bin/activate`

Your command prompt should now show the name of your virtual environment, indicating it's active.

### Step 6: Install Django

With the virtual environment activated, install Django using pip:

bashCopy code

`pip install django`

### Step 7: Start a Django Project

Create a new Django project with:

bashCopy code

`django-admin startproject myproject .`

The dot at the end creates the project in the current directory without adding an extra subdirectory.

### Step 8: Run the Development Server

Test if everything's set up correctly:

bashCopy code

`python manage.py runserver`

You should see a message indicating the development server is running. You can access the Django default welcome page by navigating to `http://localhost:8000` on your RPI4's web browser.

### Step 9: Accessing Django Admin

Before accessing the Django admin, you need to create a superuser.

1.  Create Superuser:

bashCopy code

`python manage.py createsuperuser`

Follow the prompts to set up a username, email, and password.

1.  Run the Server Again (if not running):

bashCopy code

`python manage.py runserver`

1.  Access Admin Site: Go to `http://localhost:8000/admin` and log in with the superuser account you just created.



### Step 10: Install MySQL Development Libraries

Run the following command to install the MySQL client development libraries along with other necessary build tools:

bashCopy code

`sudo apt-get install default-libmysqlclient-dev build-essential`

-   `default-libmysqlclient-dev`: This package contains the MySQL client library and development files needed by `mysqlclient`.
-   `build-essential`: This package installs various packages that are essential for building Debian packages, including `gcc` compiler and `make` tool.

### Step 11: Retry Installing `mysqlclient`

With the necessary development libraries installed, try installing `mysqlclient` again within your virtual environment:

bashCopy code

`pip install mysqlclient`

This command should now successfully install the `mysqlclient` package without the previous errors.

### Additional Steps for Django Database Configuration

After installing `mysqlclient`, you'll need to configure your Django project to use MySQL as its database backend:

1.  Modify `settings.py`: In your Django project's `settings.py` file, you'll find a `DATABASES` setting. Modify it to use MySQL, replacing `'ENGINE': 'django.db.backends.sqlite3',` with `'ENGINE': 'django.db.backends.mysql',`, and set the `NAME`, `USER`, `PASSWORD`, `HOST`, and `PORT` to match your MySQL database configuration.

2.  Example Configuration:

pythonCopy code

`sudo nano ~/myproject/myproject/settings.py`


`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',  # Or an IP address if your database is on a different server
        'PORT': '3306',  # Default MySQL port
    }
}`

### Step X: Apply Migrations

After modifying `settings.py`, return to the terminal and make sure your virtual environment is activated. Apply the Django migrations to create the necessary database tables by running:

bashCopy code

`python manage.py migrate`




### Step 1: Navigate to Your Project Directory

Ensure you're in the correct directory where your Django project is located (`/var/www/html/ISMv810` in your case). If you're not already there, use:

bashCopy code

`cd /var/www/html/ISMv810`

### Step 2: Define Your Model

1.  Open the `models.py` file within your app directory. If we're using the `inventory` app as suggested, the path would be `/var/www/html/ISMv810/inventory/models.py`.

2.  Define a `Product` model by adding the following code to `models.py`:

pythonCopy code

`from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name`

This code snippet defines a simple `Product` model with a name, description, price, and a Boolean field indicating if it's in stock.

### Step 3: Create and Apply Migrations

After defining your model, you need to create and apply migrations to update your database schema. Ensure you're still in the root directory of your Django project to execute these commands.

1.  Create migrations for your new model:

bashCopy code

`python manage.py makemigrations`

1.  Apply migrations to your database:

bashCopy code

`python manage.py migrate`

These commands analyze the models you've defined, create migration files (which are blueprints for changing your database schema), and then apply these migrations to make the actual schema changes in your database.

### Register Your Model in the Admin Site

### Step 1: Register Your Model in the Admin Site

To manage `Product` objects through the Django admin site, you need to register the model in `admin.py` of your app (`inventory`).

1.  Open `/var/www/html/ISMv810/inventory/admin.py` in a text editor.

2.  Add the following code to register the `Product` model:

pythonCopy code

`from django.contrib import admin
from .models import Product

admin.site.register(Product)`

### Step 2: Restart the Development Server and Check the Admin Site

If your development server isn't running, start it again with:

bashCopy code

`python manage.py runserver`

Now, when you navigate to `http://localhost:8000/admin` and log in, you should see the `Products` section listed along with `Groups` and `Users`. You can add, edit, or delete product entries using the admin interface.