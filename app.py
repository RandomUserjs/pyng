from classes.Menus.Menu_principal import Main
from classes.Menus.Menu_opcoes import Opcoes
import pygame as pg

"""def run_game():
    op = Opcoes()
    op.mostrar_menus()
    pg.quit()"""

def run_game():
    main = Main()
    main.mostrar_menus()
    pg.quit()

"""def run_game():
    game = Game()
    game.run()
    pg.quit()
"""
if __name__ == "__main__":
    run_game()