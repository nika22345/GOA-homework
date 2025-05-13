#შემოატანინეთ მომხხმარებელს სტრინგი და გამოიტანეთ მისი პირველი ასო
name = input("enter ur name: ")
print(name [0])
#2) შემოატანინეთ მომხმარებელს ორი სტრინგი და გამოიტანეთ მათ გაერთიანება 
name = input("enter ur name: ")
lastname = input("enter your last name: ")

print(f" {name} {lastname}")
#3) შემოატანინეთ მომხმარებელს სტრინგი და თუ მომხმარებლის შემოტანილი სტრინგი არის 'yes', მაშინ შემოატანინეთ სახელი და გამოიტანეთ ის. ყველა ვარიანტში საბოლლოდ დაემშვიდობეთ 
# მომხმარებლლს მესიჯი 'goodbye' - თი

guess = input("Enter yes or no")
if guess == "yes":
    name = input("Enter ur name")
    print(name)
    print("goodbye")
#4) შემოატანინეთ მომხმარებელს ასო თუ ეს ასო არის 'A' მაშინ გამოიტანეთ რიცხვი 100, თუ ის არის 'B' - 80, თუ 'C' - 60, თუ 'D' - 40, ხოლო თუ 'F' მაშინ სიტყვა 'Failed!'
char = input("Enter char:")
if char == "A":
    print(100)

if char == "B":
    print(80)

if char == "C":
    print(60)

if char == "D":
    print(40)

if char == "F":
    print("Failed")
#ბატონი ლაშა ლომიძე — 5/9/2025 1:45 PM
#5) მომხმარებელს შემოატანინეთ ორი სტრინგი და თუ ეს სტრინგები ერთმანეთს ემთხვევა გამოიტანეთ True ხოლო თუ არ ემთხვევა გამოიტანეთ False 
#Bonus) გააკეთეთ მეხუთე if-ის გარეშე

name1 = input("Enter name1")
name2 = input("Enter name2")
if name1==name2:
    print("True")
if name1!=name2:
    print("False")


print(name1==name2)
   