# School Bus Management Demo

This repository contains a small demonstration project built with Django. It showcases core features described in the accompanying design document such as user management, driver and vehicle tracking, bookings and dispatch operations.

The project is intentionally minimal so it can be easily set up locally for exploration or teaching. Below you will find instructions for environment setup, project execution and testing as well as an overview of all modules.

## Environment setup

The code requires **Python 3.10+**. The steps below assume a Unix-like shell but can be adapted for Windows.

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install project dependencies. Only Django is required for this demo:

   ```bash
   pip install django==4.2.8
   ```

   Optionally create a `requirements.txt` using `pip freeze > requirements.txt` if you add more packages.

## Initializing the database

The project uses SQLite by default. Run the migrations and load some example data:

```bash
python manage.py migrate
python manage.py loaddata
```

To create demonstration users, drivers and vehicles you can run the included management command:

```bash
python manage.py init_data
```

This will create an admin account (`admin` / `admin123`) as well as several standard users and drivers.

## Running the development server

Start the Django development server after applying migrations:

```bash
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser. The root URL redirects to `/bus/realtime/` which displays a list of active dispatches and a placeholder map. Visit `/admin/` for the Django admin site where you can manage users, drivers, vehicles and bookings.

Static files are served directly in development through the configuration in `school_bus/settings.py`.

## Running tests

Execute the unit tests with:

```bash
python manage.py test
```

The tests cover basic model creation and the realtime monitor view. They help verify that the demo installation works correctly.

## Project structure

```
school_bus_system/
├── manage.py           # Django management script
├── school_bus/         # Project configuration package
│   ├── __init__.py
│   ├── asgi.py         # ASGI entry point (for WebSocket support)
│   ├── settings.py     # Global settings including installed apps and database
│   ├── urls.py         # Project-level URL routes
│   └── wsgi.py         # WSGI entry point for deployment
└── bus_system/         # Main application implementing the demo features
    ├── migrations/     # Database migrations for the models
    ├── management/
    │   └── commands/
    │       └── init_data.py  # Command to create sample data
    ├── templates/
    │   └── bus_system/
    │       ├── base.html             # Shared layout
    │       ├── realtime_monitor.html # Map view of active dispatches
    │       └── statistics.html       # Example statistics page
    ├── __init__.py
    ├── admin.py        # Django admin registrations
    ├── apps.py         # Application configuration
    ├── models.py       # Data models for users, drivers, vehicles, bookings
    ├── tests.py        # Unit tests for models and views
    ├── urls.py         # App-level URL routes
    └── views.py        # Views implementing realtime tracking and statistics
```

### Key modules

- **models.py** – Defines the core data models such as `User`, `Driver`, `Vehicle`, `Booking`, `Dispatch` and `LocationHistory`. These capture the information required for managing trips and tracking vehicles.
- **views.py** – Implements three main views: `realtime_monitor` displays active dispatches on a map, `update_location` receives GPS coordinates from drivers and `statistics_view` renders charts using static demo data.
- **admin.py** – Registers all models with the Django admin interface with a few custom search options and list displays.
- **management/commands/init_data.py** – Creates sample database records including an administrator, several drivers, vehicles and users.
- **tests.py** – Contains a small suite of Django `TestCase` classes verifying model and view behaviour.

## Further improvements

This project is meant as a learning example. You can extend it with real-time WebSocket updates, integration with map APIs, proper user permissions and advanced statistics. The included PDF explains a full set of possible features for inspiration.

