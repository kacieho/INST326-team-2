from groupproject import point
import groupproject 
import builtins
from unittest import mock


#Humanplayer
def test_humanguess():
    #Color Category 
    human= groupproject.Humanplayer("humanplayer")
    with mock.patch("builtins.input", side_effect=["red"]):
        assert human.humanguess("Color") == ["red"]
    # ^ the above might be the correct way, since this
    # is the way stated on the pytest page on elms
    # for testing functions that require input answers but
    # we are still still getting errors,
    # we are working with a specific category so its more difficult
    #conclusion: joel didnt know how to help us with this test,
    # the way the bottom assert statements wont work because we
    #need to create an object of the humanplayer class like i did in
    # line 10 but it still doesnt work
    
    assert humanguess("Color")==["yellow", "blue", "orange"]
    assert humanguess("Color")==["green", "white"]
    #Foods Category 
    assert humanguess("Foods")==["apple"]
    assert humanguess("Foods")==["noodles", "hamburger"]
    assert  humanguess("Foods")==["pizza", "soup", "salad"]
    #Holidays Category
    assert humanguess("Holidays")== ["christmas"]
    assert humanguess("Holidays")== ["newyears", "hanukkah"]
    assert  humanguess("Holidays")== ["thanksgiving", "easter", "mothersday"]
    #Animals Category 
    assert humanguess("Animals")=="dog"
    assert humanguess("Animals")=="cat"
    assert  humanguess("Animals")=="zebra"
         
#Computerplayer
def test_catefile():
    computer= groupproject.Computerplayer("humanplayer")
    assert computer.catefile("Foods") == "foods.txt"
    assert computer.catefile("Holidays") == "holidays.txt"
    assert computer.catefile("Color") == "color.txt"
    assert computer.catefile("Animals") == "animals.txt"
    
#^ this is correct!!!
    
    
    
    
    
    
# other functions outside of class
def test_point():
    assert point("fruit") == 5
    assert point("APPLE") == 5
    assert point("Animal") == 6
    assert point("puppy") == 5
    assert point("WEATHER") == 7
    assert point("snow") == 4
    assert point("hi") == 2
    assert point("hello") == 5
    assert point("hellohellohell") == 14
    assert point("hellohellohello") == 15
    
def test_scorekeeping():
    assert scorekeeping(12,25) == "Current Human Score: 12" 
    "Current Computer Score: 25"
    assert scorekeeping(9,7) == "Current Human Score: 9" 
    "Current Computer Score: 7"
    assert scorekeeping(34,20) == "Current Human Score: 34" 
    "Current Computer Score: 20"
    assert scorekeeping(33,27) == "Current Human Score: 33" 
    "Current Computer Score: 27"
    assert scorekeeping(18,38) == "Current Human Score: 18" 
    "Current Computer Score: 38"

def test_outcome():
    assert outcome(10, 20) == "Computer Player won by 10!"
    assert outcome(23, 9) == "Human Player won by 14!"
    assert outcome(22, 22) == "Computer Player and Human Player tied with 22!"