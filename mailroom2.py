import pathlib #to do file directory stuff

#Starting list of donors
donor_dict= {"Jeremy Wright": [27.50, 15.00, 10.00],
         "Laura Denney": [50.00],
         "Bruce Wayne": [0.00],
         "Clark Kent": [3.00]}

#Empty variable for possible scope error
person =""

#start of program
def start(prompt, selection_dict):
    while True:
        option = input(prompt)
        if option not in selection_dict:
            print("Please select 1,2,3 or 4.")
            continue
        if selection_dict[option]() == 'exit':
            break


#get the name of the Donor
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
    in_list = False
    if person in donor_dict:
        in_list = True
    if in_list == False:
        print(f"{person} is not a current donor.")
        sure = input("Would you like the thank them anyway(Y/N): ")
        while (sure !='Y' and sure != 'N'):
            sure = input("Please type 'Y' or 'N': ")
        if sure == 'N':
            return
        else:
            donor_dict[person]=[]
    money = float (input("Please enter a donation amount: "))
    donor_dict[person].append(money)

    print(f'''
Dear {person},

Thank you for your donation of ${money:.2f}.

Sincerely,
The Mailroom
''')

#print report of current donors
def report():
    print("{:<20}{:10}{:10}{:10}".format("Donor Name", "| Total Given ","| Num Gifts ","| Average Gift"))
    print("____________________________________________________________")
    for people in donor_dict:
        print(f"{people:<20}${sum(donor_dict[people]):10.2f}{(len(donor_dict[people])):10}     ${(sum(donor_dict[people])/(len(donor_dict[people]))):10.2f}")

#Write thank you letter to all donors
def letters():
    for letter in donor_dict:
        with open(letter+'.txt', 'w') as outfile:
            outfile.write(f'''Dear {letter},

Thank you for your donation(s) totaling ${sum(donor_dict[letter]):.2f}

We appreciate your continued support.

Sincerely,
The Mailroom''')


#exit program
def quit():
    print('Thank you for using the Mailroom :)')
    return 'exit'

prompt = ('''What would you like to do?:
      1) Send a Thank you
      2) Create a Report
      3) Send letters to everyone
      4) Quit
      Your option 1-4: ''')

selection_dict={'1': thanks, '2': report, '3': letters, '4': quit}

start(prompt, selection_dict)