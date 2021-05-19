import pickle

team = {
    "group A" : ['India', 'England', 'NewZealand'],
    "group B" : ["SA", "WI", "AUS"]
}

fh = open("Teamlist", 'wb')   ## Write + Binary
print(fh)

pickle.dump(team, fh)

fh.close()

