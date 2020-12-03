import requests as r
import json
from time import sleep
from random import choice
from faker import Faker
from faker.providers import internet
import pypeln as pl

URL = 'https://usb2.vf68.xyz/Home/Register/register.html'
CODE = 2020101153485010

counter = 0

fake = Faker()
fake.add_provider(internet)


def get_user():
    email, password = fake.email(), fake.password()
    return email, password


def spam(*args):
    email, password = get_user()
    res = r.post(URL, data={
        'email': email,
        'password': password,
        'passwords': password,
        'code': 2020101153485010
    }
    )

    return (email, password)

while True:
    stage = pl.thread.map(spam, [None, None, None], workers=3)
    data = list(stage)
    for email, password in data:
        print(email, password)
    # spam()
    counter += 3
    print(counter)
    # sleep(0.01)
