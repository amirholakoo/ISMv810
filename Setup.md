### Step 1: Installing Python

Most Linux distributions come with Python pre-installed. However, to ensure you have the latest version, you can install or update Python using your package manager.

1.  Open your terminal.
2.  Update your package list to make sure you get the latest versions of the packages:

    sqlCopy code

    `sudo apt update`

3.  Install Python 3 (if it's not installed or you need an updated version):

    Copy code

    `sudo apt install python3`

4.  Verify the installation by checking the Python version:

    cssCopy code

    `python3 --version`

### Step 2: Installing pip

`pip` is the package installer for Python. You can use it to install packages from the Python Package Index (PyPI) and other indexes.

1.  If `pip` is not installed, you can install it by running:

    Copy code

    `sudo apt install python3-pip`

2.  Verify the installation by checking the `pip` version:

    cssCopy code

    `pip3 --version`

### Step 3: Setting Up a Virtual Environment

A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. Using a virtual environment allows you to manage dependencies for different projects separately.

1.  Install the `virtualenv` package:

    Copy code

    `pip3 install virtualenv`

2.  Navigate to the directory where you want to set up your Django project. This can be anywhere you have permission to write files, such as your home directory. For example, if you want to work in `~/projects/`:

    bashCopy code

    `mkdir ~/projects
    cd ~/projects`

3.  Create a new virtual environment for your project:

    Copy code

    `virtualenv inventory_env`

4.  Activate the virtual environment:

    bashCopy code

    `source inventory_env/bin/activate`

    -   Your prompt will change to indicate that you are now working within the virtual environment. It will look something like `(inventory_env) user@hostname:~/projects$`.

### Step 4: Installing Django

With your virtual environment activated, you can install Django using `pip`.

1.  Install Django:

    Copy code

    `pip install django`

2.  Verify the installation by checking the Django version:

    cssCopy code

    `django-admin --version`

### Step 5: Creating Your Django Project

1.  Still within your virtual environment and your preferred project directory, create a new Django project by running:

    Copy code

    `django-admin startproject inventory_management`

2.  Navigate into your project directory:

    bashCopy code

    `cd inventory_management`

3.  Create a Django app. Let's call it `logistics`:

    Copy code

    `python manage.py startapp logistics`

Congratulations! You have now set up your environment, installed Django, and created a new Django project with a `logistics` app. This is the foundation upon which we'll build your inventory and sales management system.