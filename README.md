# FabTechNet-CommunityChatApp
FabTechNet: A web platform for tech enthusiasts to connect, collaborate, and learn together. Create rooms based on interests, engage in real-time discussions, and find project partners.

Here’s the updated Markdown content, including the new process for creating a superuser with a custom user model, and a warning block for clarity:

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the Repository:**

   First, clone the repository to your local machine using Git.

   ```bash
   git clone https://github.com/yourusername/yourproject.git
   ```

2. **Navigate to the Project Directory:**

   Change to the project's root directory.

   ```bash
   cd yourproject
   ```

3. **Set Up a Virtual Environment (Optional but Recommended):**

   It's a good practice to use a virtual environment to manage your project's dependencies. <br><br><b>PLEASE BE NOTIFIED YOU DONT NEED TO DO THIS STEP IF YOU ARE USING PYCHARM. USE PYCHARM PROJECT INTERPRETER SYSTEM INSTEAD</b>

   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

4. **Install the Required Dependencies:**

   Install the project's dependencies using the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

5. **Run Migrations (if applicable):**

   If your project uses a database, apply the migrations to set up the database schema.

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (Optional):**

   If the project includes a Django admin interface, create a superuser to access it.

   ```bash
   python manage.py createsuperuser
   ```

   **Warning:** If you are using a custom user model, follow the steps below to create a superuser:

### Steps to Create a Superuser with a Custom User Model

   1. **Ensure Your Custom User Model is Properly Configured:**

      In your `settings.py`, you should have a line like this:

      ```python
      AUTH_USER_MODEL = 'base.User'
      ```

      This tells Django to use your custom user model instead of the default one.

   2. **Open the Python Shell:**

      Open the Django Python shell to interact with your project.

      ```bash
      python manage.py shell
      ```

   3. **Create a Superuser Programmatically:**

      Once in the Python shell, execute the following code to create a superuser:

      ```python
      from django.contrib.auth import get_user_model

      User = get_user_model()
      User.objects.create_superuser(username='admin', email='admin@fabtech.com', password='adminpass')
      ```

      This code will use your custom user model, `base.User`, instead of `auth.User`.

7. **Run the Development Server:**

   Start the Django development server to run the project locally.

   ```bash
   python manage.py runserver
   ```

8. **Access the Application:**

   Open your web browser and go to the following address:

   ```
   http://127.0.0.1:8000/
   ```

### Updating `requirements.txt`

If you add new dependencies to your project, update the `requirements.txt` file by running:

```bash
pip freeze > requirements.txt
```

This command will regenerate the `requirements.txt` file with the latest versions of all installed packages.
```

This Markdown content now includes detailed instructions for creating a superuser with a custom user model and other installation steps.