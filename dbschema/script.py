# -*- coding: utf-8 -*-
import sys

# from pyscript.model.user import User
from models.factories.user import User
# from .model.user import User

if __name__ == '__main__':
    u = User('8maki', 32)
    print(sys.path)
    print(u.greeting())
