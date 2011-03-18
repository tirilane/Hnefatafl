#!/usr/bin/python3.1


class piece:
    def __init__(self):
        self.alive = True

class defender (piece):
    def __init__ (self):
        self.img = None

class attacker (piece):
    def __init__ (self):
        self.img = None

class king (piece):
    def __init__ (self):
        self.img = None

def get_default_piece (row, col, size=11):
    if size == 11:
        if row == 0 or row == 10:
            if col > 2 and col < 8:
                return attacker()
        if col == 0 or col == 10:
            if row > 2 and row < 8:
                return attacker()
        if row == 5: 
            if col == 1 or col == 9:
                return attacker()
        if col == 5:
            if row == 1 or row == 1:
                return attacker()
        if col == 5 and row == 5:
            return king()
        if row == 5:
            if col > 2 and col < 8:
                return defender()
        if col == 5:
            if row > 2 and row < 8:
                return defender()
        if row == 4 or row == 6:
            if col == 4 or col == 6:
                return defender()



class square:
    def __init__ (self, row, col, piece=get_default_piece()):
        self.row = row
        self.col = col
        self.piece = piece


class board:
    def __init__(self):
        self.squares = []

