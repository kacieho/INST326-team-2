"""Header:
Group: Section0102 Group7
Member name: Yiling Du, Maham Sohail, Kacie Ho, Victoria Ha 
Topic: Scattergories
"""
import random
import string

class Humanplayer:
    """ User input words based on categories and letters
    Attributes: 
    HumanPlayer(string)- the humanplayer for the scategories game.
    
    """
    def __init__(self, humanplayer):
        """initialize humanplayer
        
        Args: 
        HumanPlayer(string)-the humanplayer for the scategories game.
        
        Side Effects:humanplayer inputs their guess to the console.
        """
        # self.humanplayer=humanplayer
        
    def humanguess(humanplayer, word):
        """ Take an input word from the humanplayer and instanciate the point() method.
        
        Args:
        word(string)- the word that the humanplayer inputs.
        
        Side Effects: print a string that contains the input.
        """
        # human_answer=input("Please enter the guessing word: ")
        # if answer correct then call point method() to know how much points get
        # dict={"Color": red, white, }
         
class Computerplayer:
    """Generate random words based on list given to it 
    The computer player could “make mistakes” 
    
    Attributes: 
    computerplayer(string)- the computerplayer.
    """
    def __init__(self, computerplayer):
        """initialize computerplayer
        
        Args: 
        Computerplayer(string)- the computerplayer.
        
        Side Effect: Print a string that contains the computerplayers guess. 
        """
    def mistake():
    """if the cate is fruit, then ...
    Calling back the text file that relates to the topic and modify 
    the file to limit what the computer is able to guess.
    
    Args: 
    
    Side Effects: 
    """
    # "color": pink, purple, yollow, 
    # if color, delete some color, 
    # limit what computer can guess
    
    # Notes: In computer player class
    # Player chooses a difficulty level based on how fast the computerplayer can generate answers
    # Text based menu to set difficulty level and/or set to default level. 
    # Give users options to change difficulty level. 
    #Generate a random number and use that to determine if the computer player will make a mistake
    #Generate a number between 0 and 1 which will determine the threshold(~50% chance, ~90%) of the percent the computer player
    # will make a mistake. Create a linear equation. Desmos
    
    

def generator():
    """Generate random letter and category to start game The Letters will be from
        a-z.The Category will be chosen from a given list of category topics.
         
        Args: (#check later: if no parameters no arguments)
        cateogory(list)- A given list of four different categories 
        to choose from to start the game. 
        letter(character)- A chosen letter from a-z to start the game. 
        
        Side Effects: Prints a category and letter for user to begin the game. 
        (Return:)
    """
    category_list=["Fruit","Color", "Holidays", "Animals"]
    letter_string=string.ascii_letters #"abcd...z + ABCD... Z"
    answer_cate=random.choice(category_list)
    answer_letter=random.choice(letter_string)
    print(f"The category is {answer_cate}, and the first letter is {answer_letter}.")
    
        
def timer():
    #Loops, Somepoint in the loop you need to check the time. 
    #Python for everybody chapter with formula for loops.
    #Before the loops start you want to capture current time and you want to check if time elapsed during 
    #during the loop. Check if time has elapsed and if so the timer ends. 
    
    """ This function will set a timer when the humanplayers input 
    screen pops up and checks if the given answer is within the time range.
    Timer will not be on screen but will be counting,
    the timer stops when the user inputs a word. 
    
    Args: 
    
    Side Effects: 
    """

def point(word): 
    """ Score the word.Longer words get more points. 
    #The function indicate the point system for the game
    
    Args:
    word(string)- one required parameter "word", the specific word
        
    Returns:
    point(integer)- The point the player gains for their turn.
    Points will range from 2-15.
    """
    # human_answer=input("Please enter the guessing word: ")
    # computer_answer=input("Please enter the guessing word: ")
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
        
def outcome(scorekeeping):
    """ prints the final statement of the outcome for who is winning
    with how many points each player has at the end of the game.
    
    Args: 
    scorekeeping(function)- Calling back the score keeping function. 
    
    Side Effects: Printing a statement to the console.
    """


     
"""Not Sure
def main():
    if __name__ == "__main__":
"""
    
    

        