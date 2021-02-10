# Player 
class Player:
    #Name of the player
    name = " "
    #Boolean that is set to false if the jar of the Player is empty 
    jar = False

    # construtor for Player
    # parm : 
    # name : takes name as String if no name is givien default Name is set to "Player"
    # jar  : gets set to true; jar of a Player is full when created
    def __init__(self, name):
        self.name = name
        self.jar = True

    # roll the dices function
    #parm:
    # min: lowest availabel int value for the roll
    # max: highest availabel int value for the roll
    #return:
    #  val1: first roll
    #  val2: second roll
    def rollDices(self, min, max):
        if not min:
            min = 1
        if not max:
            max = 6
        val1 = random.randint(min, max)
        val2 = random.randint(min, max)
        return val1, val2

    # Is Called if the player's jar is empty
    def jarIsEmpty(self):
       self.jar = False
    #
    def setName(self, name):
        self.name = name

    #
    def getJar(self):
        return self.jar