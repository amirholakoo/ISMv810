### Step 1: Installing Python

Django is a Python-based web framework, so the first step is to ensure you have Python installed on your system. Most Linux distributions come with Python pre-installed, but we'll make sure you have a version compatible with the latest Django release.

1.  Open a Terminal: Access your terminal through your Linux desktop environment.

2.  Check Python Installation: Type `python3 --version` into the terminal and press Enter. If you see a version number starting with 3.8 or higher, you're set. If not, or if you get an error message, proceed to install Python.

3.  Install Python: Run the following command to install Python:

    bashCopy code

    `sudo apt update
    sudo apt install python3 python3-pip python3-venv -y`

    This command updates your package list, installs Python3, pip (Python's package installer), and the package for creating virtual environments.

### Step 2: Setting Up a Virtual Environment

Using a virtual environment for your Django project is recommended. It allows you to manage project-specific dependencies separately from your global Python installation.

1.  Navigate to Your Project Directory: Decide where you want your project to live. For example, if you want it in your home directory under `projects`, you would use:

    bashCopy code

    `mkdir -p ~/projects/my_django_project
    cd ~/projects/my_django_project`

2.  Create a Virtual Environment: Run the following command to create a virtual environment named `venv` within your project directory:

    bashCopy code

    `python3 -m venv venv`

3.  Activate the Virtual Environment: Before you install Django or any other packages, activate your virtual environment:

    bashCopy code

    `source venv/bin/activate`

    Once activated, your terminal prompt should change to indicate that you're now working inside `venv`.

### Step 3: Installing Django

With your virtual environment activated, install Django using pip:

`sudo chown -R admin:admin /var/www/html/ISMv810/venv/`


`pip install django`

This command downloads and installs the latest Django version.

### Step 4: Create Your Django Project

1.  Create the Project: With Django installed, you're ready to create your project. Run:

    bashCopy code

    `django-admin startproject inventory_management .`

    The `.` at the end of the command creates the project in the current directory instead of making a new subdirectory.

2.  Start the Development Server: Check if everything is set up correctly by starting Django's development server:

    bashCopy code

    `python manage.py runserver`

3.  Access Your Project: Open a web browser and go to `http://127.0.0.1:8000/`. You should see Django's default welcome page.

### Step 5: Creating Your Django App

Now, let's create a Django app within your project where we'll define our models and views.

1.  Create the App: In your terminal (make sure you're in the project directory and have your virtual environment activated), run:

    bashCopy code

    `python manage.py startapp logistics`

This sets up a basic Django project structure and a dedicated app for handling logistics-related functionality like trucks, shipments, and purchase orders. Your environment is now ready for development!