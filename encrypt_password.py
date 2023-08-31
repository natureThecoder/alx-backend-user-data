#!/usr/bin/env python3
""" Script that validates a password"""


from bcrypt import checkpw, gensalt, hashpw


def hash_password(password: str) -> bytes:
    """ Receives a string argument and returns
    a salted, hashed password which is a byte
    """
    # encodes the string and encrypts it using gensalt method
    hash = hashpw(password.encode(), gensalt())
    return hash


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Method that validates a password
    Args:
        hashed_password: encrypted password
        password: string of character
    Return: boolean (true or false)
    """
    return checkpw(password.encode(), hashed_password)
