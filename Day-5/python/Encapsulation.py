#Encapsulation

class Bankaccount:
    
    def __init__(self,customer_name,customer_num,account_num,branch):
        self.customer_name = customer_name
        self.__customer_num  = customer_num
        self.__account_num = account_num
        self.branch        = branch
        
    def __str__(self):
        Bankaccount.customer_name
        
    def get_account_num(self):
        return self.__account_num
        
    def get_customer_num(self):
        return self.__customer_num
        
    def set_customer_num(self,customer_num):
        self.__customer_num = customer_num
        
canara = Bankaccount("gokul",9965127340,6448101002744,"Chithode")
print(canara.customer_name,canara.get_customer_num(),canara.get_account_num(),canara.branch)

print("Old customer num :",canara.get_customer_num())
canara.set_customer_num(9380011993)
print("new customer num :",canara.get_customer_num())
    
        
'''gokul 9965127340 6448101002744 Chithode
Old customer num : 9965127340
new customer num : 9380011993

=== Code Execution Successful ==='''
