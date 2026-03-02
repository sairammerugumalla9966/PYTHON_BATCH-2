
# File handling 

# sairam,trainer,28,sairam@gamil.com,50000 ---->> CSV 


# {name':"sairam",'jobrole':"trainer" ----> JSON }
'''
f = open("sample.txt", "r") # open(filename/filepath , mode)
data = f.read()
print(data)
f.close()

f = open("sample.txt", "r")
print(f.read(10))
f.close()


# read() ---> read the entire file . 

f = open("sample.txt", "w")
data=f.write("sample program")
print(data)
f.close()


f = open("sample.txt", "a")
f.write("\nNew line 1 added")
f.write("\nNew line 2 added")
f.write("\nNew line 3 added")
f.write("\n line 4 added")
f.close()



f = open("newfile.txt", "x") # create 
f.write("New file created")
f.close()


f = open("image.jpg", "rb")
data = f.read()
print(type(data))
f.close()



f = open("sample.txt", "r")
print(f.read())    # reads entire file 
f.close()

f = open("sample.txt", "r")
print(f.read(5))  # reads no of characters 
f.close()

f = open("sample.txt", "r")
print(f.readline())   # reads one line at a time 
f.close()

f = open("sample.txt", "r")
print(f.readlines()) # reads multiple lines 
f.close()



f = open("sample.txt", "r")
for line in f:
    print(line.replace(","," "))
f.close()




# CSV --> comma seperated values 

# 

import csv

with open("sai.csv" , "w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name","age"])
    writer.writerow(["sairam","29"])
    writer.writerow(["sathwik","25"])
    writer.writerow(["naseem","23"])



import csv

with open("sai.csv" , "r") as f:
    reader=csv.reader(f)

    for i in reader:
        print(i)

'''

import json

data = {"name":"sairam","age":29}
json_data = json.dumps(data)
print(json_data)
print(type(data))



