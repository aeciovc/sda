
import time

_users = [
    {
        "username": "kloseby0",
        "first_name": "Kleon",
        "last_name": "Loseby",
        "email": "kloseby0@exblog.jp",
    },
    {
        "username": "rpeele1",
        "first_name": "Ruthanne",
        "last_name": "Peele",
        "email": "rpeele1@alexa.com",
    },
    {
        "username": "lmangin2",
        "first_name": "Lamar",
        "last_name": "Mangin",
        "email": "lmangin2@msu.edu",
    },
    {
        "username": "ssima3",
        "first_name": "Spenser",
        "last_name": "Sima",
        "email": "ssima3@tripadvisor.com",
    },
]

_products = [
    {
        "name": "Pale Blue-eyed Grass",
        "sku": "ac5a71e7c937649ad36939049aa066e0",
        "in_storage": 10,
        "ordered": 6,
    },
    {
        "name": "Sudangrass",
        "sku": "452f463364ea8d35451a98dab8f4f289",
        "in_storage": 15,
        "ordered": 3,
    },
    {
        "name": "Climbing Bedstraw",
        "sku": "81a0396fa72e05bd8fc1c781d23519b8",
        "in_storage": 7,
        "ordered": 2,
    },
    {
        "name": "Pedilanthus",
        "sku": "57e34d3ba073dbcdf8f79ac8667e1637",
        "in_storage": 9,
        "ordered": 0,
    },
    {
        "name": "Ames' Lady's Tresses",
        "sku": "d835f3da395823d1b4cb606489d1a2ec",
        "in_storage": 7,
        "ordered": 0,
    },
]

_orders = [{"user_id": 0, "product_id": 1, "amount": 3, "paid": True}]

_events = []

class DB:
    """DB simulates a (very) naive database ORM. Its main goal is being slow."""

    def __init__(self):
        self._tables = {"users": _users, "products": _products, "orders": _orders, "events": _events}

    def list_tables(self):
        time.sleep(2)
        return tuple(self._tables.keys())

    def insert(self, table_name, obj):
        time.sleep(2)
        self._tables[table_name].append(obj)

    def count(self, table_name):
        time.sleep(2)
        return len(self._tables[table_name])

    def get(self, table_name, index):
        time.sleep(2)
        return self._tables[table_name][index]

    def get_table(self, table_name):
        time.sleep(2)
        return self._tables[table_name]

    def update(self, table_name, id_, obj):
        self._tables[table_name][id_] = obj
