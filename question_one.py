#question_one(i)

def calculate_area(radius):
    area_of_the_circle = 3.14 * radius**2
    return area_of_the_circle
    print(area_of_the_circle)

calculate_area(5)
radius = 5
area_of_circle = calculate_area(radius)
print(f"The area of the circle with radius {radius} is: {area_of_circle}")

#(ii)

def sum_of_natural_numbers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)

n = 4
result = sum_of_natural_numbers(n)
print(f"The sum of natural numbers up to {n} is: {result}")

#(iii)

numbers=[1,3,5,7,9]
#removing
del numbers[2]
print(numbers)
#adding
numbers.append(10)
print(numbers)  

#(iv)
even_numbers=[2,4,6,8,10]
for a in even_numbers:
        if a%2==0:
         print (a)

#(v)
student_info={
    'name':'Alice',
    'age':20,
    'grade': 'A'
}
student_info['age'] = 25 #updating a value
print(student_info)

student_info['city'] = 'New York'
print(student_info)

#(vi)
original_dict={'a':3,
    'b':8,
    'c':2,
    'd':7
}
for value in original_dict:
    if value>5:
        print(f"new_dict is {value}")








