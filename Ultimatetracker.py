##### MAIN MENU #####


class UltimateTracker():
  
  def __init__(self):
        self.mainMenu()
    
    
    
  def mainMenu(self):

        print("\n****** WELCOME TO ULTIMATE TRACKER ******\n")
        print("WHAT DO YOU WANT TO DAY?:")

        try:

            print("1 = SET BUDGET")
            print("2 = SET TRANSACTION")
            print("3 = SEE HISTORY")
            print("4 = EXIT")

            selection=int(input("Enter 1-4: "))

            if selection==1:
                self.setBudget()
            elif selection==2:
                self.setTransaction()
            elif selection==3:
                self.seeHistory()
            elif selection==4:
                exit
            else:
                print("***INVALID***")
                print("Try again!")
                self.mainMenu()
        except:
            print("Write a number from 1-6 \n")
            self.mainMenu()


if __name__ == '__main__':

    UltimateTracker()

