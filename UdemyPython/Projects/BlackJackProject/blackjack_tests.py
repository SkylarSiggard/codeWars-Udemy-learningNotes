import unittest
import gameprogress 

class Testgameplay(unittest.TestCase):
    
    def test_inputs(self):
        result = gameprogress.makebet() 
        self.assertTrue(result, result in [1,2,3,4,5,6,7,8,9,10])

    def test_winners(self):
        hand = {"hearts":[5],"spades":[],"diamonds":[],"clubs":[],"hidden":[6]}
        result,message = gameprogress.winners('player',hand) 
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main() 


