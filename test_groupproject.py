from groupproject import point
import groupproject 
import builtins
from unittest import mock
import pytest 
import random   

def test_catefile():
    """Does Computerplayer.catefile() return the correct txt file? """
    computer= groupproject.Computerplayer("humanplayer")
    assert computer.catefile("Foods") == "foods.txt"
    assert computer.catefile("Holidays") == "holidays.txt"
    assert computer.catefile("Color") == "color.txt"
    assert computer.catefile("Animals") == "animals.txt"
    
def test_scorekeeping(capsys):
    """Does scorekeeping() print the correct current scores of both players?"""
    groupproject.scorekeeping(12,25)
    outer1 = capsys.readouterr()
    out1 = outer1.out
    assert out1 == "Current Human Score: 12\nCurrent Computer Score: 25\n"
    
    groupproject.scorekeeping(9,7)
    outer2 = capsys.readouterr()
    out2 = outer2.out
    assert out2 == "Current Human Score: 9\nCurrent Computer Score: 7\n"
    
    groupproject.scorekeeping(34,20)
    outer3 = capsys.readouterr()
    out3 = outer3.out
    assert out3 == "Current Human Score: 34\nCurrent Computer Score: 20\n"
    
    groupproject.scorekeeping(33,27)
    outer4 = capsys.readouterr()
    out4 = outer4.out
    assert out4 == "Current Human Score: 33\nCurrent Computer Score: 27\n"
    
    groupproject.scorekeeping(18,38)
    outer5 = capsys.readouterr()
    out5 = outer5.out
    assert out5 == "Current Human Score: 18\nCurrent Computer Score: 38\n"


def test_outcome(capsys):
    """ Does outcome() print the correct winner of the game by the point
    difference between the two players? """
    groupproject.outcome(10,20)
    outer1 = capsys.readouterr()
    out1 = outer1.out
    assert out1 == "Computer Player won by 10!\n"
    
    groupproject.outcome(23,9)
    outer2 = capsys.readouterr()
    out2 = outer2.out
    assert out2 == "Human Player won by 14!\n"
    
    groupproject.outcome(22,22)
    outer3 = capsys.readouterr()
    out3 = outer3.out
    assert out3 == "Computer Player and Human Player tied with 22!\n"
    
def test_generator():
    """ Does generator() return one of the categories in the list?"""
    random.seed(0)
    choices = [groupproject.generator() for i in range(4)]
    assert choices == ["Animals","Animals", "Foods", "Holidays"]