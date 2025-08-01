# Angel Chavez
# Jul 28th, 2025
# Python 3.13.5
# program that tracks characters in a video game(name, class, xp, etc)

class GameCharacter:
    """Game character class"""
    
    def __init__(self, name, character_class, health, xp):
        """Inits game character"""

        self.name = name
        self.character_class = character_class
        self.health = health
        self.xp = xp
    
    def display_info(self):
        """Displays character info"""

        print('Character Stats')
        print(f'Name: {self.name.title()}')
        print(f'Class: {self.character_class.title()}')
        print(f'Health: {self.health}')
        print(f'XP: {self.xp}\n')
    
    def gain_xp(self, amount):
        """Increases character xp by a specified amount"""

        print(f'Player "{self.name.title()}" XP increased by {amount}')
        self.xp += amount

    def level_up(self):
        """Health increase by 10 and xp reset to 0"""

        # end='; ' will get rid of the new line so that the next print statement is outputed on the same line
        # and replaces it with a semicolon and a space
        print(f'Player "{self.name.title()}" leveled up!', end='; ')
        print('Health + 10, XP reset to 0\n')
        self.health += 10
        self.xp = 0

player1 = GameCharacter('angel', 'mage', 10, 25)
player2 = GameCharacter('sam', 'warrior', 25, 5)

player1.display_info()
player2.display_info()

player1.gain_xp(50)
player1.level_up()

player1.display_info()