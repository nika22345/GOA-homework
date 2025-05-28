#1) შექმენი for loop- რომელიც გამოიტანს 1-100 ჩატვლით რიცხვებს და ასევე კენტია თუ ლუწი ეს რიცხვი.


for i in range(1, 101):
    if i % 2 == 0:
        print(f"{i} is even")
    if i % 2 != 0:
        print(f"{i} is odd")


2#) მომხმარებელს შემოატანინეთ რიცხვი და და გამოიტანეთ ეს რიცხვი კენტია თუ ლუწი


num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even")
if num % 2 != 0:
    print("The number is odd")




#3) მომხმარებელს შემოატანინეთ ორი რიცხვი და დაბეჭდეთ 'მეტია' თუ მეორე რიცხვი პირველზე მეტია თუ არადა დაბეჭდეთ  ''ნაკლებია"

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if b > a:
    print("Greater")
if b <= a:
    print("Smaller")




#4) მომხმარებელს შემოატანინეთ ორი რიცხვი და დაბეჭდეთ უფრო მაღალი რიცხვი 


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print(f"The higher number is: {a}")
if b > a:
    print(f"The higher number is: {b}")
if a == b:
    print("Both numbers are equal")