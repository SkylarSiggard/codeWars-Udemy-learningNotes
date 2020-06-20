import datetime

our_time = datetime.datetime.now()

my_dates = {'year_now': our_time.year, "our_weekday": our_time.strftime('%A'), "day_now": our_time.strftime('%d'), "our_month": our_time.strftime('%m'), "month_spelled_out": our_time.strftime("%B"),'total_day_number': our_time.strftime("%j")}

my_events = {'chirstmas': [12,25], 'anniversary': [4,6], 'future_daddy': [1,7,2021], 'future_dog_daddy': [10,1]}

baby_update = 372 - int(my_dates["total_day_number"])
dog_update = 300 - int(my_dates["total_day_number"])

dog_update2 = "have a good day!"

def update():
	name = input("New Phone who dis?: ")
	if name.lower() == "skylar":
		print("You need to get ready for hunting. You need a hunting rifle and plan out the trip!! You also need your life together before that happens too!")

def dog(myname="not skylar"):
	if myname == "skylar":
		dog_update2 = str(dog_update) + " days until im a dog dad"
		print(dog_update2)
	else: 
		print("Please the correct param")

if my_dates["our_month"] == my_events["chirstmas"][0] and my_dates["day_now"] == my_events["chirstmas"][1]:
	days_til_chirstmas = "Marry Christmas!!"
else:
	if int(my_dates["total_day_number"]) > 358:
		days_til_c = 365 % int(my_dates["total_day_number"]) + 7
		days_til_chirstmas = "Christmas is " + str(days_til_c) + " days away."
	else:
		days_til_c = 358 - int(my_dates["total_day_number"])
		days_til_chirstmas = "Christmas is " + str(days_til_c) + " days away."

if my_dates["our_month"] == my_events["anniversary"][0] and my_dates["day_now"] == my_events["anniversary"][1]:
	days_til_anniversary = "Happy Anniversary!! Hope you didnt screw it up!"
elif int(my_dates["our_month"]) > 2 and int(my_dates["our_month"]) < 4:
	days_til_anniversary = "Our Anniversary is coming up! Dont mess it up!"
else:
	if int(my_dates["total_day_number"]) > 96:
		days_til_a = 365 % int(my_dates["total_day_number"]) + 96
		days_til_anniversary = "Our Anniversary is " + str(days_til_a) + " days away."
	else:
		days_til_a = 96 - int(my_dates["total_day_number"])
		days_til_anniversary = "Our Anniversary is " + str(days_til_a) + " days away."

print(f"this was before life sucked. but were still getting a dog in {dog_update}")
#print('Today is {wd} the {dn}. The month is {m} and the year is {y}.{n}Chirstmas update: {c}{n}Anniversary update: {av}{n}I will be a father in {bu} days!{n}{du}!!!' .format(n = "\n", wd = my_dates['our_weekday'], dn = my_dates['day_now'], m = my_dates['month_spelled_out'], y = my_dates['year_now'], c = days_til_chirstmas, av = days_til_anniversary, bu = baby_update, du = dog_update2))
