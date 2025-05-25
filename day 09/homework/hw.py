#შექმენით პროგრამა რომელიც მიიღებს მომხარებლისგან input-ს რიხვის სახით და დაბეჭდეთ ამ რიცხვამდე ყველა რიცხვი თანმიმდევრობით. (For loop)
number = int(input("Enter a number: "))

for i in range(number + 1):
    print(i)



#გაალეთეთ მეოთხე დავალება While loop-ის გამოყენებით.
number = int(input("შეიყვანე რიცხვი: "))

i = 0
while i <= number:
    print(i)
    i += 1