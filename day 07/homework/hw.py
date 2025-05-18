#1)#დაწერე პროგრამა, რომელიც while ციკლით დაბეჭდავს რიცხვებს 1-დან 10-მდე.
count = 10
while count > 0:
    print("hello")
    count = count - 1
#2)დაწერე პროგრამა, რომელიც დაბეჭდავს რიცხვებს 10-დან 1-მდე

count = 1
while count <= 10:
    print("hello")
    count = count + 1

#.3)კომენტარებით ახსენი while loop

#while loop aris ragacis usasrulod gaketeba

# 4)დაწერე პროგრამა, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას. სწორი პაროლია "python123". სანამ სწორად არ შეიყვანს, მოთხოვე თავიდან

password = 'python123'

user_password = input("Enter your password: ")

while user_password != password:
    print("Incorrect password please try again")
    user_password = input("Enter your password again: ")

print("Access granted!")
# 5)მომხმარებელმა უნდა შეიყვანოს რიცხვი n. პროგრამამ while ციკლით უნდა დაითვალოს 1-დან n-მდე რიცხვების ჯამი.
 

n = int(input("Enter a number"))
print("Enter a number")

count = 1
total = 0

while count<= n:
    total = total + count
    count = count + 1

print("sum of numbers from 1 to", n, "is", total)



