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
        print("Your best bet would be the Minolta Hi-Matic 7S. It has full auto settings but can work without batteries, and has a light meter if you want to shoot manually as well.")
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
            print("check out the pentax iqzoom")
            restart_input()
        elif second_input > 50 and second_input <= 150:
            return #check out the olympus stylus
            restart_input()
        elif second_input > 150:
            return # check out the konica big mini
            restart_input()
        elif second_input <= 0:
            print ("Sorry, I didnt quite get that. Try again")
            return first_choice()


#if they chose a fixed lens for portraits/landscapes
def fixed_suggestion():
    if "mech" in fixed_mech_or_batt_input.lower():
        print ("Olympus 35 RC")
    elif "batt" in fixed_mech_or_batt_input.lower():
        return #Olympus XA
    else:
        print("Whoops, lets try again. ")
        first_choice()

#if they chose interchangeable lens for portraits/landscapes
def inter_suggestion():
    if "mech" in inter_mech_or_batt_input.lower():
        print ("Nikon FM")
    elif "batt" in inter_mech_or_batt_input.lower():
        return #Nikon FE
    else:
        print("Whoops, lets try again. ")
        first_choice()


#class of cameras that identifies the attributes of the cameras
class Camera:
    
    #here we add some attributes for our camera, which will be referenced as we accept inputs
    def __init__(self, name, price, type, lens_type, mech_or_batt, af, portraits, landscapes, friends, snapshots, ):
        self.name = name
        self.price = price
        self.type = type #rangefinder, slr, point and shoot
        self.lens_type = lens_type
        self.mech_or_batt = mech_or_batt
        self.portraits = portraits
        self.landscapes = landscapes
        self.friends = friends
        self.snapshots = snapshots

    #adding __repr__ to provide an option to retrieve some more details about the camera
    """def __repr__(self): #need to figure out conditionals for final format
        return "The {camera} is a {type} camera which is {mech_or_batt}. It is best used for {x}, {y}, and {z}. It can be bought for about {price}".format(camera = self.camera, type = self.type, mech_or_batt = self.mech_or_batt,  )
        """

#need to add in cameras and their classes, research how to make a flow chart type of thing 


print ("Welcome to the best friend of the modern youth: a tool that helps you figure out what film camera you should buy! what an exciting way to kick off your new hobby.\n")

print ("Lets start with a few questions to figure out the right choice for you.\n")

first_choice()

second_choice()

try:
    fixed_suggestion()
except:
    inter_suggestion()
