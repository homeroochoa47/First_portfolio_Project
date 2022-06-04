#Command Line prortfolio project


def restart_input():
    restart = input("Would you like to start over? \n")
    if "y" in restart.lower():
        return script()
    elif "n" in restart.lower():
        print ("See ya!")
    else:
        print ("Enter yes or no")
        restart_input()

def first_choice():
    first_input = input("What types of photos do you want to take? (Portraits, landscapes, pics of your friends, quick snapshots or maybe a little bit of everything: \n")

    #if the person chooses portrait or landscape
    if "portrait" in first_input.lower() or "landscape" in first_input.lower():
        #global second_input #called global to reference in the next function
        second_input = input("Nice. Do you wand a camera with a fixed lens or do you want to be able to switch lenses? \n")
        return second_input

    #if they choose friends or snapshots
    elif "friends" in first_input.lower() or "snap" in first_input.lower():
        try:
             second_input = int(input("You're probably best off with a point and shoot camera. What's your budget? \n"))
             return second_input
        except: 
            print ("Please make sure to enter a numerical value (without a $)")
            return script()
    
    elif "everything" in first_input.lower():
        print("Your best bet would be the Minolta Hi-Matic 7S.")
        himatic.more_info()
        return restart_input()
    
    else: 
        print("Sorry, I didnt quite get that. Try again")
        return script()


def second_choice(choice):
    #choosing point and shoots above results in an int for price range
    if type(choice) == int:
        if choice > 0 and choice < 50:
            print("Check out the Pentax IQZoom")
            iqzoom.more_info()
            restart_input()
        elif choice > 50 and choice <= 150:
            print ("Check out the Olympus Stylus Zoom")
            stylus.more_info()
            restart_input()
        elif choice > 150:
            print ("check out the Konica Big Mini")
            bigmini.more_info()
            restart_input()
        elif choice <= 0:
            print ("Sorry, I didnt quite get that. Try again")
            return script()
   
    # an input of portraits or landscapes results in a string
    #depnding on this next choice, we either leave as a string or convert to a list and append the value
    elif type(choice) == str:
        if "fixed" in choice.lower():
            fixed_mech_or_batt_input = input("Fixed lens it is. Now, are you interested in a fully mechanical camera, or one that relies on batteries? \n")
            return fixed_mech_or_batt_input
            #results in a string output
   
        elif "switch" in choice.lower() or "lenses" in choice.lower():
            inter_mech_or_batt_input = input("So you'd prefer something with interchangeable lenses. Do you want battery powered or fully mechanical? \n")
            inputlist = []
            inputlist.append(inter_mech_or_batt_input)
            return inputlist
            #results in a list output, referenced in the "suggestion" function below
        else:
            print ("Sorry, I didnt quite get that. Try again")
            return script()


#if they chose portraits/landscapes
#picks between a str if they chose fixed lens above, or a list if they chose interchangeable lenses
def suggestion(choice):
    if type(choice) == str: 
        if "mech" in choice.lower():
            print ("You might like the Olympus 35 RC")
            olympus_rc.more_info()
            restart_input()
        elif "batt" in choice.lower():
            print ("You might like the Olympus XA")
            olympus_xa.more_info()
            restart_input()
        else:
            print("Whoops, lets try again. ")
            script()

    #if they chose interchangeable lens for portraits/landscapes
    elif type(choice) == list:
        if "mech" in choice[0].lower():
            print ("How about the Nikon FM?")
            nikon_fm.more_info()
            restart_input()
        elif "batt" in choice[0].lower():
            print ("How about the Nikon FE?")
            nikon_fe.more_info()
            restart_input()
        else:
            print("Whoops, lets try again. ")
            script()


#class of cameras with a couple of methods
class Camera:
    
    #here we add some attributes for our camera, which will be referenced as we accept inputs
    def __init__(self, name, price, type, mech_or_batt, uses ):
        self.name = name
        self.price = price
        self.type = type #rangefinder, slr, point and shoot
        self.mech_or_batt = mech_or_batt
        self.uses = uses

    #adding __repr__ to provide an option to retrieve some more details about the camera
    def __repr__(self): #need to figure out conditionals for final format
        return "The {camera} is a {type} camera which is {mech_or_batt}. It is best used for {uses} and can be bought for about ${price}.".format(camera = self.name, type = self.type, mech_or_batt = self.mech_or_batt, uses = self.uses, price = self.price)
        
    #method to ask user if they want more info about their suggested camera
    def more_info(self):
        answer = input("Would you like to learn more about this camera? \n")
        if "y" in answer:
            print(self)
        elif "n" in answer:
            print ("Happy buying!")
        else:
            print ("Enter yes or no")
            restart_input()


#adding all of the cameras as objects:
himatic = Camera("Minolta Hi-Matic 7S", 75, "fixed lens rangefinder", "fully mechanical with optional batteries", "portraits, landacapes, and snapshots. It's a great all around camera" )

iqzoom = Camera("Pentax IQZoom", 25, "point & shoot", "battery powered", "quick photos and snapshots")

stylus = Camera("Olympus Stylus Zoom", "50 to $100", "point & shoot with a good zoom lens", "battery powered", "quick photos and snapshots")

bigmini = Camera("Konica Big Mini BM-201", "150+", "high-quality fixed lens point & shoot", "battery powered", "quick photos and snapshots with the potential for portraits landscapes, and more" )

olympus_xa = Camera("Olympus XA", 125, "portable fixed lens rangefinder", "battery powered", "portraits, landscapes, and quick photos on the go too")

nikon_fm = Camera("Nikon FM", 125, "interchangeable lens SLR", "fully mechanical with optional batteries", "portraits and landscapes with and has a great selection of lenses")

nikon_fe = Camera("Nikon FE", 150, "interchangeable lens SLR", "battery powered", "portraits and landscapes with and has a great selection of lenses")

olympus_rc = Camera("Olympus 35RC", 100, "small fixed lens rangefinder","fully mechanical with optional batteries", "portraits and landscapes" )


#this is where we actully initiate the sequence of all of he functions, starting with two print statements.
print ("\n Welcome to the best friend of the modern youth: a tool that helps you figure out what film camera you should buy! What an exciting way to kick off your new hobby.\n")

print ("Lets start with a few questions to figure out the right choice for you.\n")


#the functions were made to be called within oneanother, and the script function here is called to start the input sequence
def script():
    suggestion(second_choice(first_choice()))

script()