"""Header:
Group: Section0102 Group7
Member name: Yiling Du, Maham Sohail, Kacie Ho, Victoria Ha 
Topic: Scattergories
"""
import random
import string

class Humanplayer():
    """User input words based on categories and letters
    """
    def __init__(self, humanplayer):
        """initialize humanplayer
        """
        # self.humanplayer=humanplayer
        
    def humanguess():
        # human_answer=input("Please enter the guessing word: ")
        # if answer correct then call point method() to know how much points get
        # dict={"Color": red, white, }
         
class Computerplayer():
    """Generate random words based on list given to it 
    The computer player could “make mistakes”
    """
    def __init__(self, computerplayer):
        """initialize computerplayer
        """
    def method2():
    """if the cate is fruit, then ...
    """
    # "color": pink, purple, yollow, 
    # if color, delete some color, 
    # limit what computer can guess

def generator():
    """Generate random letter and category to start game
        Letter a-z
        Category from a given list of topics
    """
    category_list=["Fruit", "Weather", "Weekdays","Color", "Food", "Names", "Months","Holidays", "Animals"]
    letter_string=string.ascii_letters #"abcd...z + ABCD... Z"
    answer_cate=random.choice(category_list)
    answer_letter=random.choice(letter_string)
    print(f"The category is {answer_cate}, and the first letter is {answer_letter}.")
    
        
def timer():
    """
    Set a timer to start when input screen pops up 
    Timer will not be on screen but will be counting
    Timer stops when user inputs word and calculates if user completed in time range
    If within time range gets points if not no points
    (Testing)
    """

def point(word): 
    """The funcation indicate the point system for the game
    
    Args:
        one required parameter "word", the specific word
        
    Retruns:
        return a number (integer 2-15), which means the point
        2: the word length is 2, and the player get 2 ponits
        3: the word length is 3, and the player get 3 points
        ...
        14: the word length is 14, and the player get 14 points
        15: the word length is 15, and the player get 15 points
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
    score keeping:
    Calling point system 
    Applying to human and computer player
    """
        
def outcome(scorekeeping):
    """show the out come
    Print statement of who is winning during the time duration. 
    States how many points each player has through half point time in the game.
    Prints overall winner at the end of game
    """
     
"""Not Sure
def main():
    if __name__ == "__main__":
"""
    
    

        