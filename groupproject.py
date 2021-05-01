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
    a computerguess method that purposefully limits the correct answers provided by the 
    computer to create a fair game. 
    
    The script also includes 5 functions that make the game run. 
        - The generator function creates the category that
          the players must use when inputting answers to recieve points. 
        - The point function counts the characters in each word and determines the points earned. 
        - The scorekeeping function stores and displays the points of both players.
        - The outcome function prints the winning result of the game. 
"""
import random
import string
import time 

class Humanplayer:
    """ User input words based on categories.
    
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
        
    def humanguess(self,answer_cate):
        """ Allows humanplayer to make guesses based on the category given,
        with a 10 second time limit. Adds the humanplayer inputted words 
        into list1.
        
        Args:
            answer_cate (str): the catgeory of the game provided
            from the generator function
        
        
        Side Effects: returns a list that contains the input.
        """
        starttime=time.time()     
        future = starttime + 10    
        while time.time() < future:
            humaninput=input(f"{answer_cate} category- Humanplayer guesses: ")
            self.list1.append(humaninput)
        return self.list1
  
#class Computerplayer:
    #"""Generate random words based on the given category.
    
    #Attributes: 
        #computerplayer(string)- the computerplayer.
    #"""
    
    #def __init__(self, computerplayer):
        #"""initialize computerplayer
        
        #Args: 
            #Computerplayer(string)- the computerplayer.
        #"""
        #self.computerplayer = computerplayer
        #self.wordsinput= []
        
    #def computerguess(self,answer_cate):
        #""" Allow computer to answer both correctly and incorrectly by accessing
        #different txt files of each category. 
    
        #Args: 
            #answer_cate (str)- the catgeory of the game provided
            #from the generator function
            
        #Side Effect: returns a list that contains the computerplayers guess. 
        #"""
        #wrongnumchoices= random.randint(1,5)
        #rightnumchoices= random.randint(1,10)
        #if answer_cate == "Holidays":
            #with open ("color.txt", "r", encoding="utf-8") as f: 
                #for line in f:
                    #while len(self.wordsinput) < wrongnumchoices:
                        #self.wordsinput.append(line)
            #with open ("holidays.txt", "r", encoding="utf-8") as f:
                #for line in f:
                    #while len(self.wordsinput) < rightnumchoices:
                        #self.wordsinput.append(line)           
                #return self.wordsinput
        #if answer_cate == "Colors":
            #with open("holidays.txt", "r", encoding = "utf-8") as f:
                #for line in f:
                    #while len(self.wordsinput) < wrongnumchoices:
                        #self.wordsinput.append(line)
            #with open ("color.txt", "r", encoding="utf-8") as f: 
                #for line in f:
                    #while len(self.wordsinput) < rightnumchoices:
                        #self.wordsinput.append(line)       
                #return self.wordsinput 
        #if answer_cate == "Animals":
            #with open ("foods.txt", "r", encoding= "utf-8") as f:
                #for line in f:
                    #while len(self.wordsinput) < wrongnumchoices:
                        #self.wordsinput.append(line)
            #with open ("animals.txt", "r", encoding= "utf-8") as f:
                #for line in f:
                    #while len(self.wordsinput) < rightnumchoices:
                        #self.wordsinput.append(line)        
                #return self.wordsinput
        #if answer_cate == "Food":
            #with open ("animals.txt", "r", encoding= "utf-8") as f:
                #for line in f:
                    #while len(self.wordsinput) < wrongnumchoices:
                        #self.wordsinput.append(line)
            #with open ("foods.txt", "r", encoding= "utf-8") as f:
                #for line in f:
                    #while len(self.wordsinput) < rightnumchoices:
                        #self.wordsinput.append(line)        
                #return self.wordsinput
        
  
def generator():
    """ Generate random category to start game.
        
    Return: 
        answer_cate (str): the category of the game
    """
    category_list=["Food","Color", "Holidays", "Animals"]
    answer_cate=random.choice(category_list)
    return (answer_cate)
 

def point(humanplayer, computerplayer): 
    """ Score the word. Longer words get more points. 
    Args:
        humanplayer (str): the human player of the game, object of 
        humanplayer class
        computerplayer (str): the computer player of the game, object of 
        computerplayer class
        
    Returns:
        hpoint(int)- The points humanplayer gains ranging from 2-15.
        cpoint(int)- The point computerplayer gains, ranging from 2-15.
    """
    human_answer = Humanplayer(humanplayer).humanguess()
    #computer_anwser = Computerplayer(computerplayer).mistake().wordsinput
    for word in human_answer: 
        length=len(word)
        for i in range(16): 
            if i==length:
                hpoint=i
    #for words in computer_answer:
        #length=len(word)
        #for i in range(16): 
            #if i==length:
                #cpoint=i
    #return hpoint,cpoint
    return hpoint
        
def scorekeeping(hpoint, cpoint):
    """ 
    This function calls hpoint and cpoint from the point() function, and
    prints out a current score of the game.
    
    Args: 
        hpoint(int)- The points humanplayer gains ranging from 2-15.
        cpoint(int)- The point computerplayer gains, ranging from 2-15.
    
    Side Effects: prints the current points for each player 
    """
    print(f"Current Human Score: {hpoint}")
    #print(f"Current Computer Score: {cpoint}")
        
#def outcome(humanscore,compscore):
    """ prints the final winning statement by how many points.
     
    Args: 
        humanscore (int): the total humanplayer score
        computerscore (int): the total computerplayer score
    
    Side Effects: Printing a winning statement to the console.
    """
    #if humanscore > compscore:
        #print (f"Human Player won by {humanscore- compscore}!")
    #elif humanscore < compscore:
        #print(f"Computer Player won by {compscore - humanscore}!")
    #elif humanscore == compscore:
        #print(f"Computer Player and Human Player tied with {humanscore}!")
    
def main(): 
    """Runs the entire game, by printing out category topics, computer 
    and human guesses, and winning outcome.

    Returns:
        string: multiple sentences outputted for game results
    """
    answer_cate = generator()
    print(f"The category: {answer_cate}") 
    hguess=(Humanplayer('humanplayer'))
    #h2guess= (Computerplayer('computerplayer'))
    print(f"(Humans answers are:{hguess.humanguess(answer_cate)}")
    #print (f"(Computer answers are:{h2guess.computerguess(answer_cate)}")
    #hpoint,cpoint= point(hguess,h2guess)
    #scorekeeping(hpoint,cpoint)
    #outcome(hpoint,cpoint)

     
if __name__ == "__main__": 
    main()