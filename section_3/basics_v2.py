users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)

print(users["Jonathan"]["twitter"])

# 2. Get Erik's hometown

print(users["Erik"]["home_town"])

# 3. Get the array of Erik's lottery numbers

print(users["Erik"]["lottery_numbers"])

# 4. Get the species of Avril's pet Monty

print(users["Avril"]["pets"][0]["species"])

# 5. Get the smallest of Erik's lottery numbers

eriks_lottery_numbers = users["Erik"]["lottery_numbers"]
print(min(eriks_lottery_numbers))

# 6. Return an array of Avril's lottery numbers that are even

avrils_lottery_numbers = users["Avril"]["lottery_numbers"]
avrils_evens = []
for number in avrils_lottery_numbers:
    if number % 2 == 0:
        avrils_evens.append(number)

print(avrils_evens)
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers

eriks_lottery_numbers = users["Erik"]["lottery_numbers"]
eriks_lottery_numbers.append(7)

print(eriks_lottery_numbers)

# 8. Change Erik's hometown to Edinburgh

users["Erik"]["home_town"] = "Edinburgh"
print(users["Erik"]["home_town"])

# 9. Add a pet dog to Erik called "Fluffy"

eriks_pets = users["Erik"]["pets"]
eriks_pets.append({"species: dog", "name: Fluffy"})
print(eriks_pets)

# 10. Add another person to the users dictionary