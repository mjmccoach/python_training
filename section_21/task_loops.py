ages = [5, 15, 64, 27, 84, 26]
odd_ages = [age for age in ages if age % 2 != 0]

print(odd_ages)

chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]

h_named_chickens = [chicken for chicken in chicken_names if chicken[0] == 'H']

print(h_named_chickens)

long_chicken_names = [chicken for chicken in chicken_names if len(chicken) >= 10]

print(long_chicken_names)

words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

first_letter_of_words = [word[0].lower() for word in words]

print(first_letter_of_words)
