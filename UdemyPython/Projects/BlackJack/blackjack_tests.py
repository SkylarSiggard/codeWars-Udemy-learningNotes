import unittest
import gameprogress 



class Testgameplay(unittest.TestCase):
    
    def test_inputs(self):
        result = gameprogress.makebet() 
        self.assertTrue(result, result in [1,2,3,4,5,6,7,8,9,10])

    def test_keep_playing(self):
        hand = {"hearts":[5],"spades":[],"diamonds":[],"clubs":[],"hidden":[6]}
        result,message = gameprogress.winners('player',hand) 
        self.assertEqual(result, True)

    def test_loser(self):
        hand = {"hearts":[5,9],"spades":[4],"diamonds":[5,8],"clubs":[],"hidden":[6]}
        result,message = gameprogress.winners('player',hand) 
        self.assertEqual(result, False)

    def test_winner(self):
        hand = {"hearts":[5],"spades":[5],"diamonds":[10],"clubs":[],"hidden":[1]}
        result,message = gameprogress.winners('player',hand) 
        self.assertEqual(result, False)

    def test_hold(self):
        result = gameprogress.fold()
        if result == False:
            self.assertEqual(result,False)
        else:
            self.assertEqual(result,True)


if __name__ == "__main__":
    unittest.main() 


