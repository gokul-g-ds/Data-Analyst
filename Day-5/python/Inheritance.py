class Truck:
    
    def __init__(self,Truck_name,Reg_num,Model,Wheels):
        self.Truck_name = Truck_name
        self.Reg_num = Reg_num
        self.Model = Model
        self.Wheels = Wheels
        
    def display(self):
        print("Truck_name = ",self.Truck_name)
        print("Reg_num = ",self.Reg_num)
        print("Model = ",self.Model)
        print("Wheels = ",self.Wheels)
        
class Truck_branch(Truck):
    
    def Truck_branch(self):
        print("This is Truck branch")
     
Lorry = Truck_branch("Tata",765,"TN345",16)

Lorry.Truck_branch()
Lorry.display()


'''This is Truck branch
Truck_name =  Tata
Reg_num =  765
Model =  TN345
Wheels =  16

=== Code Execution Successful ==='''
