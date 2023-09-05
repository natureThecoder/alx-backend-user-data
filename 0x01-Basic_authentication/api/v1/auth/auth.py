#!/usr/bin/env python3
""" Authentication for the Simple API"""

from typing import List, TypeVar
from flask import Flask, request


class Auth:
    """authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ public method that returns a boolean """
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths:
            return False

        for excluded_path in excluded_paths:
            if excluded_path.startswith(path):
                return False
            elif path.startswith(excluded_path):
                return False
            elif excluded_path[-1] == "*":
                if path.startswith(excluded_path[:-1]):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """pubic method that returns a string"""
        if request is None:
            return None
        val = request.headers.get('Authorization')
        if url is None:
            return None
        else:
            return val

    def current_user(self, request=None) -> TypeVar('User'):
        """method that returns a TypeVar"""
        return None
