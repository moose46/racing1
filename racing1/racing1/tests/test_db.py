import os

import pytest
from django.conf import settings
from django.db import connections
from django.db.utils import OperationalError

# from settings import DATABASES

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "racing1.settings")
# DJANGO_SETTINGS_MODULE = settings.configure()
# settings.configure()


class DbCheckMiddleware(object):
    def process_request(self):
        db_conn = connections["postgres"]
        print(f"db_conn.__repr__ = {db_conn.__repr__}")
        try:
            "Some DB Code"
            c = db_conn.cursor()
            success = True
        except OperationalError:
            assert True == False
        else:
            assert True == True


# https://pytest-django.readthedocs.io/en/latest/database.html
@pytest.mark.django_db(databases=["postgres"])
def test_connection_connection():
    # print(f"DJANGO_SETTINGS_MODULE = {DJANGO_SETTINGS_MODULE}")
    db = DbCheckMiddleware()
    db.process_request()


def test_me():
    assert 1 == 1
