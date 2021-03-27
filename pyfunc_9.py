# Args

def printplayerdetails(name, age, team):
    print("Player Details: ")
    print("Name: {}, Age: {}, Team: {}".format(name, age, team))


printplayerdetails("Virat", 33, "RCB")


msd = ("MS Dhoni", 37, "CSK")
printplayerdetails(msd[0], msd[1], msd[2])


printplayerdetails(*msd)


# Packing & Unpacking     *
# Args