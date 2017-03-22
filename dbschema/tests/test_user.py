# -*- coding: utf-8 -*-
from models.factories.user import User


def test_user_greeting():
    u = User('8maki', 31)
    print(u.greeting())
