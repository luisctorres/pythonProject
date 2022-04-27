
Students = ["Alice", "Bob", "Cameron", "Dan", "Ellen", "Frank", "Grace", "Harry"]

print("Are you a student? \nLets find out…")

accept = input("Are you a student? \n(yes/no)")
while accept == "" or accept[0] != 'y' and accept[0] != 'n':
    accept = input("Are you a student? \n(yes/no)")

if accept[0] == "y":
    name = input("What is your name?")
    if name.casefold() in (stu_name.casefold() for stu_name in Students):
        print("Welcome to class " + name.capitalize())
    else:
        print("You’re not supposed to be here")
else:
    print("You’re not supposed to be here")
    exit()