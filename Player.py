
class Player(object):
    """
    Takes 4 arguments :
        The name of the player
        The color he chooses
        The number of points he has
        The name of the adversary
    Takes two method :
        get_adversary()
        set_adversary()
    """
    def __init__(self, player_name, player_color):
        """ Is the constructor of the class player"""
        self.adversary = None
        self.name = player_name
        self.color = player_color
        self.points = 0

    def get_adversary(self):
        """ Returns the adversary of the player """
        return self.adversary

    def set_adversary(self, adversary):
        """ Returns the adversary entered by the player"""
        if self.adversary is None:
            self.adversary = adversary
        return self.adversary

    def jouer(self, grid):
        """ Takes the inputs of the player and makes him play"""
        while True:
            pos = input("What is the position you want to conquer")
            pos = pos.split(" ")
            pos_x = pos[0]
            pos_y = pos[1]
            if grid.add_a_pawn(self, pos_x, pos_y):
                break
            