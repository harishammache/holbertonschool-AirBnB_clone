#!/usr/bin/python3
"""models/place.py"""

from models.base_model import BaseModel


class State(BaseModel):
    """Place class that inherits from BaseModel."""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    nombre_chambres = 0
    nombre_salles_de_bain = 0
    max_invités = 0
    prix_par_nuit = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
