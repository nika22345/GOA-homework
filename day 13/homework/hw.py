# დავალება 1: წნევის ანალიზი მომხმარებელი შეიყვანს ორ მაჩვენებელს: სისტოლური და დიასტოლური წნევა.



systolic = int(input("Enter systolic blood pressure: "))
diastolic = int(input("Enter diastolic blood pressure: "))

if systolic > 140 or diastolic > 90:
    print("High blood pressure")
elif systolic < 90 or diastolic < 60:
    print("Low blood pressure")
else:
    print("Blood pressure is normal")


#დავალება 2: წონის შეფასება ასაკის მიხედვით (უბრალოდ და ლოგიკურად)

age = int(input("Enter your age: "))
weight = int(input("Enter your weight: "))

if age < 10:
    result = "Consider gaining weight" if weight < 20 else "Your weight seems fine" if weight <= 40 else "You might want to watch your weight"
elif age < 18:
    result = "You might need to gain some weight" if weight < 40 else "Your weight appears to be within a normal range" if weight <= 65 else "It could be beneficial to manage your weight"
else:
    result = "You may need to gain weight" if weight < 50 else "Your weight looks okay" if weight <= 90 else "Managing your weight might be helpful"

print(result)



# დავალება 3: ასაკის შეჯერება დღის მონაკვეთთან შეიყვანოს მომხმარებელმა ასაკი და საათი (0-დან 23-მდე)


age = int(input("Enter your age: "))
hour = int(input("Enter the current hour (0-23): "))

if age < 18 and hour >= 22:
    message = "It's time to sleep"
elif age >= 60 and hour >= 21:
    message = "Rest is recommended"
else:
    message = "You can continue your activities"

print(message)

#დავალება 4: ფიზიკური აქტივობის რეკომენდაცია მომხმარებელი შეიყვანს თავის ასაკს და გულის ცემას.


age = int(input("Enter your age: "))
heart_rate = int(input("Enter your heart rate: "))

if age < 30 and heart_rate < 140:
    message = "You can exercise more"
elif age >= 30 and heart_rate > 170:
    message = "You need to rest"
else:
    message = "Your activity level is normal"

print(message)