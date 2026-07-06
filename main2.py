# A Python program with two classes — Cricket and Football —
#  that both have info() and play() methods (polymorphism), store player and score as private attributes 
# (encapsulation), and allow scores to be updated only through a setter method with validation. You use a for loop to 
# display all sports at once, try a direct attribute change to see why it fails, and then use the setter to update scores safely.

class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(self.__player)
        print(self.__score)

    def play(self):
        print(f"The player {self.__player} is playing cricket.")

    def change(self, player, score):
        self.__player = player
        self.__score = score

class Football:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(self.__player)
        print(self.__score)

    def play(self):
        print(f"The player {self.__player} is playing football.")

    def change(self, player, score):
        self.__player = player
        self.__score = score



c = Cricket("Virat", 15)
f = Football("Ronaldo", 45)

c.info()
c.play()

f.info()
f.play()

f.change("Messi", 34)
f.info()