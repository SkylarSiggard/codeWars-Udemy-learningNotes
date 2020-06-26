import unittest
import gameprogress 

class Testgameplay(unittest.TestCase):
    
    def test_inputs(self):
        test = 1
        result = cap.cap_text(test) 
        self.assertEqual(result, 1)



if __name__ == "__main__":
    unittest.main() 



def makebet():
	choice = "Wrong"
	while choice not in ['1','2','3','4','5','6','7','8','9','10']:
		choice = input("\nMake a bet? \n")
		if choice not in [1,2,3,4,5,6,7,8,9,10]:
			print("Sorry, You need to bet at least $1 \n")	
	return int(choice)