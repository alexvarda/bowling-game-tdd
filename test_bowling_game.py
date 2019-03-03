from game import Game
import unittest



class TestBowlingGame(unittest.TestCase):


    def setUp(self):
        self.game = Game()
        
    def testAllOnes(self):
        pins = [1 for i in range(11)]
        self.game.roll(11,pins)
        self.assertEqual(self.game.score, 11)

    def testSpare(self):
        self.game.roll(11, [5,5,5,4])
        self.assertEqual(self.game.score, 24)

    def testStrike(self):
        self.game.roll(11,[10,5,4])
        self.assertEqual(self.game.score, 28)
    

if __name__ == '__main__':
    unittest.main()
