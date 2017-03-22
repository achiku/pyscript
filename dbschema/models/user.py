# -*- coding: utf-8 -*-


class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return "I'm {0}.".format(self.name)
