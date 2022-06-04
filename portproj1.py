#Command Line prortfolio project

print ("Welcome to the best friend of the modern youth: a tool that helps you figure out what film camera you should buy! what an exciting way to kick off your new hobby.\n")

print ("Lets start with a few questions to figure out the right choice for you.\n")

#input that takes in user response
#in the future: make sure user can only do one input at a time
#first_input = input("First off, what types of photos do you want to take? (Portraits, landscapes, pics of your friends, quick snapshots: ")


#providing options in case user inputs "not sure"
def first_choice():
    first_input = input("What types of photos do you want to take? (Portraits, landscapes, pics of your friends, quick snapshots: ")
    if "portrait" in first_input.lower() or "landscape" in first_input.lower():
        global second_input
        second_input = input("Nice. Do you wand a camera with a fixed lens or do you want to be able to switch lenses?")
        pass
        #need to figure out how to sort through all of the cameras
    elif "friends" in first_input.lower() or "snapshots" in first_input.lower():
        second_input = int(input("You're probably best off with a point and shoot camera. What's your price range? "))
        pass
    else: 
        print("Sorry, I didnt quite get that. Try again")
        return first_choice()

first_choice()

#called global in the last if statement in order to break up the conditionals into separate chunks. Didnt want one massive if statement to dictate the whole program





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


