"""Header:
Group: Section0102 Group7
Member name: Yiling Du, Maham Sohail, Kacie Ho, Victoria Ha 
Topic: Scattergories
"""
import random
import string
import time 

class Humanplayer:
    """ User input words based on categories and letters.
    
    Attributes: 
        HumanPlayer(string)- the humanplayer for the scategories game.
    """
    def __init__(self, humanplayer):
        """initialize humanplayer
        
        Args: 
            HumanPlayer(string)-the humanplayer for the scategories game.
        
        Side Effects:humanplayer inputs their guess to the console.
        """
        self.humanplayer=humanplayer
        
    def humanguess(humanplayer, word):
        """ Take an input word from humanplayer and 
        instanciate the point() method and store the point in a list.
        
        Args:
            word(string)- the word that the humanplayer inputs.
        
        Side Effects: print a string that contains the input.
        """
        # human_answer=input("Please enter the guessing word: ")
        # if answer correct then call point method() to know how much points get
        # dict={"Color": red, white, }
         
class Computerplayer:
    """Generate random words based on the given category and letter.
    
    Attributes: 
        computerplayer(string)- the computerplayer.
    """
    
    def __init__(self, computerplayer):
        """initialize computerplayer
        
        Args: 
            Computerplayer(string)- the computerplayer.
        """
        self.computerplayer = computerplayer
        
    def mistake():
    """ Create intentional mistakes for computerplayer.
    
    Side Effect: Print a string that contains the computerplayers guess. 
    """
  
def generator():
    """ Generate random letter and category to start game.
          
        #Side Effects: Prints a category and letter for user to begin the game. 
        
        Return: 
            answer_cate and answer_letter.
    """
    category_list=["Fruit","Color", "Holidays", "Animals"]
    letter_string=string.ascii_letters #"abcd...z + ABCD... Z"
    answer_cate=random.choice(category_list)
    answer_letter=random.choice(letter_string)
    #print(f"The category is {answer_cate}, and the first letter is {answer_letter}.")
    return (answer_cate, answer_letter)

def timer(seconds):
    """set a timer when the humanplayer inputs and checks if answer is within time range.  
    
    Args:
        Seconds(integer)- The amount of time allowed.
        
    Side Effects: Timer starts when input statement is displayed.
    """
    #time.sleep(60*seconds)

def point(word): 
    """ Score the word. Longer words get more points. 
    Args:
        word(string)- one required parameter "word", the specific word
        
    Returns:
        point(integer)- The points player gains ranges from 2-15.
    """
    #human_answer=input("Please enter the guessing word: ")
    #computer_answer=input("Please enter the guessing word: ")
    length=len(word)
    for i in range(16): 
        if i==length:
            point=i
    return point
        
def scorekeeping(point):
    """ 
    This function calls the point() system and applies to human and computer player.
    
    Args: 
        point(integer)- The amount of points from each player from the point()system.
    
    Side Effects: Stores the points. 
    """
# when humanplayer's answer == generator() method answer_cate then humanplayer get point    
        
def outcome(scorekeeping):
    """ prints the final winning statement by how many points.
     
    Args: 
        scorekeeping(function)- Calling back the score keeping function. 
    
    Side Effects: Printing a statement to the console.
    """


     
"""Not Sure
def main():
    if __name__ == "__main__":
"""
    
    

        