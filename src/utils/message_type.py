from enum import Enum

# POSSIVEIS TIPOS DE MENSAGENS


class MessageTypes(Enum):
    INFORMATION = 1
    START = 2
    UPDATE_BALLS = 3
    WINNER = 4
    EXIT = 5
