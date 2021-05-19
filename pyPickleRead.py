import pickle

fh = open("Teamlist", 'rb') ## Read + Binary

contest = pickle.load(fh)

fh.close()

print("contest:", contest)
print("Type of contest:", type(contest))