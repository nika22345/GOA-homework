#day 02 saklaso davaleba for loopit

values = ["gamarjoba", 20, 25.1, True, False]

for i in range(5):
    print(values[i])


#day 03 saklaso davaleba for loopit

first_name = "Nika"
last_name = "Kalandadze"
age = 15
city = "Tbilisi"
hobby = "Programming"

info = [first_name, last_name, age, city, hobby]

for i in range(5):
    print(info[i])


#day 05 saklaso davaleba for loopit


name = input("Enter your name: ")

for i in range(1):
    print(name[0])


    name = input("Enter your name: ")
lastname = input("Enter your last name: ")

for i in range(1):
    print(f"{name} {lastname}")



    guess = input("Enter yes or no: ")

for i in range(1): 
    if guess == "yes":
        name = input("Enter your name: ")
        print(name)
        print("goodbye")



for i in range(1): 
    if input("Enter char: ") == "A":
        print(100)
    if input("Enter char: ") == "B":
        print(80)
    if input("Enter char: ") == "C":
        print(60)
    if input("Enter char: ") == "D":
        print(40)
    if input("Enter char: ") == "F":
        print("Failed")


#day 06 classwork for loopit



name = input("Enter your name: ")
for i in range(10):
    print(name)