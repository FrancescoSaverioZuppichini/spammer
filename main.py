import requests as r
import json
from time import sleep
from random import choice
from faker import Faker
from faker.providers import internet

URL = 'https://usb2.vf68.xyz/Home/Register/register.html'
CODE = 2020101153485010

counter = 0

fake = Faker()
fake.add_provider(internet)


def get_user():
    email, password = fake.email(), fake.password()
    return email, password


def spam():
    email, password = get_user()
    res = r.post(URL, data={
        'email': email,
        'password': password,
        'passwords': password,
        'code': 2020101153485010
    }
    )

while True:
    spam()
    counter += 1
    print(counter)
    sleep(0.01)
