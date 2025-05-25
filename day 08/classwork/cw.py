#მომხმარებელს შემოატანინეთ სამი რიცხვი, start/end/step და ჩასვით for loop-ში სათანადო ადგილას.
start = int(input("Enter the starting number (start): "))
end = int(input("Enter the ending number (end): "))
step = int(input("Enter the step value (step): "))

for i in range(start, end, step):
    print(i)

#მომხმარებელს შემოატანინეთ რიცხვი და დაპრინტეთ რიცხვი ყოველ იტერაციაზე იქამდე, სანამ რიცხვი მომხმარებლის რიცხვს არ გაუტოლდება (While Loop)

user_number = int(input("Enter a number: "))

i = 0

while i <= user_number:
    print(i)
    i += 1