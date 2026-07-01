# A Python program with two classes — Cricket and Football — that both have info() and play() methods (polymorphism), 
# store player and score as private attributes (encapsulation), and allow scores to be updated only through a setter method with
# validation. You use a for loop to display all sports at once, try a direct attributechange to see why it fails, and then use the 
# setter to update scores safely.

class Cricket:
    def __init__(self, player, score):
        self.player = player
        self.score = score
    
    def info(self):
        print(f"The player {self.player} has a score of {self.score}.")
    
    def play(self):
        print(f"The player {self.player} played circket.")

class Football:
    def __init__(self, player, score):
        self.player = player
        self.score = score
    
    def info(self):
        print(f"The player {self.player} has a score of {self.score}.")
    
    def play(self):
        print(f"The player {self.player} played football.")

c = Cricket("Virat", 15)
f = Football("Ronaldo", 45)

c.info()
c.play()

f.info()
f.play()
