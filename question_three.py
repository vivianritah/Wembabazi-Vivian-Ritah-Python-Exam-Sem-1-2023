#(i)
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible")
else:
    print("You are not eligible")

#(iii)
def grade_students():
    python=int(input('Enter python marks:'))
    
    if python>=90 and python<=100:
        print("A")
    elif python>=80 and python<=89:
        print("B")
    elif python>=70 and python<=79:
        print("C")
    elif python>=60 and python<=69:
        print("D")
    else:
        print("F")
grade_students()

#(iv)
def grade_students():
    try:
        python=int(input('Enter python marks:'))
        
        if python>=90 and python<=100:
            print("A")
        elif python>=80 and python<=89:
            print("B")
        elif python>=70 and python<=79:
            print("C")
        elif python>=60 and python<=69:
            print("D")
        else:
            print("F")
    except ValueError:
        return 'Invalid input.'

grade_students()

#(v)
def grade_students():
    python=int(input('Enter python marks:'))
    
    if python>=90 and python<=100:
        print("A"+" "+"Excellent" )
    elif python>=80 and python<=89:
        print("B" + " " + "Excellent")
    elif python>=70 and python<=79:
        print("C" +" " +"Good")
    elif python>=60 and python<=69:
        print("D" + " " +"Satisfactory")
    else:
        print("F" + " " + "Needs Improvement")
grade_students()

#(vi)
def grade_students():
    python=int(input('Enter python marks:'))
    
    if python>=90 and python<=100:
        print("A"+" "+"Excellent" )
    elif python>=80 and python<=89:
        print("B" + " " + "Excellent")
    elif python>=70 and python<=79:
        print("C" +" " +"Good")
    elif python>=60 and python<=69:
        print("D" + " " +"Satisfactory")
    else:
        print("F" + " " + "Needs Improvement")
grade_students()





