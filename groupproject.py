"""Header:
Group: Section0102 Group7
Member name: Yiling Du, Maham Sohail, Kacie Ho, Victoria Ha 
Topic: Scattergories
"""

"""Yiling Du added test example"""
"""hi kacie"""
"""hi this is vivi"""
'''This is Maham'''

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
    length=len(word)
    for i in range(16):
        if i==length:
            point=i
    return point

def score():
    """
    score keeping:
    Calling point system 
    Applying to human player
    """