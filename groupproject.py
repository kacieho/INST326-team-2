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
    answers for the game. For the ComputerPlayer class there is an __init__ method, a readwords method 
    that reads in the text file and inputs a random list of words for the computer answer.
    The computerplayer class also has a computerguess method that purposefully 
    limits the correct answers provided by the computer to create a fair game. 
    
    The script also includes 5 functions that make the game run. 
        - The generator function creates the category that
          the players must use when inputting answers to recieve points. 
        - The point function counts the characters in each word and determines the points earned. 
        - The scorekeeping function stores and displays the points of both players.
        - The outcome function prints the winning result of the game. 
"""
import random
import time 

class Humanplayer:
    """ User input words based on categories.
    
    Attributes: 
        HumanPlayer(str)- the humanplayer for the scategories game.
    """
    def __init__(self, humanplayer):
        """initialize humanplayer
        
        Args: 
            HumanPlayer(object)-the humanplayer for the scategories game.
        
        Side Effects: Sets attribute list1
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
        
        Side Effects: modified the self.list1
        Returns: 
            list1: return the list that contains the input.
        """
        starttime=time.time()     
        future = starttime + 10    
        while time.time() < future:
            humaninput=input(f"{answer_cate} category- Humanplayer guesses: ")
            self.list1.append(humaninput)
        return self.list1
    
  
class Computerplayer:
    """Generate random words based on the given category.
    
    Attributes: 
        computerplayer(object)- the computerplayer.
        wordsinput (list)- the list of words outputted by the computerplayer
    """
    
    def __init__(self, computerplayer):
        """initialize computerplayer
        
        Args: 
            Computerplayer(object)- the computerplayer.
        Side effect: Sets an attribute wordsinput
        """
        self.computerplayer = computerplayer
        self.wordsinput= []
        
    def readwords(self, numwords, filepath):
        """Read words and cleans words in the text file, as well as inputting
        words into wordsinput.
        
        Args:
            numwords(int): the number of words to be extended to wordsinput
            filepath(str): the name of the .txt files
            
        Side Effects: Modifying wordsinput
        """
        with open (filepath, "r", encoding="utf-8") as f:
            list2=f.readline().strip().split('\t')
        self.wordsinput.extend(random.sample(list2, numwords))
          
    def catefile(self,cate):
            """Category file
            
            Args:
                cate(str): cateory name
                
            Returns:
                return a string: category's name (lowercase) + .txt
            """
            return cate.lower()+".txt"    
    def computerguess(self,answer_cate):
        """ Allow computer to answer both correctly and incorrectly by accessing
        the correct txt file for the category, as well as an incorrect txt file. 
    
        Args: 
            answer_cate (str)- the catgeory of the game provided
            from the generator function
            
        Side Effect: modifies wordsinput
        
        Returns: 
            wordsinput: returns wordsinput that contains the computerplayers guesses. 
        """   
        wrongnumchoices= random.randint(1,3) 
        rightnumchoices= random.randint(1,3)
        cate= self.catefile(answer_cate)
        correct= self.readwords(rightnumchoices, cate)
        category_set={"Foods","Color", "Holidays", "Animals"}
        category_set.remove(answer_cate)
        cate2=self.catefile(category_set.pop())
        self.readwords(wrongnumchoices, cate2)
        return self.wordsinput
        
  
def generator():
    """ Generate random category to start game out of the provided list
    of categories.
        
    Return: 
        answer_cate (str): the category of the game
    """
    category_list=["Foods","Color", "Holidays", "Animals"]
    answer_cate=random.choice(category_list)
    return answer_cate
 

def point(answer_cate,humanplayer, computerplayer): 
    """ Scores each word in the list of answers, longer words and more words
    get more points. 
    Args:
        answer_cate(str): the name of the category
        humanplayer (object): the human player of the game, object of 
        humanplayer class
        computerplayer (object): the computer player of the game, object of 
        computerplayer class
        
    Returns:
        hpoint(int)- The points humanplayer gains
        cpoint(int)- The point computerplayer gains
    """
    if answer_cate=="Foods":
        pathfile='foods.txt'
    if answer_cate=="Color":
        pathfile='color.txt'
    if answer_cate=="Holidays":
        pathfile='holidays.txt'
    if answer_cate=="Animals":
        pathfile='animals.txt'
    with open (pathfile, 'r', encoding="utf-8") as f:
        correct_answer_list=f.readline().strip().split('\t')
        
    hpoint = 0
    cpoint = 0
    for word in humanplayer.list1: 
        human_length=len(word)
        hpoint += human_length        
    for word in computerplayer.wordsinput:
        if word in correct_answer_list:
            comp_length=len(word)
            cpoint += comp_length
    return hpoint,cpoint
   
        
def scorekeeping(hpoint, cpoint):
    """ This function calls hpoint and cpoint from the point() function, and
    prints out a current score of the game.
    
    Args: 
        hpoint(int)- The points humanplayer gains
        cpoint(int)- The point computerplayer gains
    
    Side Effects: prints the current points for each player 
    """
    print(f"Current Human Score: {str(hpoint)}\nCurrent Computer Score: {str(cpoint)}")
        
def outcome(humanscore,compscore):
    """ prints the final winning statement by how many points.
     
    Args: 
        humanscore (int): the total humanplayer score
        compscore (int): the total computerplayer score
    
    Side Effects: Printing a winning statement to the console.
    """
    if humanscore > compscore:
        print (f"Human Player won by {humanscore- compscore}!")
    elif humanscore < compscore:
        print(f"Computer Player won by {compscore - humanscore}!")
    elif humanscore == compscore:
        print(f"Computer Player and Human Player tied with {humanscore}!")
    
def main(): 
    """Runs the entire game, by printing out category topics, computer 
    and human guesses, and winning outcome.

    Returns:
        string: multiple sentences outputted for game results
    """
    answer_cate = generator()
    print(f"The category: {answer_cate}") 
    hguess=(Humanplayer('humanplayer'))
    cguess= (Computerplayer('computerplayer'))
    print(f"Humans answers are:{hguess.humanguess(answer_cate)}")
    print (f"Computer answers are:{cguess.computerguess(answer_cate)}")
    hpoint,cpoint= point(answer_cate,hguess,cguess)
    scorekeeping(hpoint,cpoint)
    outcome(hpoint,cpoint)

     
if __name__ == "__main__": 
    main()