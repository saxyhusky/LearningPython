#Starting list of donors
donors= [["Jeremy Wright", 27.50, 15.00, 10.00],
         ["Laura Denney", 50.00],
         ["Bruce Wayne", 0.00],
         ["Clark Kent", 3.00]]

#Empty variable for possible scope error
person =""

#start of program
def start():
    while True:
        option = int (input('''Please choose an option:
      1) Send a Thank you
      2) Create a Report
      3) Quit
      Your option 1-3: '''))
        if option not in [1,2,3]:
            #option = int (input("Please select 1, 2, or 3: "))
            print("Please select 1,2, or 3.")
        if option == 1:
            thanks()
        elif option == 2:
            report()
        elif option == 3:
            #print("I don't know how to make it stop")
            print("STOPPED")
            break


def get_a_name():
    while True:
        person=input('''Please enter the full name of the donor
or type 'list' to see a list of current donors: ''' )
        if person == 'list':
            report()
        else:
            return person


#adds donors to list and thanks them for donation
def thanks():
    person = get_a_name()
#     while True:
#         person=input('''Please enter the full name of the donor
# or type 'list' to see a list of current donors: ''' )
#         if person == 'list':
#             report()
#         else:
#             break # <---------------------------------------------------------------------------------------LOOK HERE
     #comes back here after printing report. FIXED ---------------------------NOT FIXED SEE PROGRAM RUNNING

    in_list = False
    for donor in donors:
        if person in donor:
            in_list = True
    if in_list == False:
        print(f"{person} is not a donor.")
        sure = input("Would you like the thank them anyway(Y/N): ")
        while (sure !='Y' and sure != 'N'):
            sure = input("Please type 'Y' or 'N': ")
        if sure == 'N':
            return
        else:
            donors.append([person])
    money = float (input("Please enter a donation amount: "))
    for lst in donors:
        if person in lst:
            lst.append(money)

    print(f'''
Dear {person},

Thank you for your donation of ${money:.2f}.

Sincerely,
The Mailroom
''')
    #start()

#Prints list of donors.
#If arrived here through calling list in thanks() should return to thanks(),
#otherwise return to start()
def report(person= None): # <---------------------------------------------------------------------------------------LOOK HERE
    print("{:<20}{:10}{:10}{:10}".format("Donor Name", "| Total Given ","| Num Gifts ","| Average Gift"))
    print("____________________________________________________________")
    for people in donors:
        print(f"{people[0]:<20}${sum(people[1:]):10.2f}{(len(people)-1):10}     ${(sum(people[1:])/(len(people)-1)):10.2f}")
    #if person == 'list':
        #thanks() #FIXED - 'person' is a local variable to thanks() and needed to be passed to report() I set a default value of NONE, meaning if nothing is passed, it doesn't break, is 'list' is passed it works as planned
    #else:
        #start()


start()