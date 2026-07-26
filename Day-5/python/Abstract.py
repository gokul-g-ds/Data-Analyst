# Abstraction

from abc import ABC, abstractmethod


class College(ABC):

    def __init__(self, Top_ranking, placements, fees_structure, Total_course):
        self.Top_ranking = Top_ranking
        self.placements = placements
        self.fees_structure = fees_structure
        self.Total_course = Total_course

    @abstractmethod
    def college_type(self):
        pass


class Top_tier(College):

    def college_type(self):
        print("This is a Top Tier College")


class Mid_tier(College):

    def college_type(self):
        print("This is a Mid Tier College")


class Low_tier(College):

    def college_type(self):
        print("This is a Low Tier College")


# Create objects

TT = Top_tier(1, "100%", 75000, 68)
MT = Mid_tier(18, "79%", 67000, 55)
LT = Low_tier(34, "34%", 25000, 22)


# Calling methods

TT.college_type()
MT.college_type()
LT.college_type()

'''This is a Top Tier College
This is a Mid Tier College
This is a Low Tier College'''
