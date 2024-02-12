import random
import string

from models.client import Client
from models.package import Package


def create_client(full_name, passport_number=None):
    s = string.ascii_lowercase+string.digits
    return Client(full_name, passport_number or random.sample(s, 8))


def create_package(date, owner, code=None, origin=None,
                   destination=None, description=None):
    s = string.ascii_lowercase+string.digits
    return Package(date, owner, code or random.sample(s, 5),
                   origin, destination, description)
