"""
describes the grid to play with
"""

from Pawn import Pawn


class Grid(object):
    """
    define the Grid of the game
    """
    def __init__(self, taille_grid):

        self.grid = [[Pawn(None) for dummy_i in range(taille_grid)]\
                     for dummy_j in range(taille_grid)]

    def add_a_pawn(self, player, pos_x, pos_y):
        """
        add a pawn in the grid if possible return True else return False
        """
        if self.grid[pos_y][pos_x].color is None:
            self.grid[pos_y][pos_x].change_color(player.color)
            return True
        else:
            return False

    def is_finished(self):
        """
        test if grid is finished
        """
        for line in self.grid:
            for pawn in line:
                if pawn.color is None:
                    return False
        return True

    def give_winner(self):
        """
        return the color of the winner
        """
        player_score = {}
        for line in self.grid:
            for pawn in line:
                player_score[pawn.color] = player_score.get(pawn.color, 0) + 1
        return max(player_score)

