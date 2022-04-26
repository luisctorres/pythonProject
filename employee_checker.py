COMPANY_NAME = "Tech Inc."

EMPLOYEES = ["Alice", "Bob", "Cameron", "Dan", "Ellen", "Frank", "Grace", "Harry"]

# Welcome message + employee names listed out
print("\nWelcome to the " + COMPANY_NAME + " employee check-in\n")
print("We at " + COMPANY_NAME + " are very proud of our employees: ")
for emp_name in EMPLOYEES:
    print("-- " + emp_name)
print("\n")

# user input section (buggy code)

accept = input("Do you work for " + COMPANY_NAME + "?\n(yes/no): ")
while accept == "" or accept[0] != 'y' and accept[0] != 'n':
    accept = input("Do you work for " + COMPANY_NAME + "?\n(yes/no): ")
if accept[0] == "y":
    # we use .strip() to remove white spaces and .casefold() to ignore case sensitivity
    name = input("What is your name?\nName: ").strip().casefold()

    if name.casefold() in (emp_name.casefold() for emp_name in EMPLOYEES):
        print("Thank you " + name.capitalize() + ", you are now checked in.")
    else:
        print("You're not an employee")
else:
    print("This service is not for you. Exiting program...")
    exit()
