from Grid import Grid
from Player import Player

class VirusGame:

    def __init__(self, grille_lenght):
        """
        constructor of the virusgame, initialize the name and color of the Player
        and create the grid
        """
        self.grid = Grid(grille_lenght)
        player1_name = "toto"#input("name of player 1 :")
        player1_color = "bleu"#input("color of player 1 :")
        self.player1 = Player(player1_name, player1_color)
        player2_name = "tata"#input("name of player 2 :")
        player2_color = "rouge"#input("color of player 2 :")
        while player2_name == player1_name or player2_color == player1_color:
            print("please choose a valid color and name")
            player2_name = input("name of player 2 :")
            player2_color = input("color of player 2 :")

        self.player2 = Player(player2_name, player2_color)

        self.player1.set_adversary(self.player2)
        self.player2.set_adversary(self.player1)
        self.player = self.player1
    def play(self):
        """
        launch the game
        """
        print(self.grid)
        if self.grid.is_finished():
            return False

        self.player.play(self.grid)
        self.player = self.player.get_adversary()

if __name__ == "__main__":
    GAME = VirusGame(3)
    GAME.play()
