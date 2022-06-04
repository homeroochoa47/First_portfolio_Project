#Command Line prortfolio project

def restart_input():
    restart = input("Would you like to start over? \n")
    if "y" in restart.lower():
        return first_choice()
    elif "n" in restart.lower():
        print ("See ya!")
        exit()
    else:
        print ("Enter yes or no")
        restart_input()

def first_choice():
    first_input = input("What types of photos do you want to take? (Portraits, landscapes, pics of your friends, quick snapshots or maybe a little bit of everything: \n")

    #if the person chooses portrait or landscape
    if "portrait" in first_input.lower() or "landscape" in first_input.lower():
        global second_input #called global to reference in the next function
        second_input = input("Nice. Do you wand a camera with a fixed lens or do you want to be able to switch lenses? \n")

    #if they choose friends or snapshots
    elif "friends" in first_input.lower() or "snap" in first_input.lower():
        try:
             second_input = int(input("You're probably best off with a point and shoot camera. What's your budget? \n"))
        except: 
            print ("Please make sure to enter a numerical value (without a $)")
            return first_choice()
    
    elif "everything" in first_input.lower():
        print("Your best bet would be the Minolta Hi-Matic 7S.")
        himatic.more_info()
        return restart_input()
    
    else: 
        print("Sorry, I didnt quite get that. Try again")
        return first_choice()


def second_choice():
    # an input of portraits or landscapes results in a string
    if type(second_input) == str:
        global fixed_mech_or_batt_input
        global inter_mech_or_batt_input
        if "fixed" in second_input.lower():
            fixed_mech_or_batt_input = input("Fixed lens it is. Now, are you interested in a fully mechanical camera, or one that relies on batteries? \n")
   
        elif "switch" in second_input.lower() or "lenses" in second_input.lower():
            inter_mech_or_batt_input = input("So you'd prefer something with interchangeable lenses. Would you prefer battery powered or fully mechanical? \n")
        

    #choosing point and shoots above results in an int for price range
    elif type(second_input) == int:
        if second_input > 0 and second_input < 50:
            print("Check out the Pentax IQZoom")
            iqzoom.more_info()
            restart_input()
        elif second_input > 50 and second_input <= 150:
            print ("Check out the Olympus Stylus Zoom")
            stylus.more_info()
            restart_input()
        elif second_input > 150:
            print ("check out the Konica Big Mini")
            bigmini.moreinfo()
            restart_input()
        elif second_input <= 0:
            print ("Sorry, I didnt quite get that. Try again")
            return first_choice()


#if they chose a fixed lens for portraits/landscapes
def fixed_suggestion():
    if "mech" in fixed_mech_or_batt_input.lower():
        print ("You might like the Olympus 35 RC")
        olympus_rc.more_info()
        return restart_input
    elif "batt" in fixed_mech_or_batt_input.lower():
        print ("You might like the Olympus XA")
        olympus_xa.more_info()
        return restart_input
    else:
        print("Whoops, lets try again. ")
        first_choice()

#if they chose interchangeable lens for portraits/landscapes
def inter_suggestion():
    if "mech" in inter_mech_or_batt_input.lower():
        print ("How about the Nikon FM?")
        nikon_fm.more_info()
        return restart_input
    elif "batt" in inter_mech_or_batt_input.lower():
        print ("How about the Nikon FE?")
        nikon_fe.more_info()
        return restart_input
    else:
        print("Whoops, lets try again. ")
        first_choice()


#function that asks if the user wants more info on their camera -- calls the repr in the camera class

#class of cameras that identifies the attributes of the cameras
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
            print ("See ya!")
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



print ("Welcome to the best friend of the modern youth: a tool that helps you figure out what film camera you should buy! what an exciting way to kick off your new hobby.\n")

print ("Lets start with a few questions to figure out the right choice for you.\n")

first_choice()

second_choice()

try:
    fixed_suggestion()
except:
    inter_suggestion()
