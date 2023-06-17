def gpa(lst):
    avg = float((lst[0] + lst[1] + lst[2])/ len(lst))
    GPA = avg/25
    print(GPA, "is the gpa")
    


subjects = ["math", "english", "french"]
ids = []
names = []
marks1 = []
marks2 = []
marks3 = []
for j in range(3):
    y = input("Enter the name: ")
    x = int(input("Enter the id: "))
    for i in subjects:
        z = int(input("Enter the mark in {}: ".format(i)))
        
        if (len(marks1) < 3):
            marks1.append(z)
        elif (len(marks2) < 3):
            marks2.append(z)
        else:
            marks3.append(z)
    ids.append(x)
    names.append(y)
print(ids) 
print(names)
print(marks1, marks2, marks3)

gpa(marks1)
gpa(marks2)
gpa(marks3)
        

    
    