import pygame

class pieces:
    def __init__(self, piecetype, position):
        self.type = piecetype
        self.pos = position
        match(self.type.splice[1]):  
            case 'k': 
                self.move = {
                    'diagnol': True,
                    'forward': True,
                    'horizontal': True,
                    'back': True,
                    'L' : True,
                    'multi step': False
                }
            case 'q':
                self.move = {
                    'diagnol': True,
                    'forward': True,
                    'horizontal': True,
                    'back': True,
                    'L' : False,
                    'multi step': True
                }
            case 'b':
                self.move = {
                    'diagnol': True,
                    'forward': False,
                    'horizontal': False,
                    'back': False,
                    'L': False,
                    'multi step': True
                }
            case 'n':
                self.move = {
                    'diagnol': False,
                    'forward': False,
                    'horizontal': False,
                    'back': False,
                    'L': True,
                    'multi step': False
                }
            case 'r':
                self.move = {
                    'diagnol': False,
                    'forward': True,
                    'horizontal': True,
                    'back': True,
                    'L': False,
                    'multi step': True
                }
            case _:
                self.move = {
                    'diagnol': False,
                    'forward': True,
                    'horizontal': False,
                    'back': False,
                    'L': False,
                    'multi step': False
                }
    def sight(self):
        if self.move['multi step']:
            count = 30
        else:
            count = 1
        possible_moves = []
        for i in range(count):
            possible_moves[i] = [
                check.movement(self)
            ]
        return possible_moves

class check:
    def movement(piece):
        print('test')
    def special():
        print('test')
    def check(piece):
        print('test')

    