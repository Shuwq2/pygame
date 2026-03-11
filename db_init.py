# Script qui va permettre de rajouter, modifier, suprimé des charactères dans la DB
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')


db = client["game_db"]

characters_collection = db["characters"]
monsters_collection = db["monsters"]
attemps_collection = db["attemps"]


def add_character(NAME: str, ATK: int, DEF: int, HP: int):
    new_character = {
        "NAME": NAME,
        "ATK": ATK,
        "DEF": DEF,
        "HP": HP
    }
    characters_collection.insert_one(new_character)

def add_monster(NAME: str, ATK: int, DEF: int, HP: int):
    new_monster = {
        "NAME": NAME,
        "ATK": ATK,
        "DEF": DEF,
        "HP": HP
    }
    monsters_collection.insert_one(new_monster)


def add_attemps(NAME, vague, characters):
    new_attemp = {
        "NAME": NAME,
        "VAGUE": vague,
        "CHARACTERS": characters
    }
    attemps_collection.insert_one(new_attemp)


def get_all_attemps():
    liste_attemps = []
    for attemp in attemps_collection.find({}, {"NAME": 1, "VAGUE": 1, "CHARACTERS": 1, "_id": 0}).sort("VAGUE", -1):
        liste_attemps.append(attemp)
    return liste_attemps



