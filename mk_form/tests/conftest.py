# With pytest-django it is necessary to overwrite the default testing database..
# ..information if you want to run tests in a database instance other than default
# "TEST": {"ENGINE": "", "NAME": "", etc} in the main settings.py file will not work!
# <https://github.com/pytest-dev/pytest-django/issues/643>

# import pytest
# from pathlib import Path

# from django.conf import settings
# from django.db import connections

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent


# @pytest.fixture(scope="session")
# def django_db_setup():

#     # Remove cached_property of connections.settings
#     del connections.__dict__["settings"]

#     settings.DATABASES["default"] = {
#         "ENGINE": "your.engine.here",
#         "NAME": BASE_DIR / "db.name",
#     }

#     # Re-configure the settings with the new database configuration
#     connections._settings = connections.configure_settings(settings.DATABASES)

#     # Open connection to the newly specified database
#     connections["default"] = connections.create_connection("default")
