"""Header:
Group: Section0102 Group7
Member name: Yiling Du, Maham Sohail, Kacie Ho, Victoria Ha 
Topic: Scattergories
"""
"""Module Docstring: 
    This script creates a scategories game between a humanplayer and the computerplayer.
    The script creates 2 classes for each player (human and computer) and intializes 
    both players. For the HumanPlayer class there is an __init__ method, that initializes 
    the human player, and a  humanguess method that allows the human to input their 
    answers for the game. For the ComputerPlayer class there is an __init__ method and 
    a mistake method that purposefully limits the correct answers provided by the 
    computer to create a fair game. 
    
    The script also includes 5 functions that make the game run. 
        - The generator function creates the category and letter that
          the players must use when inputting answers to recieve points. 
        - The timer function creates a 30 second time limit for inputted answers. 
        - The point function counts the characters in each word and determines the points earned. 
        - The scorekeeping function stores and displays the points of both players.
        - The outcome function prints the winning result of the game. 
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
        self.list1= []
        
    def humanguess():
        """ Take an input word from humanplayer and 
        instanciate the point() method and store the point in a list.
        
        
        Side Effects: print a string that contains the input.
        """
        
        #Vivi 4/26: we need to print the category for the game here (call generator function)
        #still need to figure out timer
        starttime=time.time()
        while starttime >= 0:
            humaninput=input("Humanplayer guesses: ")
            self.list1.append(humaninput)
            if humaninput == "quit":
                break
        endtime=time.time()
        print(f"you took {endtime-starttime} seconds to answer question.")
        return self.list1
                 
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
        self.wordsinput= []
        
    def computerguess(computerplayer):
        """ Create intentional mistakes for computerplayer 
    
        Args: 
            computerplayer (string)- the computer player
            
        Side Effect: Print a string that contains the computerplayers guess. 
        """
        wrongnumchoices= random.randint(1,5)
        rightnumchoices= random.randint(1,10)
        if self.answer_cate == "Holidays":
            with open ("colors.txt", "r", encoding="utf-8") as f: 
                for line in f:
                    while len(self.wordsinput) < wrongnumchoices:
                        self.wordsinput.append(line)
            with open ("holidays.txt", "r", encoding="utf-8") as f:
                for line in f:
                    while len(self.wordsinput) < rightnumchoices:
                        self.wordsinput.append(line)           
                return self.wordsinput
        if self.answer_cate == "Colors":
            with open("holidays.txt", "r", encoding = "utf-8") as f:
                for line in f:
                    while len(self.wordsinput) < wrongnumchoices:
                        self.wordsinput.append(line)
            with open ("colors.txt", "r", encoding="utf-8") as f: 
                for line in f:
                    while len(self.wordsinput) < rightnumchoices:
                        self.wordsinput.append(line)       
                return self.wordsinput 
        if self.answer_cate == "Animals":
            with open ("food.txt", "r", encoding= "utf-8") as f:
                for line in f:
                    while len(self.wordsinput) < wrongnumchoices:
                        self.wordsinput.append(line)
            with open ("animals.txt", "r", encoding= "utf-8") as f:
                for line in f:
                    while len(self.wordsinput) < rightnumchoices:
                        self.wordsinput.append(line)        
                return self.wordsinput
        if self.answer_cate == "Food":
            with open ("animals.txt", "r", encoding= "utf-8") as f:
                for line in f:
                    while len(self.wordsinput) < wrongnumchoices:
                        self.wordsinput.append(line)
            with open ("food.txt", "r", encoding= "utf-8") as f:
                for line in f:
                    while len(self.wordsinput) < rightnumchoices:
                        self.wordsinput.append(line)        
                return self.wordsinput
        
  
def generator():
    """ Generate random letter and category to start game.
          
        #Side Effects: Prints a category and letter for user to begin the game. 
        
        Return: 
            answer_cate and answer_letter.
    """
    category_list=["Fruit","Color", "Holidays", "Animals"]
    answer_cate=random.choice(category_list)
    self.answer_cate=answer_cate
    return (answer_cate)
 

def point(word, humanplayer, computerplayer): 
    """ Score the word. Longer words get more points. 
    Args:
        word(string)- one required parameter "word", the specific word
        
    Returns:
        point(integer)- The points player gains ranges from 2-15.
    """
    human_answer = Humanplayer("humanplayer").human_guesses().list1
    computer_anwser = Computerplayer("computerplayer").mistake().wordsinput
    for word in human_answer: 
        length=len(word)
        for i in range(16): 
            if i==length:
                hpoint=i
        return hpoint
    for words in computer_answer:
        length=len(word)
        for i in range(16): 
            if i==length:
                cpoint=i
        return cpoint
        
def scorekeeping(point):
    """ 
    This function calls the point() system and applies to human and computer player.
    
    Args: 
        point(integer)- The amount of points from each player from the point()system.
    
    Returns:
        string- prints out current score of each player 
    
    Side Effects: Stores the points. 
    """
    humanscore = point(hpoint)
    compscore = point(cpoint)
    print(f"Current Human Score: {humanscore}")
    print(f"Current Computer Score: {compscore}")
        
def outcome(scorekeeping):
    """ prints the final winning statement by how many points.
     
    Args: 
        scorekeeping(function)- Calling back the score keeping function. 
    
    Returns:
        string- which player won and by how much
        
    Side Effects: Printing a statement to the console.
    """
    p1 = scorekeeping(humanscore)
    p2 = scorekeeping(compscore)
    if p1 > p2:
        return (f"Human Player won by {p1 - p2}!")
    elif p1 < p2:
        return (f"Computer Player won by {p2 - p1}!")
    elif p1 == p2:
        return (f"Computer Player and Human Player tied with {p1}!")
    
def main(): 
    """Runs the entire game, by printing out category and letter topics, computer 
    and human guesses, and checking if outputs were within time range.

    Returns:
        string: multiple sentences outputted for game results
    """
    print(f"The category: {generator[0]}")

    if t < 30 and t > 0:
        print (f"Human answers are: {Humanplayer('humanplayer').humanguess()}")
        print (f"Computer answers are: {Computerplayer('computerplayer').computerguess()}")
    else: 
        print (f"Human spent {humantime} for this round, answers don't count!")
        print (f"Computer spent {computertime} for this round, answers dont count!")
    return outcome()

     
#if __name__ == "__main__": 
    #going to call main()