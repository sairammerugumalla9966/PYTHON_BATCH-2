Assignment 12
==============================
# FILE HANDLING 
------------------

## SECTION 1: BASICS OF FILE HANDLING
--------------------------------------

### 1. Create and Write to a File

**Question:**
Write a program to:

* Create a file named `students.txt`
* Write names of 5 students into the file
* Each name should be written on a new line
* Display a success message after writing

f = open("students.txt","x")
f = open("students.txt" , "w")
f.write("Manasa Annapureddy\n")
f.write("Jyoshna Annapureddy\n")
f.write("Ravindra Reddy Pasem\n")
f.write("Lucky Reddy\n")
f.write("Rami Reddy Annapureddy\n")
print("successfully inserted 5 students names into the file")
f.close()

successfully inserted 5 students names into the file

-------------------------------------------------------------

### 2. Read Entire File Content

**Question:**
Write a program to:

* Open `students.txt`
* Read the entire content using `read()`
* Display the content on the screen

f = open("students.txt","r")
data = f.read()
print(data)
f.close()

Manasa Annapureddy
Jyoshna Annapureddy
Ravindra Reddy Pasem
Lucky Reddy
Rami Reddy Annapureddy
-----------------------------------------------------------------

### 3. Read File Line by Line

**Question:**
Write a program to:

* Open `students.txt`
* Read the file using a loop
* Print each line separately

f = open("students.txt","r")
data = f.readlines()
for i in data:
    print(i.strip())
f.close()

Manasa Annapureddy
Jyoshna Annapureddy
Ravindra Reddy Pasem
Lucky Reddy
Rami Reddy Annapureddy
--------------------------------------------------------

### 4. Count Words and Lines in File

**Question:**
Write a program to:

* Count the number of lines
* Count the total number of words in `students.txt`

**Expected Output Format Example:**
Total Lines: 5
Total Words: 5

line_count = 0
word_count = 0
f = open("students.txt","r")


for i in f:
    line_count+=1
    words=i.split()
    word_count+=len(words)

print("Total Lines:",line_count)
print("Total words:",word_count)

Total Lines: 5
Total words: 12

-----------------------------------------------------------
## SECTION 2: FILE MODES (r, w, a, r+, w+)
-----------------------------------------------------------

### 5. Demonstrate Write Mode (w)

**Question:**
Write a program to:

* Create a file `data.txt`
* Write some content into it
* Reopen the same file in write mode
* Write new content again

Observe what happens to the previous content.
Explain your observation in comments.

f = open("data.txt" , "x")
f=open("data.txt","w")
f.write("Manasa Annapureddy")
f = open("data.txt","w")
f.write("Jyoshna Annapureddy")

f.close()

when I created "data.txt" and inserted content into it ,the inserted content is visible 
but when I added new data to the same file previous data is not visible and newly inserted data is visible

-----------------------------------------------------------

### 6. Demonstrate Append Mode (a)

**Question:**
Write a program to:

* Open `students.txt` in append mode
* Add 3 new student names
* Ensure old data remains unchanged

f = open("students.txt","a")
f.write("suresh\n")
f.write("Ramesh\n")
f.write("Nandhu\n")
f.close()

-----------------------------------------------------------

### 7. Using r+ Mode

**Question:**
Write a program to:

* Open a file using `r+` mode
* Read existing content
* Add new content at the end

Explain how `r+` works in your own words.

f = open("sample.txt","r+")
data = f.read()
print(data)
f.seek(0,2)
f.write("jyoshna Annapureddy\n")

-----------------------------------------------------------
## SECTION 3: PRACTICAL TEXT FILE OPERATIONS
-----------------------------------------------------------

### 8. Search Word in File

**Question:**
Write a program to:

* Search for a specific word in `students.txt`
* Print whether the word is found or not

**Example Output:**
Rahul found in file.

OR

Rahul not found in file.

word = input("enter word")

f = open("students.txt","r")
data = f.read()
if word in data:
    print(word,"found in the file")
else:
    print(word,"not found in the file")

f.close()

enter wordManasa
Manasa found in the file

enter wordraghu
raghu not found in the file

-----------------------------------------------------------

### 9. Replace Word in File

**Question:**
Write a program to:

* Replace a word in a file
* Example: Replace "Python" with "Java"

Hint:
Read the file → Modify content → Write back to file

f = open("sample.txt","r")
data = f.read()
print(data)

f.close()
new_data = data.replace("Manasa Annapureddy" , "pandu")

f = open("sample.txt","w")
f.write(new_data)
f.close()


-----------------------------------------------------------

### 10. Copy Content from One File to Another

**Question:**
Write a program to:

* Read content from `students.txt`
* Write the same content into a new file `backup.txt`

f = open("students.txt","r")
data = f.read()
print(data)
f.close()

f = open("backup.txt" , "w")
f.write(data)
f.close()
-----------------------------------------------------------

### 11. Count Vowels in File

**Question:**
Write a program to:

* Read file content
* Count total vowels present in the file
count = 0
vowels = "aeiouAEIOU"
f = open("students.txt","r")
data = f.read()
print(data)

for i in data:
    if i in vowels:
        count+=1
print("count of vowels :" , count)

Manasa Annapureddy
Jyoshna Annapureddy
Ravindra Reddy Pasem
Lucky Reddy
Rami Reddy Annapureddy
suresh
Ramesh
Nandhu

count of vowels : 34

-----------------------------------------------------------
## SECTION 4: INTRODUCTION TO CSV FILES
-----------------------------------------------------------

### 12. Create and Write CSV File

**Question:**
Write a program to:

* Create a CSV file named `employees.csv`
* Store the following fields:

  * ID
  * Name
  * Salary
* Add at least 5 employee records

import csv
f = open("employees.csv" , "w",newline = "")
writer = csv.writer(f)
writer.writerow(["ID" , "Name" , "Salary"])
writer.writerow(["1" , "Manasa" , "50000"])
writer.writerow(["2" , "Jyoshna" , "35000"])
writer.writerow(["3" , "Pavan" , "30000"])
writer.writerow(["4" , "sunitha" , "40000"])
writer.writerow(["5" , "Ravi" , "25000"])
f.close()
-----------------------------------------------------------

### 13. Read Data from CSV File

**Question:**
Write a program to:

* Read data from `employees.csv`
* Display each row in formatted style

**Example Output Format:**
ID: 1 | Name: Sairam | Salary: 50000

import csv
f = open("employees.csv" ,"r")
reader = csv.reader(f)

for i in reader:
    print(f"ID: {i[0]} | Name: {i[1]} | Salary: {i[2]}")
       
   

f.close()

ID: ID | Name: Name | Salary: Salary
ID: 1 | Name: Manasa | Salary: 50000
ID: 2 | Name: Jyoshna | Salary: 35000
ID: 3 | Name: Pavan | Salary: 30000
ID: 4 | Name: sunitha | Salary: 40000
ID: 5 | Name: Ravi | Salary: 25000

-----------------------------------------------------------

### 14. Calculate Total Salary from CSV

**Question:**
Write a program to:

* Read `employees.csv`
* Calculate total salary of all employees

**Expected Output Example:**
Total Salary: 250000

import csv
count = 0
f = open("employees.csv","r")
reader = csv.reader(f)

for i in reader:
    if i[2].isdigit():
        count = count + int(i[2])
   
print("Total Salary",count)

f.close()

Total Salary 180000

-----------------------------------------------------------
## SECTION 5: INTRODUCTION TO JSON
-----------------------------------------------------------

### 15. Create and Write JSON File

**Question:**
Write a program to:

* Create a JSON file named `student.json`
* Store the following details:

  * Name
  * Age
  * Course
  * Marks (list of subject marks)

import json

data = {"Name" : "Manasa Annapureddy" , 
        "Age" : 23 ,
         "Course" : "CSE" , 
         "Marks" : [85,90,80,88]
       }

f = open("student.json" , "w")
json_data = json.dumps(data)
f.write(json_data)
f.close()


-----------------------------------------------------------

### 16. Read JSON File

**Question:**
Write a program to:

* Read data from `student.json`
* Display all details clearly

f = open("student.json","r")
data = f.read()
print(data)
f.close()

{"Name": "Manasa Annapureddy", "Age": 23, "Course": "CSE", "Marks": [85, 90, 80, 88]}

-----------------------------------------------------------

### 17. Update JSON Data

**Question:**
Write a program to:

* Read JSON file
* Add one more subject mark
* Write updated data back to the file
import json
f = open("student.json" , "r")
data = f.read()
print(data)
f.close()

data1 = {"Name" : "Jyoshna","Age" : 21,"Course" : "ECE" , "Marks" : [85,90,86,80]}

f = open("student.json" , "a")
data2 = json.dumps(data1,indent=4)
f.write(data2)
f.close()

-----------------------------------------------------------

### 18. Convert Dictionary to JSON and Back

**Question:**
Write a program to:

* Create a Python dictionary
* Convert it into JSON format
* Write it to a file
* Read it again
* Convert JSON back to dictionary

data = {"Name":"Manasa","Age":23,"Course":"CSE"}
print(data)
print(type(data))

import json
data1 = json.dumps(data)
print(data1)
print(type(data1))

f = open("json.txt","w")
f.write(data1)
f.close()

f = open("json.txt" , "r")
result = f.read()
print(result)

result1 = json.loads(result)
print(result1)
print(type(result1))

