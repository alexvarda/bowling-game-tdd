from game import Game
import unittest



class TestBowlingGame(unittest.TestCase):


    def setUp(self):
        self.game = Game()
        
    def rollMany (self, n , pins):
        for i in range(n):
            self.game.roll(pins)

    def testGutterGame(self):
        self.rollMany(20,0)
        self.assertEqual(self.game.score(), 0)


    def testAllOnes(self):
        self.rollMany(20,1)
        self.assertEqual(self.game.score(), 20)

    def testOneSpare(self):
        self.game.roll(5) 
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(17,0)
        self.assertEqual(self.game.score(),16 )

    def testOneStrike(self):
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        self.rollMany(16,0)
        self.assertEqual(self.game.score(),24 )

    def testPerfectGame(self):
        self.rollMany(12,10)
        self.assertEqual(self.game.score(), 300)



if __name__ == '__main__':
    unittest.main()





