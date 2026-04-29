my_number = 5
value = int(input("What number am I thinking of? "))

while (value != my_number):
    value = int(input("nope! try again... "))

print("yes!")

#we give some feedback now
my_number = 5
value = int(input("What number am I thinking of? "))

while (value != my_number):
    if (value > my_number):
        print("too high")
    else:
        print("too low")
    value = int(input("try again... "))

print("yes!")