from ast import Sub
from email.mime import base
from random import random
from tkinter import Place
import numpy as np
import pandas as pd
import random
dimensions = (8,8)
board = np.zeros(dimensions, dtype = int)

class Ship(object):
    length = 0 
    name = ''
    coords = []
    direction = None
    hits = 0
    def __init__(self) -> None:
        self.hits = 0 
        self.coords = []
        pass
    def ShipSunk(self):
        if self.hits == self.length:
            return print('your ' + self.name + ' has sunk!' )
    def place(self,row,col,direction):
        Placement = 0
        while Placement!=1:
            if direction == "LR":
                self.coords = [(c,row) for c in range(col, col + self.length)]
                Placement = 1
                break
            if direction == "UD":
                self.coords = [(col,r) for r in range(row, row + self.length)]
                Placement = 1
                break
            else:
                print("Invalid Direction")
        if (row + self.length >=8) or (col + self.length >=8):
            print('The Battleship goes off the Board')
            return
        else: 
            print('Valid Location!')
class Carrier(Ship):
    length = 5 
    name = 'Carrier'
class Battleship(Ship):
    length = 4 
    name = 'Battleship'
class Submarine(Ship):
    length = 3 
    name = 'Submarine'
class Destroyer(Ship):
    length = 2 
    name = 'Destroyer'
List_Of_Ships = [Carrier,Battleship,Submarine,Destroyer]
class Player(object):
    name = ''
    _board = None
    enemy = None 
    _ships = None 
    def __init__(self,name) -> None:
        dimensions = (8,8)
        self.name = name 
        self._board = np.zeros(dimensions, dtype = int)
        self._ships = []
        pass
    def placeship(self,ship,row,col,direction):
        ship.place(row,col,direction)
        n = 0
        for col, row in ship.coords:
            if self._board[row][col] == 0: 
                self._board[row][col] = 1
                n = n + 1 
            else:
                print('Somehthing exists in your path!')
                for i in range(n):
                    if direction == "LR":  
                        self._board[row][col-(i+1)] = 0
                    if direction == "UD":
                        self._board[row-(i+1)][col] = 0
                break
        self._ships.append(ship)
    def placeships(self):
        for ship in List_Of_Ships:
            while True:
                try:
                    a = input('Type in row')
                    b = input('Type in col')
                    c = input('Type in direction') 
                    row = int(a) 
                    col = int(b)
                    direction = c
                    player.placeship(ship(),row,col,direction)
                    print(player._board)
                    break
                except ValueError:
                    print('Invalid input.')
                
player = Player('John')