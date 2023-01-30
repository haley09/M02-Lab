# M02 Lab - Case Study: If...Else and while
# This python code is going to ask for the students name and their GPAs along with letting them know if the qualify for the Dean's List ot the Honor Roll
# This code is being written by Haley Abel
firstName = (str)
lastName = (str)
count = 1
while count <=5:
    print(count)
    lastName = input("Enter your last name here: ")
    firstName = input("Enter your first name: ")
    studentGPA = float(input("Enter your GPA: "))
    count = count + 1

    if lastName == 'ZZZ':
        quit()

    if studentGPA  >= 3.5:
        print("Congratulations " + firstName + " " + lastName + ", you made it into the Dean's List!")

    elif studentGPA >= 3.25:
        print("Congratulations " + firstName + " " + lastName + ", you made it into the Honor Roll!")

    else:
        print("Unfortunately " + firstName + " " + lastName + ", you did not make it into the Dean's list or Honor Roll, better luck next time.")

