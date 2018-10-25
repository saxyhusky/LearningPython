fruit = ["Apples", "Pears", "Oranges", "Peaches"]
def series1(fruit):
    print (fruit)
    q1 = input("What fruit would you like to add: ")
    fruit.extend([q1])
    print (fruit)
    q2 = int(input("Which item would you like to view (1-5):"))
    print ("Item {} is {}".format(q2,fruit[q2-1]))
    fruit = ["Grapes"] + fruit
    print (fruit)
    fruit.insert(0, "Pineapple")
    print (fruit)
    short_fruit=[]
    for i in fruit:
        if i.startswith("P"):
            short_fruit = [i] + short_fruit
    print (short_fruit)

def series2(fruit):
    print(fruit)
    fruit.pop(len(fruit)-1)
    print(fruit)
    q3 = input("What fruit would you like to delete: ")
    while q3 not in fruit:
        q3 = input("I could not find that fruit. Please try again: ")
    fruit.remove(q3)
    print (fruit)

def series3(fruit):
    for i in fruit[:]:
        q4 = input("Do you like {}? Yes/No: ".format(i.lower()))
        while (q4  != "Yes" and q4 != "No"):
            q4 = input("Please type 'Yes' or 'No': ")
        if q4 == "No":
            fruit.remove(i)
    print (fruit)

def series4(fruit):
    bass_ackwards= fruit[:]
    x=0
    for i in bass_ackwards:
        bass_ackwards[x]=i[::-1]
        x+=1
    fruit.pop(len(fruit)-1)
    print (fruit)
    print (bass_ackwards)

#series1(fruit[:])
#series2(fruit[:])
#series3(fruit[:])
series4(fruit[:])