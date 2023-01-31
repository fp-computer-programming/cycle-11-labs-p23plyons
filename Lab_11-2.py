# Author: PCL 1/31/23

#defining the dictionary
grades = {"Mid Year Project Presention":100, "Mid Year Project Proposal":100, "Mid Year Project Code":97, "Mid Year Project Reflection":93}

#Printing all grade values
print()
print("All grades")
print(grades.values())

#Printing all keys (assignment names)
print()
print("All assignment names")
for k in grades:
    print(k)

#Printing all grades (values) above 70
print()
print("Grades above 70")
for (k,v) in grades.items():
    if (v >= 70):
        print(v)

#Printing all grades (values) above 50
print()
print("Grades above 50")
for (k,v) in grades.items():
    if (v >= 50):
        print(v)