# Reading and writing in files using pickle
import pickle

Omkar = {'key': 'Omkar', 'name': 'Omkar Pathak',
         'age': 21, 'pay': 40000}
Jagdish = {'key': 'Jagdish', 'name': 'Jagdish Pathak',
           'age': 50, 'pay': 50000}

dic = {}
dic["Omkar"] = Omkar
dic["Jagdish"] = Jagdish

# Writing data
with open("1.txt", "wb") as first:
    pickle.dump(dic, first)
    pickle.dump("Second String", first)

# Reading data
with open("1.txt", "rb") as first:
    data = pickle.load(first)
    str = pickle.load(first)

print(str)
for key in data:
    print(f"{key} ==> {data[key]}")
