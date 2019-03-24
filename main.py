#!/usr/bin/python3
# -*-coding:Utf-8 -*

import pygame
from pygame.locals import *
from app.position import Position
from app.subapp.module import (
    Classe1, Classe2, fonction1, fonction2
)

pygame.init()

def main():
    """Main entry point."""
    position1 = Position(2, 3)

    print(position1)

if __name__ == "__main__":
    main()