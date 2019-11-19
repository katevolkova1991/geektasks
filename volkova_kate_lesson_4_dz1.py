from sys import argv

name_of_script, amount_of_hours, earn_per_hour, bonus = argv

print(int(amount_of_hours) * int(earn_per_hour) + int(bonus))

