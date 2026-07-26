# Static Method

class College:

    def __init__(self, name, ranking):
        self.name = name
        self.ranking = ranking

    def display(self):
        print("College Name :", self.name)
        print("Ranking :", self.ranking)

    @staticmethod
    def college_location():
        print("Tamil Nadu")


# Create object

kongu = College("Kongu Engineering College", 1)

# Instance method
kongu.display()

# Static method
College.college_location()

'''College Name : Kongu Engineering College
Ranking : 1
Tamil Nadu'''
