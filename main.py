#!/usr/bin/python3
# -*-coding:Utf-8 -*

# -tc- commencer par développer le jeu en terminal, donc pas encore besoin de pygame
import pygame
from pygame.locals import color
from app.position import Position
from app.gardien import (
    gardien
)
from app.laby import (
    laby
)
from app.macgyver import (
    macgyver
)
from app.objets import (
    objets
)
import pylint


def main():
    """Main entry point."""
    position1 = Position(2, 3)

    print(position1)


if __name__ == "__main__":
    main()
