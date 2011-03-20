#!/usr/bin/python3.1

from exception import *



size = 11
board = None

class piece:
    def __init__ (self):
        self.alive = True

    def move_piece (self, from_coor, to_coor):
       pass
        
class defender (piece):
    def __init__ (self):
        self.img = None

    def __str__ (self):
        return "O"

class attacker (piece):
    def __init__ (self):
        self.img = None

    def __str__ (self):
        return "X"

class king (piece):
    def __init__ (self):
        self.img = None

    def __str__ (self):
        return "#"

def get_square_type (row, col):
    global size
    if size == 11:
        if col == 5 and row == 5:
            return "throne"
        if row == 0 or row == 10:
            if col > 2 and col < 8:
                return "attacker"
        if col == 0 or col == 10:
            if row > 2 and row < 8:
                return "attacker"
            elif row == 0 or row == 10:
                return "burg"
        if row == 5: 
            if col == 1 or col == 9:
                return "attacker"
        if col == 5:
            if row == 1 or row == 9:
                return "attacker"
        if row == 5:
            if col > 2 and col < 8:
                return "defender"
        if col == 5:
            if row > 2 and row < 8:
                return "defender"
        if row == 4 or row == 6:
            if col == 4 or col == 6:
                return "defender"
        return "default"
    elif size == 13:
        if col == 6 and row == 6:
            return "throne"
        if row == 0 or row == 12:
            if col > 3 and col < 9:
                return "attacker"
            elif col == 0 or col == 12:
                return "burg"
        if col == 0 or col == 12:
            if row > 3 and row < 9:
                return "attacker"
        if row == 1 or row == 11:
            if col == 6:
                return "attacker"
        if row == 6:
            if col == 1 or col == 11:
                return "attacker"
            elif col > 2 and col < 10:
                return "defender"
        if col == 6:
            if row == 1 or row == 11:
                return "attacker"
            elif row > 2 and row < 10:
                return "defender"
        return "default"
    else:
        raise WrongSizeException("Board size is %s: should be either 11 or 13.")

class square:
    def __init__ (self, row, col):
        self.row = row
        self.col = col
        self.square_type = get_square_type(row, col)
        self.piece = self.get_default_piece()

    def __str__ (self):
        if self.piece:
            return "%s%s" % (str(self.piece), self.get_square_representation())
        return " %s" % self.get_square_representation()

    def get_square_representation (self):
        if self.square_type == "burg":
            return "I"
        if self.square_type == "throne":
            return "¤"
        return " "

    def get_default_piece (self):
        if self.square_type == "defender":
            return defender()
        elif self.square_type == "attacker":
            return attacker()
        elif self.square_type == "throne":
            return king()
        else:
            return None
        


class board:
    def __init__ (self):
        global size
        self.size = size
        self.squares = [[square(row, col) for col in range(size)] for row in range(size)]

    def __str__ (self):
        for row in self.squares:
            for col in row:
                print(col),
            print

    def print_board (self):
        global size
        print("   ", end="")
        for i in range(size):
            print("%3i" % i, end="")
        print()
        self.print_hline()
        for row in self.squares:
            print("%2i " % row[0].row, end="")
            for col in row:
                print("|", str(col), sep="", end="")
            print("|")
        self.print_hline()

    def print_hline (self):
        if size == 11:
            print("   ----------------------------------")
        elif size == 13:
            print("   ----------------------------------------")
        else:
            raise WrongSizeException("Board size is %s: should be either 11 or 13.")

def hnefatafl (board_size=11):
    if board_size != 11 and board_size != 13:
            raise WrongSizeException("Board size is %s: should be either 11 or 13.")
        
    global size, board
    size = board_size
    board = board()



hnefatafl()


