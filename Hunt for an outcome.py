##Hunt For an Outcome
##By Chase Cole
##12/8/21 6:18PM

##imports random function
import random
##Gets username from input 
userName = input("What is the name of your character ")
##lucky number generation
luckynumber = random.randint(1,25)
searchFF = int(0)
searchWW = int(0)
searchFFo = int(0)
searchCC = int(0)
##Locations
##Frozen Fjord
##Wasted Wastes
##Forgotten Forest
##Crumbling Caverens
location = int(0)
while location <= 4:
    print("Where would you like to go?")
    print("Frozen Fjord? Please enter 1 \n " )
    print("Wasted Wastes? Please enter 2 \n " )
    print("Forgotten Forest? Please enter 3 \n " )
    print("Crumbling Caverens? Please enter 4 \n " )
    print("To quit the expedition..Please enter 5 \n " )
    location = int(input())
    if location != int(location):
        print("Try again commander? I hope you did not hit your head...")
    if  location == int(1):
        print("Good Choice! To the Frozen Fjord we go!\n\n")
        print("   XXX            XXXXXX           XXX \n")
        print("  XXXXX          XXXXXXXXX        XXX\n")
        print(" XXXXXXX          XXXXXXX        XXX\n")
        print(" XXXXXXX                        XXX\n")
        print(" XXXXXXXX                      XXX\n")
        print(" XXXXXXXXXX      XXXXXXX     XXX\n")
        print(" XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        while searchFF != '3':
            print("where would you like to search?")
            print("Frozen Pond? Please enter 1 \n " )
            print("Yeti Cave? Please enter 2 \n " )
            print("The Fridged Peak? Please enter 3 \n " )
            searchFF = input('')
            if searchFF == '1':
                print("Nothing of intrest! Please try again!")
            elif searchFF == '2':
                print("Nothing of intrest! Please try again!")
            elif searchFF == '3':
                print("You see something sticking out of the top of the peak")        
                print("You continue to dig")
                print("You found the Frozen Crown")
                print("X   X   X")
                print("XXXXXXXXX")
                print("xxxxxxxxx")
            else:
                print("Commander! That is not a location")
    elif  location == int(2):
        print("Good Choice! To the Wasted Wastes we go!\n\n")
        print(" XX   XXXXX X    XX   XXX     XXX\n")
        print(" XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        while searchWW != '2':
            print("where would you like to search?")
            print("Endless Pit? Please enter 1 \n " )
            print("Wolf Cave? Please enter 2 \n " )
            print("Doom Sayer's Hill? Please enter 3 \n " )
            searchWW = input('')
            if searchWW == '1':
                print("Nothing of intrest! Please try again!")
            elif searchWW =='3':
                print("Nothing of intrest! Please try again!")
            elif searchWW == '2':
                print("You see something in a pile of bones")        
                print("You continue to dig")
                print("You found the Wolf's Bane")
                print("  x")
                print("  x")          
                print("  x")  
                print("  x")           
                print("  x")         
                print("  x")  
                print("XXXXX")          
                print("  X")
                print("  X")
            else:
                print("Commander! That is not a location")
    elif  location == int(3):
        print("Good Choice! To the Forgotten Forest we go!\n\n")
        print("\n")
        print("\n")
        print("  xxx                         \n")
        print("  xxx   xxx               xx  \n")
        print("  xxx   xxx              xxxx \n")
        print("   x     x              xxxxxx\n")
        print("   x     x    xxx       xx  xx\n")      
        print("   x     x    xxx       xxxxxx\n")
        print(" XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        while searchFFo != '1':
            print("where would you like to search?")
            print("The lost house? Please enter 1 \n " )
            print("Bushes? Please enter 2 \n " )
            print("The Tree's? Please enter 3 \n " )
            searchFFo = input('')
            if searchFFo == '2':
                print("Nothing of intrest! Please try again!")
            elif searchFFo == '3':
                print("Nothing of intrest! Please try again!")
            elif searchFFo == '1':
                 print("You see something off inside the house")        
                 print("You pull it from the wall")
                 print("You found the your name on a plaque! How Strange!")                 
                 print("XXXXXXXXXXXXXXX")  
                 print("XXXXX" + userName + "XXXXX")          
                 print("XXXXXXXXXXXXXXX")
            else:
                print("Commander! That is not a location")    
    elif  location == int(4):
        print("Good Choice! To the Crumbling Caverns we go!\n\n")
        print(" XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        print(" XX   XXXXXX   x     XXX      XXX\n")        
        print(" XX   XXXXXX         XXX      XXX\n")
        print(" XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        while searchCC != '2':
            print("where would you like to search?")
            print("Go forward? Please enter 1 \n " )
            print("Take a left? Please enter 2 \n " )
            print("Go right? Please enter 3 \n " )
            searchCC = input('')
            if searchCC == '3':
                print("Nothing of intrest! Please try again!")
            elif searchCC == '1':
                print("Nothing of intrest! Please try again!")
            elif searchCC == '2':
                print("You see something in a mysterious pile of rocks")        
                print("You continue to dig")
                print("You found the valueable gem!")
                print("   X")
                print("  XXX")          
                print(" XXXXX ")  
                print("  XXX")           
                print("   X") 
            else:
                print("Commander! That is not a location")
print("Welcome back from the expedition, time for some rest")

          
