# INST326-team-2 Project

### Summary: 
Scattergories is a game where a random category is selected and players type as many words as they know that fits the category within the timelimit. Then the score is calculated by the length of each word totaled. The player also is playing against computer player where computer player's words are selected randomly from a txt file that corresponds with the given topic. 

For the HumanPlayer class there is an `__init__` method, that initializes the human player, and a  humanguess method that allows the human to input their answers for the game. For the ComputerPlayer class there is an `__init__` method, a readwords method that reads in the text file and inputs a random list of words for the computer answer. The computerplayer class also has a computerguess method that purposefully limits the correct answers provided by the computer to create a fair game. 

### Purpose of each file in repository:
1. README.md: Introduce the program to audiences
2. animals.txt: a textfile that contains many words that belong to "Animals" category
3. color.txt: a textfile that contains many words that belong to "Color" category
4. foods.txt: a textfile that contains many words that belong to "Foods" category
5. holidays.txt: a textfile that contains many words that belong to "Holidays" category
6. groupproject.py: program code script
7. test_groupproject.py: pytest file that tests methods in groupproject.py

### Instructions from Command Line: 
1. Open command from integrated terminal of the groupproject.py file
2. Type `python3 groupproject.py` in the terminal. 
3. Terminal will output 1 of 4 categories and user can start typing words in the terminal based on that category. For example, `Holidays category- Humanplayer guesses:` users can start typing words that relate to 'Holidays' once the statement shows up. 
4. Terminal will automatically display the list of words the user typed in.
5. When the timer stops, the human and computer player answers will be outputted as a list.
6. Then the current scores of both players along with the final game outcome will be outputted automatically. 

### how to use your program and/or interpret the output of the program, as applicable
As stated above, our program is used through the command line where a humanplayer (the user) will battle the computer by inputting as many words (longer words as well) in accordance to a generated category to gain more points against the computer. The output of our program shows the process of the game, and the user can intepret how many points they have lost or won by.

### An annotated bibliography of all sources you used to develop your project. For each source, explain how you used the source.
