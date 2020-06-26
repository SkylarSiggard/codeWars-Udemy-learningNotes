import unittest
import gameprogress 

class Testgameplay(unittest.TestCase):
    
    def test_inputs(self):
        result = gameprogress.makebet() 
        self.assertTrue(result, result in [1,2,3,4,5,6,7,8,9,10])



if __name__ == "__main__":
    unittest.main() 


