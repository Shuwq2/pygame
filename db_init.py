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
    characters_collection.insert_one(new_monster)


def add_attemps(NAME, vague, characters):

    ...



