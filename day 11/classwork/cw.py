
#1)მომხმარებელს შემოატანინეთ 3 რიცხვი და გამოიტანეთ მაგ სამი რიცხვის ჯამი 

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

total = num1 + num2 + num3

print("The three numbers are:", total)
#2)დაბეჭდეთ რიცხვები 10 - 1 მდე 

for i in range(10, 0, -1):
    print(i)
#3)დაბეჭდეთ 1- 100 რიცხვი მხოლოდ კენტები 

for i in range(1, 101, 2):
    print(i)
#4)დაბეჭდეთ ყველა რიცხვი რომელიც 3 ზე უნაშთოდ იყოფა 1- 100

for i in range(3, 101, 3):
    print(i)
#5)იპოვეთ 1 - 100 რიცხვის ჯამი 

n = 100
total = n * (n + 1) // 2
print("Something from 1 to 100 is:", total)