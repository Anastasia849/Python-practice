import doctor
import nurse
import pickle

with open('doctors_nurses.pickle', 'rb') as f:
    doctors_nurses_new = pickle.load(f)

for i in doctors_nurses_new:
    for j in i:
        print(j.all_info())
