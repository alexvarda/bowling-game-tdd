
class Game:
    def __init__(self):
        self.rolls  = [[] for i in range(21)]
        self.current_roll = 0

    def __repr__(self):
        return str(self.rolls)

    def roll (self, pins):
        self.rolls[self.current_roll] = pins
        self.current_roll+=1

    def score (self):
        score = 0
        frameIndx = 0
        for i in range(10):
            if self.isStrike(frameIndx):
                score += 10 
                score += self.strikeBonus(frameIndx) 
                frameIndx += 1
            elif self.isSpare(frameIndx):
                score += 10 
                score += self.spareBonus(frameIndx) 
                frameIndx += 2 
            else:
                score+= self.sumofBallsinFrame(frameIndx)
                frameIndx += 2 
        return score
    

    def isSpare (self, frameIndx):
        return ((self.rolls[frameIndx] + self.rolls[frameIndx+1]) == 10)

    def spareBonus(self, frameIndx):
        return (self.rolls[frameIndx+2])

    def isStrike(self, frameIndx):
        return (self.rolls [frameIndx] == 10)

    def strikeBonus(self, frameIndx):
        return (self.rolls[frameIndx+1] + self.rolls[frameIndx+2])

    def sumofBallsinFrame(self, frameIndx):
        return ( self.rolls[frameIndx] + self.rolls[frameIndx+1] )

