"""
describes the grid to play with
"""

from Pawn import Pawn


class Grid(object):
    """
    define the Grid of the game
    """
    def __init__(self, taille_grid):
        """
        constructor of the grid, create a grid of pawn with None color
        """
        self.grid = [[Pawn(None) for dummy_i in range(taille_grid)]\
                     for dummy_j in range(taille_grid)]

    def add_a_pawn(self, player, pos_x, pos_y):
        """
        add a pawn in the grid if possible return True else return False
        """
        if not pos_x in range(0, len(self.grid)) \
        or not pos_y in range(0, len(self.grid)):
            return False
        if self.grid[pos_x][pos_y].color is None:
            for index_x in range(-1, 2):
                for index_y in range(-1, 2):
                    other_pos_x = pos_x + index_x
                    other_pos_y = pos_y + index_y
                    if other_pos_x < 0 or other_pos_y < 0:
                        continue
                    try:
                        if not self.grid[other_pos_x][other_pos_y].color is None:
                            self.grid[other_pos_x][other_pos_y].change_color(player.color)
                    except IndexError:
                        continue
            self.grid[pos_x][pos_y].change_color(player.color)
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

    def __repr__(self):
        msg = ""
        for index_x in range(len(self.grid)):
            for index_y in range(len(self.grid[index_x])):
                msg += str(self.grid[index_x][index_y]) + " "
            msg += "\n"
        return msg


