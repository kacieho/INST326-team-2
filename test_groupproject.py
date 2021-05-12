from groupproject import point
import groupproject 
#Humanplayer
def test_humanguess():
    #Color Category 
    assert humanguess("Color")== "red"
    assert humanguess("Color")=="yellow"
    assert humanguess("Color")=="green"
    #Foods Category 
    assert humanguess("Foods")=="apple"
    assert humanguess("Foods")=="noodles"
    assert  humanguess("Foods")=="pizza"
    #Holidays Category
    assert humanguess("Holidays")=="christmas"
    assert humanguess("Holidays")=="newyears"
    assert  humanguess("Holidays")=="thanksgiving"
    #Animals Category 
    assert humanguess("Animals")=="dog"
    assert humanguess("Animals")=="cat"
    assert  humanguess("Animals")=="zebra"
         
#Computerplayer
def ()


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
    