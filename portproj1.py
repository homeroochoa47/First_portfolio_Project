#Command Line prortfolio project

print ("Welcome to the best friend of the modern youth: a tool that helps you figure out what film camera you should buy! what an exciting way to kick off your new hobby.\n")

print ("Lets start with a few questions to figure out the right choice for you.\n")

#input that takes in user response
first_input = input("First off, what types of photos do you want to take? (Portraits, landscapes, pics of your friends, quick snapshots,) If you need some other ideas, enter \"not sure\". ")

#providing options in case user inputs "not sure"
if "not sure" in first_input.lower():
    print ("Here are some ideas: ")
    print ("street")
    print ("editorial")
    print ("sports")
    global not_sure_input
    not_sure_input = input("ready for some camera options? what type of photography are you interested in?")



#class of cameras that identifies the attributes of the cameras
class Camera:
    
    #here we add some attributes for our camera, which will be referenced as we accept inputs
    def __init__(self, name, price, type, mech_or_batt, af, portraits, landscapes, friends, snapshots, street, editorial, sports ):
        self.name = name
        self.price = price
        self.type = type #rangefinder, slr, point and shoot
        self.mech_or_batt = mech_or_batt
        self.af = af
        self.portraits = portraits
        self.landscapes = landscapes
        self.friends = friends
        self.snapshots = snapshots
        self.street = street
        self.editorial = editorial
        self.sports = sports

    #adding __repr__ to provide an option to retrieve some more details about the camera
    """def __repr__(self): #need to figure out conditionals for final format
        return "The {camera} is a {type} camera which is {mech_or_batt}. It is best used for {x}, {y}, and {z}. It can be bought for about {price}".format(camera = self.camera, type = self.type, mech_or_batt = self.mech_or_batt,  )
        """



