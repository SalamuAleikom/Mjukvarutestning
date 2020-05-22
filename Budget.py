import os
import sys
import datetime
from Ultimatetracker import UltimateTracker

class Budget(Ultimatetracker):
    # def __init__(self):
    #     self.dateNow = datetime.date.today()
    #     self.budget = 0
    #     self.budget_list = []
    #     self.totalbudget = 0
    #     self.expenses = 0
    #     self.setBudget()
    def __init__(self, budget, budget_list):

        UltimateTracker.__init__(self, budget = 0, budget_list = [])

    
    def setBudget(self):
        self.=int(input("Please enter your budget today: "))

        try:
                    
            if self.budget <= 0:
                print("Please be serious and enter your budget for today!")
                self.setBudget()
            else:

                # "SPARA BUDGETEN I PROGRAMMET SÅ DEN KAN FÖLJA MED?"
                self.budget_list.append(self.budget)

                # Lägg till i TOTALT(expenses)
                self.income_sum()

                print(self.budget, "kr || Budget has been added! ", self.dateNow, "\n\n")
        except:
            print("Please enter your budget!\n")
            self.setBudget()            



        # self.setBudget()
