def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, snack):
    output = False;
    for item in person["favourites"]["snacks"]:
        if item == snack:
            output = True
    
    return output

def add_friend(person, friend):
    person["friends"].append(friend)

def remove_friend(person, friend):
    friend_index = person["friends"].index(friend)
    person["friends"].pop(friend_index)

def total_money(list):
    total = 0
    for item in list:
        total += item["monies"]
    return total

def l_money(person_loaning, person_receiving, money_loaned):
    person_loaning["monies"] -= money_loaned
    person_receiving["monies"] += money_loaned

def all_favourite_foods(people):
    all_favourite_foods = []
    for person in people:
        for favourite in person["favourites"]["snacks"]:
            if favourite not in all_favourite_foods:
                all_favourite_foods.append(favourite)
    return all_favourite_foods

def find_no_friendends(people):
    person_with_no_friends = []
    for person in people:
        print(len(person["friends"]))
        if len(person["friends"]) == 0:
            person_with_no_friends.append(person)
    return person_with_no_friends
