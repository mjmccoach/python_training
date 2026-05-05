def greet(time_of_day, name):
    return "Good " + time_of_day + " " + name

greeting = greet("Morning", "Matthew")
print(greeting)

name_1 = "Bob"
time_of_day_1 = "morning"
greeting = greet(time_of_day_1, name_1)
print(greeting)

name_2 = "Ada"
time_of_day_2 = "afternoon"
greeting = greet(time_of_day_2, name_2)
print(greeting)

chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]

def count_eggs( list ):
    print(list)
    total_eggs = 0

    for bird in list:
        total_eggs += bird["eggs"]
        bird["eggs"] = 0 # eggs have been collected

    return f"{total_eggs} eggs collected"

print(count_eggs(chickens))