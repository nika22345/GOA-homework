# შექმენით ხუთი ცვლადი და გამოიყენეთ ეს ცვლადები რომ შეადგინოთ წინადადება
name = "nika"
last_name = "kalandadze"
age = 15
city = "Tbilisi"
Height = 1.80

print(f"chemi saxeli aris {name} ,chemi gvari aris {last_name} , me var {age}wlis , me vcxovrob {city}shi, chemi simaglea {Height}")
#2) დაარქვით ამ ცვლადებს snake_case სინტაქსით

#3) მომხმარებელს შეატანინეთ მისი სახელი გვარი და ასაკი და შემდეგ გამოიტანეთ ისინი outpout-ში შედეგი გამოსახულებით -სახელი: {შემოყვანილი სახელი}- (იგივე ყველა ცვლადზე)
name = input("Enter Your Name:")
last_name = input("Enter Your Last Name")
age = input("Enter Your Age")

print(f"Saxeli: {name}")
print(f"Gvari: {last_name}")
print(f"Asaki: {age}")