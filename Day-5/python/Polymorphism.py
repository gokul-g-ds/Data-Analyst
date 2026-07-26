#polymorphism  -> same method ,different behaviour

class college:
    
    def __init__(self,Top_ranking,placements,fees_structure,Total_course):
        self.Top_ranking = Top_ranking
        self.placements =placements
        self.fees_structure = fees_structure
        self.Total_course = Total_course
        
    def display(self):
        print("Top_ranking = ",self.Top_ranking)
        print("placements = ",self.placements)
        print("fees_structure = ",self.fees_structure)
        print("Total_course = ",self.Total_course)
        
class Top_tier(college):

    def kongu(self):
        print("The top tier college")
            
class mid_tier(college):
        
    def erode_arts(self):
        print("The mid tier college")
          
          
class low_tier(college):
    
    def vasavi(self):
        print("The low tier college")
        
        
TT = Top_tier(1,"100%",75000,68)
MT = mid_tier(18,"79%",67000,55)
LT = low_tier(34,"34%",25000,22)

TT.display()
MT.display()
LT.display()

TT.college()
MT.college()
LT.college()


'''Top_ranking =  1
placements =  100%
fees_structure =  75000
Total_course =  68
Top_ranking =  18
placements =  79%
fees_structure =  67000
Total_course =  55
Top_ranking =  34
placements =  34%
fees_structure =  25000
Total_course =  22

=== Code Exited With Errors ==='''
