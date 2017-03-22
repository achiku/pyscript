# -*- coding: utf-8 -*-
from models.user import User


class UserFactory(object):
    def __init__(self):
        self.u = User('tarou', 34)

    def greeting(self):
        return self.u.greeting()
