#!/usr/bin/env python3
""" Script that validates a password (UKN)"""


import bcrypt


def hash_password(password: str) -> bytes:
    """ Receives a string argument and returns
    a salted, hashed password which is a byte
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Method that validates a password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
