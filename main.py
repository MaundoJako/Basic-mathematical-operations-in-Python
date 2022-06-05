#### Number Manipulation and F Strings in Python
print(round(8/3, 2))
#### comma is the decimel points
print(8 // 3)
#### // flaw division - calculation will always be converted into a float. But if u use // then it gets put into an int.

result = 4 / 2
result /= 2
print(result)
#### this divides by 2, then divides by 2 again

#### example
score = 0
#### user scores a point
score += 1
print(score)
#### relly useful for manipulating a value based jupon its previous value

#### F Strings
score = 0
height = 1.8
is_winning = True
print(f"your score is {score}, your height is {height}, you are winning is {is_winning}")

#### add f infront of "" to make it into an f string
#### Does all the converting for you


#### TASK - calculating how many days, weeks and months left till you turn 90

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

new_age = int(age)

days_90 = (365 * 90)
days_had = (new_age * 365)
days_left = (days_90 - days_had)
#print(days_left)

weeks_90 = (52 * 90)
weeks_had = (new_age * 52)
weeks_left = (weeks_90 - weeks_had)
#print(weeks_left)
months_90 = (12 * 90)
months_had = (new_age * 12)
months_left = (months_90 - months_had)
#print(months_left)
print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left")

#Notes from teach
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message = f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left"
print(message) 