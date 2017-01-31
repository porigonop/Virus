"""
describe the pawn
"""

class Pawn:
    """
    define the Pawn object
    """
    def __init__(self, color):
        """
        constructor of the pawn
        """
        self.color = color

    def change_color(self, color):
        """
        allow the user to change the color of the pawn
        """
        self.color = color
