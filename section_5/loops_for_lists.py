chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]

def find_chicken_by_name( list, chicken_name ):
  for chicken in list:
    if chicken["name"] == chicken_name:
      return chicken

  return "Not Found"

print(find_chicken_by_name(chickens, "Audrey"))

def find_chicken_by_name_v2( list, chicken_name ):
  found_chicken = None
  for chicken in list:
    if chicken["name"] == chicken_name:
      found_chicken = chicken

  return found_chicken

print(find_chicken_by_name_v2(chickens, "Mabel"))

users = [
  { "user_id": 1, "first_name": "Margaret", "last_name": "Chicken" },
  { "user_id": 2, "first_name": "Bill", "last_name": "Gates" },
  { "user_id": 3, "first_name": "Steve", "last_name": "Jobs" },
  { "user_id": 4, "first_name": "Guido", "last_name": "van Rossum" },
  { "user_id": 5, "first_name": "Brendan", "last_name": "Eich" },
]

def find_user_by_id( list, user_id):
  for user in list:
    if user["user_id"] == user_id:
        return user
  return "Not found"

print(find_user_by_id(users, 4))