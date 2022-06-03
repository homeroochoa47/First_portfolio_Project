#Command Line prortfolio project

#Welcome to the best friend of the modern youth: a tool that helps you figure out what film camera you should buy! what an exciting way to kick off your new hobby.

#lets start with a few questions to figure out the right choice for you. First off, what types of photos do you want to take? (Portraits, landscapes, pics of your friends, quick snapshots,) If you need some other ideas, enter "not sure"

#input that takes in user response


#class of cameras that identifies the attributes of the cameras
class Camera:
    
    #here we add some attributes for our camera, which will be referenced as we accept inputs
    def __init__(self, name, price, mech_or_batt, af, portraits, landscapes, friends, snapshots, street, editorial, sports ):
        self.name = name
        self.price = price
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


#camera price
# bool for what types of photography a camera is good for
# manual or auto capabilities
# fixed lens or interchangeable
# mechanical or battery operaated




#Class that defines our types of cameras
