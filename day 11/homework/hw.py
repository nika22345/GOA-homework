#1) შემოაყვანინეთ მომხმარებელს n რიცხვი და დაპრინტეთ ყველა რიცხვი ნოლიდან n+1-მდე

n = int(input("Enter a number n: "))

for i in range(0, n + 2):
    print(i)


#2) მომხმარებელს სთხოვე შეიყვანოს თავისი ასაკი და მიუთითოს, აქვს თუ არა სტუდენტური ბარათი.
#შემდეგ:
#თუ ასაკი ნაკლებია 18-ზე ან სტუდენტური ბარათი აქვს → დაბეჭდე "დანაზოგი გაქვს!"
#თუ ასაკი 60 ან მეტია და არ აქვს ბარათი → დაბეჭდე "პენსიონერის ფასდაკლება გაქვს!"
#სხვა შემთხვევაში → "ფასდაკლება არ გეკუთვნის."

age = int(input("Enter your age: "))
student_card = input("Do you have a student card? (yes/no): ")

if age < 18 or student_card == "yes":
    print("You get a discount!")

if age >= 60 and student_card != "yes":
    print("You get a senior discount!")

if not (age < 18 or student_card == "yes") and not (age >= 60 and student_card != "yes"):
    print("No discount available.")
3#) მომხმარებელს სთხოვე შეიყვანოს ორი რიცხვი. შემდეგ:
#თუ ორივე რიცხვი დადებითია → დაბეჭდე "ორივე დადებითია"
#თუ მხოლოდ ერთი დადებითია → "მხოლოდ ერთი დადებითი რიცხვია"
#თუ არცერთი არ არის დადებითი → "არცერთი არ არის დადებითი"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > 0 and num2 > 0:
    print("Both numbers are positive")

if (num1 > 0 and num2 <= 0) or (num1 <= 0 and num2 > 0):
    print("Only one number is positive")

if num1 <= 0 and num2 <= 0:
    print("Neither number is positive")
#4) მომხმარებელი შეიყვანს ორ რიცხვს და ოპერაციას (+, -, *, /)
#დაბეჭდე შედეგი შესაბამისი მოქმედებით.
#თუ ოპერაცია არასწორია (მაგ 0-ს გაყოფა ან ტექსტი ან უცხო სიმბოლო) → "არასწორი ოპერაცია!"

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(num1 + num2)

if operation == "-":
    print(num1 - num2)

if operation == "*":
    print(num1 * num2)

if operation == "/":
    if num2 == 0:
        print("Invalid operation!")
    if num2 != 0:
        print(num1 / num2)

if operation != "+" and operation != "-" and operation != "*" and operation != "/":
    print("Invalid operation!")
#5) შეამოწმეთ რესურსებში ჩაგდებული სურათი და მის მიხედვით დაწერეთ კომენტარებად ან პრეზენტაციაში მოქმედედების თანმიმდევრობა და საბოლოო პასუხი, ასევე როგორც ნამდვილი პითონის კოდი ###(შექმენით a,b,c ცვლადები, შექმენით result_0, result_1, result_2 ცვლადები და შეინახეთ თითოეულში შესაბამისი მნიშვნელობა და გამოპრინტეთ).  