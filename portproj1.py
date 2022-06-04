#Command Line prortfolio project

print ("Welcome to the best friend of the modern youth: a tool that helps you figure out what film camera you should buy! what an exciting way to kick off your new hobby.\n")

print ("Lets start with a few questions to figure out the right choice for you.\n")

#this function initates a couple of inputs and goes back to the start if it doesnt get an input we can use
def first_choice():
    first_input = input("What types of photos do you want to take? (Portraits, landscapes, pics of your friends, quick snapshots: \n")

    if "portrait" in first_input.lower() or "landscape" in first_input.lower():
        global second_input #called global to reference in the next function
        second_input = input("Nice. Do you wand a camera with a fixed lens or do you want to be able to switch lenses? \n")

    elif "friends" in first_input.lower() or "snap" in first_input.lower():
        try:
             second_input = int(input("You're probably best off with a point and shoot camera. What's your price range? \n"))
        except: 
            print ("Please make sure to enter a numerical value")
            return first_choice()
        
    else: 
        print("Sorry, I didnt quite get that. Try again")
        return first_choice()

first_choice()


def second_choice():
    if type(second_input) == str:
        global mech_or_batt_input
        if "fixed" in second_input.lower():
            mech_or_batt_input = input("Fixed lens it is. Now, are you interested in a fully mechanical camera, or one that relies on batteries? \n")

        elif "switch" in second_input.lower() or "lenses" in second_input.lower():
            mech_or_batt_input = input("So you'd prefer something with interchangeable lenses. Would you prefer battery powered or fully mechanical? \n")
    elif type(second_input) == int:
        if second_input > 0 and second_input < 50:
            print("check out the pentax iqzoom")
        elif second_input > 50 and second_input <= 150:
            return #check out the olympus stylus
        elif second_input > 150:
            return # check out the konica big mini
        elif second_input <= 0:
            print ("Sorry, I didnt quite get that. Try again")
            return first_choice()

second_choice()



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


