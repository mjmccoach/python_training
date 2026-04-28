my_first_empty_dictionary = {}
my_second_empty_dictionary = dict()

meals = { "breakfast" : "yoghurt",  "lunch" : "roll", "dinner" : "steak" }
print(meals)

silly_thing = { 1 : "2", 2 : "3", 4 : False }
print(silly_thing)

print (meals["breakfast"]) #Print value associated with key 'breakfast'

#print (meals["supper"]) 
#Key error - no supper key to print value for

print ("breakfast" in meals)
# => True

print ("supper" in meals)
# => False

meals["supper"] = "pancakes"
print(meals)

meals["dinner"] = "pasta"
print(meals)

del(meals["breakfast"])
print(meals)

prize_winnings = dict()

prize_winnings["Rory"] = 20;
prize_winnings["Scottie"] = 25
prize_winnings["Tommy"] = 15

print(prize_winnings)

del(prize_winnings["Scottie"])

print(list(prize_winnings))

print(prize_winnings.keys())

print(prize_winnings.values())

#nested dictionaries

countries = {
	"uk": {
		"capital": "London",
		"population": 1000
	},
	"germany": {
		"capital": "Berlin",
		"population": 5
	}
}

print(countries)

print(countries["germany"]["population"])




