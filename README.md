# INST326-team-2 Project

### Summary: 
Scattergories is a game where a random category is selected and players type as many words as they know that fits the category within the timelimit. Then the score is calculated by the length of each word totaled. The player also is playing against computer player where computer player's words are selected randomly from a txt file that corresponds with the given topic. 

For the HumanPlayer class there is an `__init__` method, that initializes the human player, and a  humanguess method that allows the human to input their answers for the game. For the ComputerPlayer class there is an `__init__` method, a readwords method that reads in the text file and inputs a random list of words for the computer answer. The computerplayer class also has a computerguess method that purposefully limits the correct answers provided by the computer to create a fair game. 

### Purpose of each file in repository:
1. README.md: Introduce the program to audiences
2. animals.txt: a textfile contians many words that belong to "Animals" category
3. color.txt: a textfile contians many words that belong to "Color" category
4. foods.txt: a textfile contians many words that belong to "Foods" category
5. holidays.txt: a textfile contians many words that belong to "Holidays" category
6. groupproject.py: program code script
7. test_groupproject.py: pytest file that tests methods in groupproject.py

### Instructions from Command Line: 
1. Open command from integrated terminal of the groupproject.py file
2. Type `python3 groupproject.py` in the terminal. 
3. Terminal will output 1 of 4 categories and user can start typing words in the terminal. For example, `Holidays category- Humanplayer guesses:` users can start typing once the statement shows up. 
4. Terminal will automatically display the list of words the user typed in.
5. When timer stops, computer player answers, scores of both players, and the winner would be displayed. 

### how to use your program and/or interpret the output of the program, as applicable


### An annotated bibliography of all sources you used to develop your project. For each source, explain how you used the source.
- timer
