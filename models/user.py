#!/usr/bin/python3
"""Module for user"""

import models
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
