
class Game:
    def __init__(self):
        self.score = 0
        self.pins = [0 for i in range(11)]


    def roll(self, n, pins):
        x = 0

        for pin in pins:
            self.pins[x] = pin
            x += 1

        x = 0
        spareBegin = 0
        spareEnd = 2

        for roll in range(n):
            spare = sum(self.pins[spareBegin:spareEnd])
            if self.pins[x] == 10:
                self.score = self.pins[x] + self.pins[x+1] + self.pins[x+2]
            elif spare == 10:
                self.score = spare + self.pins[x+2]
                x += 1
            else: self.score += self.pins[x]
            x += 1
            if x == 11:
                break
            
            spareBegin += 2
            spareEnd += 2



