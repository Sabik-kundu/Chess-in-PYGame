import pygame
import os, sys
LIGHT = (238, 238, 210)
DARK = (118, 150, 86)

BOARD_SIZE = 8
SQUARE_SIZE = 80
BOARD_AREA = BOARD_SIZE * SQUARE_SIZE
IMAGE_DIR = r"./Pieces"

board = [
    ["bR","bN","bB","bQ","bK","bB","bN","bR"],
    ["bP","bP","bP","bP","bP","bP","bP","bP"],
    [None]*8,
    [None]*8,
    [None]*8,
    [None]*8,
    ["wP","wP","wP","wP","wP","wP","wP","wP"],
    ["wR","wN","wB","wQ","wK","wB","wN","wR"],
    ]

piece_img = {
    "bR" : "bR.png", "bN" : "bN.png", "bB" : "bB.png", "bQ" : "bQ.png", "bK" : "bK.png", "bP" : "bP.png",
    "wR" : "wR.png", "wN" : "wN.png", "wB" : "wB.png", "wQ" : "wQ.png", "wK" : "wK.png", "wP" : "wP.png",
}

def draw_board(surface: pygame.Surface) -> None:
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = LIGHT if (row + col) % 2 == 0 else DARK
            pygame.draw.rect(
                surface,
                color,
                (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            )
            
