# D2/L22 -  Mathematical Operations in Python
print(type(3*6))
#Gives u the type

print (2**2)
#Gives the power to ---- 2 * 2 * 2

#TASK - Calculating BMI

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

height1 = float(height)
weight1 = int(weight)

result = int(weight1 / (height1 * height1))

print(result)

# OR

#bmi = int(weight) / float(height) ** 2 
#bmi_int = int(bmi)
#print(bmi_int)