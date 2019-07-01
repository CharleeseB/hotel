HotelGuest ={
    '1': {
        '101': ['George Jefferson', 'Wheezy Jefferson'],
        "102": [ ],
        "103": [ ],
        "100": []
},
    '2': {
        '200': ['Jack Torrance', 'Wendy Torrance'],
        "201":[],
        "202":[],
        "203":[]
},

}



Guest_name =(" ")
def Menu():
    option = input("Welcome to Charleese's Cabin. To check in enter 1. To check out enter 2. To quit enter 3. ")
    if option == "1" :
        print(" Welcome to the cabin lets checkin ")
        Checkin()
    elif option == "2" :
        Checkout()
    else:
        print ("Goodbye")

def Checkin():
    New_guest = 0
    Floor_num = input("Which floor would you like? 1 or 2?")
    if Floor_num == "1":
        floor_room_num = input("which room number would u like? 100,101,102,103 ")
    else:
        floor_room_num = input("which room number would u like? 200,201,202,203 ")
    while floor_room_num not in HotelGuest[Floor_num].keys() :
        print ("That room is not available")
        print("Please choose another room? ")
        floor_room_num = input("which room number would u like? ")
    while len(HotelGuest[Floor_num][floor_room_num]) > 0:
        print ("That room is taken. Try  another room.")
        floor_room_num = input("Please choose another room? ")
    New_guest = int(input("How many guests?"))
    for _ in range(New_guest):
        Guest_name = input("What are the names for the room? ")
        print ("Thank you for providing your name " + (Guest_name))
        Room_choice = HotelGuest[Floor_num]
        Room_choice[floor_room_num].append(Guest_name)
    print (HotelGuest)
Menu()

def Checkout():
    Floor_num = input("Which floor Are you on? ")
    floor_room_num = input("which room number would u like to check out of? ")
    while len(HotelGuest[Floor_num][floor_room_num]) < 1:
        Floor_num = input("Which floor Are you on? ")
        floor_room_num = input("which room number would u like to check out of? ")
    print ("Thank you for staying with us. " )
    HotelGuest[Floor_num][floor_room_num] = []

print (HotelGuest)
Menu()

