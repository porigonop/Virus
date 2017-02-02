"""
describe the pawn
"""

class Pawn:
    """
    define the Pawn object
    """
    color_name = {}
    lst_of_name = [".", "x", "o", "+", "*"]
    iteration = 0
    def __init__(self, color):
        """
        constructor of the pawn
        """
        self.color = color
        if self.color not in Pawn.color_name:
            Pawn.color_name[color] = Pawn.lst_of_name[Pawn.iteration]
            Pawn.iteration += 1
    def change_color(self, color):
        """
        allow the user to change the color of the pawn
        """
        self.color = color
    def __repr__(self):
        if self.color is None:
            return "."
        elif self.color == "rouge":
            return "x"
        else:
            return "o"
