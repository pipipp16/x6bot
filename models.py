from dataclasses import dataclass
from datetime import datetime

@dataclass
class Player:

    discord_id:int
    game_name:str
    avatar:str
    position:str

    club:str|None=None

    registered:bool=True

@dataclass
class Club:

    name:str

    short:str

    captain:int

    sub1:int|None=None

    sub2:int|None=None

    jersey1:str=""

    jersey2:str=""

@dataclass
class Offer:

    offer_id:str

    club:str

    player:int

    role:str

    created:datetime

    expire:datetime
