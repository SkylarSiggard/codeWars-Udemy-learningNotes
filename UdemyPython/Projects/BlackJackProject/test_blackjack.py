import unittest
import handlecard
# Practice unit testing for blackjack project. i will get there once i have a good start on the game.
dex = {'hearts':[1,2,3,4,5,6,7,8,9,10,10,10,10,11],'spades':[1,2,3,4,5,6,7,8,9,10,10,10,10,11],'diamonds': [1,2,3,4,5,6,7,8,9,10,10,10,10,11],'clubs':[1,2,3,4,5,6,7,8,9,10,10,10,10,11]}

class TestCards(unittest.TestCase):
    
    def test_start(self):
        result = handlecard.start(dex) 
        self.assertEqual(result,"Python")
        
    def test_two_word(self):
        result = handlecard.start(dex) 
        self.assertEqual(result,"Python")


if __name__ == "__main__":
    unittest.main() 

