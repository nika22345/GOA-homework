#ახსენით რა განსხვავებაა implicit და explicit datatype comversion-ში.

x = 5       # integer
y = 2.5     # float
result = x + y  # Python გარდაქმნის x-ს float-ად

print(result)  # 7.5 (float)

#შექმენით პროგრამა რომელიც მიიღებს მომხარებლისგან input-ს რიხვის სახით და დაბეჭდეთ ამ რიცხვამდე ყველა რიცხვი თანმიმდევრობით. (For loop)

number = int(input("Enter a number: "))

for i in range(number + 1):
    print(i)



#გაალეთეთ მეოთხე დავალება While loop-ის გამოყენებით.
while True:
    name = input("Enter Your Name: ")
    age = input("Enter Your Age: ")

    print(f"First Name: {name}")
    print(f"Age: {age}")

    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    print(num1 + num2)
    print(num2 - num1)
    print(num1 * num2)
    print(num2 / num1)

    width = float(input("Enter Width: "))
    height = float(input("Enter Height: "))

    S = width * height
    P = 2 * (width + height)

    print(f"area {S}")
    print(f"perimeter {P}")

    break