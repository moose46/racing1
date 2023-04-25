import os

import pytest
from django.conf import settings
from django.contrib.auth.models import User
from django.db import connections
from django.db.utils import OperationalError

# from settings import DATABASES

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "racing1.settings")
# DJANGO_SETTINGS_MODULE = settings.configure()
# settings.configure()


@pytest.mark.django_db(databases=["default"])
class DbCheckMiddleware(object):
    db_conn = connections["default"]

    def process_request(self):
        print(f"db_conn.__repr__ = {self.db_conn.__repr__}")
        try:
            "Some DB Code"
            c = self.db_conn.cursor()
            assert True == True
        except OperationalError:
            assert True == False
        else:
            assert True == True


@pytest.mark.django_db(databases=["default"])
def test_driver():
    # db_conn = connections["default"]
    me = User.objects.create_user(username="BooBoo")
    print(f"me = {me.username}")
    assert me.username == "BooBoo"
    # assert User.objects.filter(name="me").count() == 1


# https://pytest-django.readthedocs.io/en/latest/database.html
@pytest.mark.django_db(databases=["default"])
def test_connection_connection():
    # print(f"DJANGO_SETTINGS_MODULE = {DJANGO_SETTINGS_MODULE}")
    db = DbCheckMiddleware()
    db.process_request()


def test_me():
    assert 1 == 1
